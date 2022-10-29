import datetime
import sys
from collections import defaultdict
from PySide6.QtCore import QSize, QCoreApplication
from PySide6.QtGui import QPixmap, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMdiArea, QMdiSubWindow, QTextEdit, QDialog, \
    QVBoxLayout, QLabel, QSizePolicy, QHBoxLayout, QSpacerItem, QPushButton
from design import Ui_MainWindow
from delete_design import Ui_DeleteWindow
from imutils import paths
import numpy as np
import cv2
import os
import sqlite3

DIR = os.path.dirname(__file__)
db = sqlite3.connect(os.path.join(DIR, "delete_images.db"))
SQL = db.cursor()

SQL.execute("""CREATE TABLE if not exists delete_images(
    _id INTEGER PRIMARY KEY AUTOINCREMENT,
    image_bytes BLOB,
    image_name text)""")
db.commit()


class DeleteWindow(QMainWindow):
    def __init__(self, parent=None):
        super(DeleteWindow, self).__init__(parent)
        self.ui = Ui_DeleteWindow()
        self.ui.setupUi(self)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.mdi = QMdiArea()
        self.ui.open_folder_button.clicked.connect(self.browse_folder)
        self.ui.next_button.clicked.connect(self.open_next_image)
        self.ui.back_button.clicked.connect(self.open_prev_image)
        self.ui.delete_button_2.clicked.connect(self.delete_double_image)
        self.ui.open_restore_window.clicked.connect(self.open_restore_window)
        self.directory = None
        self.imageList = None
        self.hashes = []
        self.hash_idx = 0
        self.originals = []
        self.pairs = []
        self.pathsImage = []
        self.double_count = 0
        self.deleted_images_dict = defaultdict(dict)
        self.deleted_images_count = 0

    def dhash(self, image, hashSize=8):
        # пробразовываем изображение в оттенки серого и изменяем
        # его размер, затем добавляем столбец ширины, чтобы
        # можно было вычислить горизонтальный градиет
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        resized = cv2.resize(gray, (hashSize + 1, hashSize))

        # вычисляем относительный горизонтальный градиент
        # между пикселями соседних столбцов
        diff = resized[:, 1:] > resized[:, :-1]

        # преобразуем разностное изображение в хэш и возвращаем его
        return sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])

    def pars_image(self):
        print("[INFO] вычисляем хэш изображений")

        images_count = len(self.imageList)  # общее количество картинок в папке(для счетчика)
        image_number = 0  # количество картинок пропарсено
        one_percent = images_count // 100 if images_count >= 100 else 1

        # проходим по списку изображений
        for imagePath in self.imageList:
            # загружаем входное изображение и вычисляем хэш
            image = cv2.imdecode(np.fromfile(str(imagePath), dtype=np.uint8), cv2.IMREAD_COLOR)
            h = self.dhash(image)

            # добавляем в список хэш изображения
            self.hashes.append(h)
            # и в новый список путь к изображению
            self.pathsImage.append(imagePath)
            image_number += 1
            # вычисляем процент для прогресс бара
            if image_number % one_percent == 0 or image_number == images_count:
                self.ui.progressBar.setValue((image_number/images_count)*100)

        for ind, h in enumerate(self.hashes):
            if h in self.originals: continue
            for ind2, h2 in enumerate(self.hashes[ind + 1:]):
                ind2 += ind + 1
                if h == h2:
                    self.pairs.append((ind, ind2))
            self.originals.append(h)

    # отправляем изображения в гуи
    def show_image(self):
        idxs = self.pairs[self.hash_idx]
        original_pixmap = QPixmap(f'{self.imageList[idxs[0]]}')
        double_pixmap = QPixmap(f'{self.imageList[idxs[1]]}')

        # вычисляем нужный размер изображения из размера лейбла и самого изображения
        height = original_pixmap.height() / original_pixmap.width() * self.ui.original.width()
        if height > self.ui.original.height():
            height = self.ui.original.height()
            width = original_pixmap.width() / original_pixmap.height() * height
        else:
            width = self.ui.original.width()

        self.double_count = len([None for i in self.pairs if i[0] == self.pairs[self.hash_idx][0] and self.pathsImage[i[1]].split('\\')[-1] in os.listdir(self.directory)])
        self.ui.duble_count.setText(f'Число копий: {self.double_count}')
        self.ui.original.setPixmap(original_pixmap.scaled(width, height))
        self.ui.duble.setPixmap(double_pixmap.scaled(width, height))

    # логика кнопки "Далее"
    def open_next_image(self):
        if self.pairs:
            self.hash_idx += 1
            if self.hash_idx >= len(self.pairs):
                self.hash_idx = 0
            while_counter = 0
            while self.pathsImage[self.pairs[self.hash_idx][1]].split('\\')[-1] not in os.listdir(self.directory):
                while_counter += 1
                self.hash_idx += 1
                if self.hash_idx >= len(self.pairs):
                    self.hash_idx = 0
                if while_counter > len(self.pairs):
                    self.ui.original.setText('Дублей больше нет')
                    self.ui.duble.setText('Дублей больше нет')
                    return
            self.show_image()

    # логика кнопки "Назад"
    def open_prev_image(self):
        if self.pairs:
            self.hash_idx -= 1
            if self.hash_idx < 0:
                self.hash_idx = len(self.pairs) - 1
            while_counter = 0
            while self.pathsImage[self.pairs[self.hash_idx][1]].split('\\')[-1] not in os.listdir(self.directory):
                while_counter += 1
                self.hash_idx -= 1
                if self.hash_idx < 0:
                    self.hash_idx = len(self.pairs) - 1
                if while_counter > len(self.pairs):
                    self.ui.original.setText('Дублей больше нет')
                    self.ui.duble.setText('Дублей больше нет')
                    return
            self.show_image()

    # логика кнопки "Удалить"
    def delete_double_image(self):
        if self.pairs:
            if self.pathsImage[self.pairs[self.hash_idx][1]].split('\\')[-1] in os.listdir(self.directory):
                with open(self.pathsImage[self.pairs[self.hash_idx][1]], 'rb') as file:
                    blob_image = file.read()
                image_name = self.pathsImage[self.pairs[self.hash_idx][1]].split('\\')[-1]
                sqlite_insert_blob_query = "INSERT INTO delete_images(image_bytes, image_name) VALUES (?, ?)"
                data_tuple = (blob_image, image_name)
                SQL.execute(sqlite_insert_blob_query, data_tuple)
                db.commit()

                os.remove(self.pathsImage[self.pairs[self.hash_idx][1]])
            self.open_next_image()

    # логика кнопки выбора пути до папки с изображениями
    def browse_folder(self):
        self.ui.folder_line_edit.clear()
        self.directory = QFileDialog.getExistingDirectory(self, "Выберите папку")
        # открыть диалог выбора директории и установить значение переменной
        # равной пути к выбранной директории

        if self.directory:  # не продолжать выполнение, если пользователь не выбрал директорию
            self.hash_idx = 0
            self.pairs = []
            self.originals = []
            self.hashes = []
            self.pathsImage = []
            self.imageList = list(paths.list_images(self.directory))
            if not self.imageList:
                self.ui.original.setText('В папке нет картинок')
                self.ui.duble.setText('В папке нет картинок')
                return
            self.ui.folder_line_edit.setText(self.directory)
            self.ui.original.setText('Подождите, идет поиск')
            self.ui.duble.setText('Подождите, идет поиск')
            self.pars_image()
            if not self.pairs:
                self.ui.original.setText('Дублей не найдено')
                self.ui.duble.setText('Дублей не найдено')
                return
            self.show_image()

    def open_restore_window(self):
        deleted_images = SQL.execute("SELECT * FROM delete_images").fetchall()
        self.delete_window = DeleteWindow()

        # если удаленных изображений нет
        if not deleted_images:
            # то создаем лейбл с надписью что их нет
            verticalLayout_img = QVBoxLayout()
            verticalLayout_img.setAlignment(Qt.AlignCenter)
            verticalLayout_img.setObjectName(f"verticalLayout")
            restore_label = QLabel(self.delete_window.ui.scrollAreaWidgetContents)
            restore_label.setObjectName(u"restore_label")
            restore_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            restore_label.setAlignment(Qt.AlignCenter)
            verticalLayout_img.addWidget(restore_label)
            self.delete_window.ui.verticalLayout.addLayout(verticalLayout_img)
            restore_label.setText("Удаленных изображений не обнаружено")

        # иначе генерируем интерфейс с изображениями и кнопкой
        else:
            self.deleted_images_count = len(deleted_images)
            for img in deleted_images:
                verticalLayout_img = QVBoxLayout()
                verticalLayout_img.setObjectName(f"verticalLayout_{img[0]}")
                restore_label = QLabel(self.delete_window.ui.scrollAreaWidgetContents)
                restore_label.setObjectName(u"restore_label")
                sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                sizePolicy3.setHorizontalStretch(45)
                sizePolicy3.setVerticalStretch(45)
                sizePolicy3.setHeightForWidth(restore_label.sizePolicy().hasHeightForWidth())
                restore_label.setSizePolicy(sizePolicy3)
                restore_label.setMinimumSize(QSize(450, 250))
                restore_label.setMaximumSize(QSize(16777215, 16777215))

                verticalLayout_img.addWidget(restore_label)

                controls_horizontal_layout = QHBoxLayout()
                controls_horizontal_layout.setObjectName(f"controls_horizontal_layout_{img[0]}")
                controls_horizontal_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

                controls_horizontal_layout.addItem(controls_horizontal_spacer)

                restore_button = QPushButton(self.delete_window.ui.scrollAreaWidgetContents)
                restore_button.setObjectName(f"{img[0]}")
                self.delete_window.ui.sizePolicy1.setHeightForWidth(restore_button.sizePolicy().hasHeightForWidth())
                restore_button.setSizePolicy(self.delete_window.ui.sizePolicy1)
                restore_button.setStyleSheet(u"")

                controls_horizontal_layout.addWidget(restore_button)
                verticalLayout_img.addLayout(controls_horizontal_layout)
                self.delete_window.ui.verticalLayout.addLayout(verticalLayout_img)

                qp = QPixmap()
                qp.loadFromData(img[1])

                height = qp.height() / qp.width() * restore_label.width()
                if height > restore_label.height():
                    height = restore_label.height()
                    width = qp.width() / qp.height() * height
                else:
                    width = restore_label.width()

                restore_label.setText("")
                restore_label.setPixmap(qp.scaled(width, height))
                restore_button.setText(QCoreApplication.translate("MainWindow", "Восстановить", None))
                restore_button.clicked.connect(self.restore_image_func)

                self.deleted_images_dict[str(img[0])] = {'image': img[1],
                                                         'image_name': img[2],
                                                         'layout': verticalLayout_img}
        self.delete_window.show()  # Показываем окно

    # функции восстановления изображений
    def restore_image_func(self):
        if not os.path.exists('./restore_image'):
            os.mkdir('./restore_image')

        with open(f"./restore_image/{self.deleted_images_dict[self.sender().objectName()]['image_name']}", 'wb') as file:
            file.write(self.deleted_images_dict[self.sender().objectName()]['image'])

        SQL.execute(f"DELETE FROM delete_images WHERE _id = {self.sender().objectName()}")
        db.commit()

        # удаляем layout и всё что к нему относится
        layout = self.deleted_images_dict[self.sender().objectName()]['layout']
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.setParent(None)

        self.deleted_images_count -= 1

        # если восстановили все удаленные изображения
        # то создаем лейбл с надписью что удаленных изображений не осталось
        if self.deleted_images_count == 0:
            verticalLayout_img = QVBoxLayout()
            verticalLayout_img.setAlignment(Qt.AlignCenter)
            verticalLayout_img.setObjectName(f"verticalLayout")
            restore_label = QLabel(self.delete_window.ui.scrollAreaWidgetContents)
            restore_label.setObjectName(u"restore_label")
            restore_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            restore_label.setAlignment(Qt.AlignCenter)

            verticalLayout_img.addWidget(restore_label)
            self.delete_window.ui.verticalLayout.addLayout(verticalLayout_img)

            restore_label.setText("Больше удаленных изображений нет")


def main():
    app = QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MainWindow()  # Создаём объект класса MainWindow
    window.show()  # Показываем окно
    app.exec()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
