import os
import cv2
import sys
from PyQt5.QtGui import QImage
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog, QWidget, QMessageBox

class Window(QWidget):
    def __init__(self):
        super().__init__()

        # 设置窗口标题和大小
        self.setWindowTitle("座椅缺陷识别")
        self.setGeometry(200, 200, 1800, 1200)
        self.setWindowIcon(QIcon('app.png'))
    
        # 创建控件
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setStyleSheet("border: 2px solid gray;")
        self.result_label = QLabel(self)
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setStyleSheet("border: 2px solid gray;")
        self.select_button = QPushButton("选择图片", self)
        self.select_button.clicked.connect(self.select_image)
        self.detect_button = QPushButton("开始识别", self)
        self.detect_button.clicked.connect(self.detect_image)

        # 创建布局管理器
        self.layout = QVBoxLayout()
        self.image_layout = QHBoxLayout()
        self.image_layout.addWidget(self.image_label)
        self.image_layout.addWidget(self.result_label)
        self.control_layout = QHBoxLayout()
        self.control_layout.addWidget(self.select_button)
        self.control_layout.addWidget(self.detect_button)
        self.layout.addLayout(self.image_layout)
        self.layout.addLayout(self.control_layout)
        self.setLayout(self.layout)

        # 初始化分类器
        self.cascade_classifier = cv2.CascadeClassifier(os.getcwd() + "\\" + "data\\data2\\cascade.xml")

    def select_image(self):
        # 选择图片
        file_path, _ = QFileDialog.getOpenFileName(self, "选择图片", ".", "Images (*.png *.jpg *.bmp)")
        if file_path:
            try:
                # 加载图片并显示
                self.image = cv2.imread(file_path)
                if self.image is None:
                    raise Exception("无法加载图片，请选择其他图片！")
                # 缩放图像到指定大小
                # print(self.image_label.width(), self.image_label.height())
                # scale_ratio = min(self.image_label.width() / self.image.shape[1], self.image_label.height() / self.image.shape[0])
                # self.image = cv2.resize(self.image, None, fx=scale_ratio, fy=scale_ratio)
                self.image = cv2.resize(self.image, (800, 1000))
                self.show_image(self.image, self.image_label)
            except Exception as e:
                print("Error: ", e)
                QMessageBox.critical(self, "Error", "无法加载图片，请选择其他图片！\n请检查图片路径中是否含有中文!")


    def detect_image(self):
        if hasattr(self, 'image'):
            # 进行目标识别
            img_gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            objects = self.cascade_classifier.detectMultiScale(img_gray)
            img_with_box = self.image.copy()
            for (x, y, w, h) in objects:
                cv2.rectangle(img_with_box, (x, y), (x + w, y + h), (0, 255, 0), 2)
            self.show_image(img_with_box, self.result_label)
        else:
            self.result_label.setText("请先选择一张图片")
        

    def show_image(self, image, label):
        # 将OpenCV图像转换为QPixmap格式并显示
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # print(image.shape)
        qimage = QPixmap.fromImage(QImage(rgb_image.data, rgb_image.shape[1], rgb_image.shape[0], QImage.Format_RGB888))
        label.setPixmap(qimage)
                
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
