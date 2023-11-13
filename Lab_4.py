import sys
from PyQt5 import QtWidgets, QtGui
from get_next import get_next_instance


class DatasetApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Определяется интерфейс
        self.setWindowTitle('Dataset App')
        self.setGeometry(100, 100, 1300, 700)
        self.folderpath = None  # Переменная для хранения пути к папке с исходным датасетом

        # Кнопка для выбора папки с исходным датасетом
        self.browse_button = QtWidgets.QPushButton('Выбрать папку с датасетом', self)
        self.browse_button.setGeometry(20, 20, 200, 30)
        self.browse_button.clicked.connect(self.browse_dataset_folder)

        # Кнопка для создания файла аннотации
        self.create_annotation_button = QtWidgets.QPushButton('Создать аннотацию', self)
        self.create_annotation_button.setGeometry(20, 60, 200, 30)
        self.create_annotation_button.setEnabled(False)  # По умолчанию отключена
        self.create_annotation_button.clicked.connect(self.create_annotation)

        # Кнопки для получения следующего экземпляра
        self.next_class1_button = QtWidgets.QPushButton('Следующая кошка', self)
        self.next_class1_button.setGeometry(20, 100, 200, 30)
        self.next_class1_button.setEnabled(False)  # По умолчанию отключена
        self.next_class1_button.clicked.connect(self.get_next_class1)

        self.next_class2_button = QtWidgets.QPushButton('Следующая собака', self)
        self.next_class2_button.setGeometry(20, 140, 200, 30)
        self.next_class2_button.setEnabled(False)  # По умолчанию отключена
        self.next_class2_button.clicked.connect(self.get_next_class2)

        self.image_label = QtWidgets.QLabel(self)
        self.image_label.setGeometry(250, 20, 1000, 600)  
        self.image_label.setScaledContents(True)

    def browse_dataset_folder(self):
        self.folderpath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Выберите папку с исходным датасетом')
        if self.folderpath:
            self.create_annotation_button.setEnabled(True)
            self.next_class1_button.setEnabled(True)
            self.next_class2_button.setEnabled(True)

    
    def get_next_class1(self):
        if self.folderpath:
            next_instance = get_next_instance('cat', self.folderpath)
            if next_instance:
                pixmap = QtGui.QPixmap(next_instance)
                self.image_label.setPixmap(pixmap)

    def get_next_class2(self):
        if self.folderpath:
            next_instance = get_next_instance('dog', self.folderpath)
            if next_instance:
                pixmap = QtGui.QPixmap(next_instance)
                self.image_label.setPixmap(pixmap)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = DatasetApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
