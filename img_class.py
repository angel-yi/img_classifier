# -*- coding: utf-8 -*-
"""
图片分类工具
"""
import multiprocessing
import os
import shutil
import sys
from loguru import logger
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import config as cfg

logger.add('./log/log.log')


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(150, 460, 111, 51))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(340, 460, 111, 51))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(300, 10, 171, 41))
        font = QFont()
        font.setFamily(u"Agency FB")
        font.setPointSize(20)
        self.label.setFont(font)
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(630, 50, 111, 51))
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(630, 130, 111, 51))
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(630, 210, 111, 51))
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(630, 290, 111, 51))
        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(630, 370, 111, 51))
        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(630, 450, 111, 51))
        self.pushButton_9 = QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(10, 50, 91, 41))
        self.pushButton_10 = QPushButton(self.centralwidget)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(10, 510, 81, 41))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 60, 441, 31))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(100, 520, 441, 31))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 110, 541, 321))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"没有菜单", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4e00\u5f20", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u5f20", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u5206\u7c7b\u5de5\u5177", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u5206\u7c7b1", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u5206\u7c7b2", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u5206\u7c7b3", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u5206\u7c7b4", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u5206\u7c7b5", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u5206\u7c7b6", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u56fe\u7247", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u8def\u5f84", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u5de5\u4f5c\u8def\u5f84", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u8def\u5f84", None))
        # self.label_4.setText(QCoreApplication.translate("MainWindow", u"图片预览", None))
    # retranslateUi


class MyMainWindow(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(MainWindow)
        self.label_3.setText('保存路径下如果没有分类对应的文件夹将自动创建与分类对应的文件夹')
        # '上一张'
        self.pushButton.clicked.connect(self.previous_file)
        # '下一张'
        self.pushButton_2.clicked.connect(self.next_file_2)
        # '分类1'
        self.pushButton_3.clicked.connect(self.class_1)
        # '分类2'
        self.pushButton_4.clicked.connect(self.class_2)
        # '分类3'
        self.pushButton_5.clicked.connect(self.class_3)
        # '分类4'
        self.pushButton_6.clicked.connect(self.class_4)
        # '分类5'
        self.pushButton_7.clicked.connect(self.class_5)
        # '分类6'
        self.pushButton_8.clicked.connect(self.class_6)
        # '导入图片路径'
        self.pushButton_9.clicked.connect(self.open_files)
        # '保存图片路径'
        self.pushButton_10.clicked.connect(self.save_files)

        button_calss = {
            0: self.pushButton_3,
            1: self.pushButton_4,
            2: self.pushButton_5,
            3: self.pushButton_6,
            4: self.pushButton_7,
            5: self.pushButton_8,
        }

        self.cls_dir = {
            0: '',
            1: '',
            2: '',
            3: '',
            4: '',
            5: ''
        }

        if cfg.use_chines:
            self.img_class = cfg.img_class_ch
        else:
            self.img_class = cfg.img_class
        for k, v in self.img_class.items():
            button_calss[k].setText(v)
        self.index = 0

    def get_img(self, index):
        try:
            img_path = os.path.join(self.dir_path, self.all_imgs[index])
        except:
            img_path = False
        return img_path

    def open_files(self):
        open_file = QFileDialog.getExistingDirectoryUrl(None, '选择文件')
        self.dir_path = open_file.path()[1:]
        print(self.dir_path)
        self.all_imgs = os.listdir(self.dir_path)
        print(len(self.all_imgs))
        self.label_2.setText(self.dir_path + ' ' + f'共{len(self.all_imgs)}个文件')
        self.next_file()


    def save_files(self):
        open_file = QFileDialog.getExistingDirectoryUrl(None, '选择文件')
        self.save_dir = open_file.path()[1:]
        self.label_3.setText(self.save_dir)
        if self.save_dir:
            temp_dirs = os.listdir(self.save_dir)
            for k, v in self.img_class.items():
                if v not in temp_dirs:
                    os.mkdir(os.path.join(self.save_dir, v))
                self.cls_dir[k] = os.path.join(self.save_dir, v)

    def previous_file(self):
        self.index -= 1
        img_path = self.get_img(self.index)
        print(img_path)
        self.label_4.setPixmap(img_path)
        self.label_4.setScaledContents(True)
        logger.info(f'{self.index} {img_path}')

    def next_file_2(self):
        self.index += 1
        img_path = self.get_img(self.index)
        logger.info(f'{self.index} {img_path}')
        print(img_path)
        if isinstance(img_path, bool):
            self.label_4.setText('所有图像已分类完成')
        else:
            self.label_4.setPixmap(img_path)
            self.label_4.setScaledContents(True)
            # self.index += 1
            logger.info(f'{self.index} {img_path}')

    def next_file(self):
        img_path = self.get_img(self.index)
        logger.info(f'{self.index} {img_path}')
        print(img_path)
        if isinstance(img_path, bool):
            self.label_4.setText('所有图像已分类完成')
        else:
            self.label_4.setPixmap(img_path)
            self.label_4.setScaledContents(True)
            # self.index += 1
            logger.info(f'{self.index} {img_path}')

    def class_1(self):
        logger.info(f'{self.index} {self.all_imgs[self.index]}')
        shutil.move(
            os.path.join(self.dir_path, self.all_imgs[self.index]),
            os.path.join(self.cls_dir[0], os.path.basename(self.all_imgs[self.index]))
        )
        logger.info(f'{os.path.join(self.dir_path, self.all_imgs[self.index]), os.path.join(self.cls_dir[0], os.path.basename(self.all_imgs[self.index]))}')
        self.index += 1
        self.next_file()

    def class_2(self):
        logger.info(f'{self.index} {self.all_imgs[self.index]}')
        shutil.move(
            os.path.join(self.dir_path, self.all_imgs[self.index]),
            os.path.join(self.cls_dir[1], os.path.basename(self.all_imgs[self.index]))
        )
        logger.info(
            f'{os.path.join(self.dir_path, self.all_imgs[self.index]), os.path.join(self.cls_dir[1], os.path.basename(self.all_imgs[self.index]))}')
        self.index += 1
        self.next_file()

    def class_3(self):
        logger.info(f'{self.index} {self.all_imgs[self.index]}')
        shutil.move(
            os.path.join(self.dir_path, self.all_imgs[self.index]),
            os.path.join(self.cls_dir[2], os.path.basename(self.all_imgs[self.index]))
        )
        logger.info(
            f'{os.path.join(self.dir_path, self.all_imgs[self.index]), os.path.join(self.cls_dir[2], os.path.basename(self.all_imgs[self.index]))}')
        self.index += 1
        self.next_file()

    def class_4(self):
        logger.info(f'{self.index} {self.all_imgs[self.index]}')
        shutil.move(
            os.path.join(self.dir_path, self.all_imgs[self.index]),
            os.path.join(self.cls_dir[3], os.path.basename(self.all_imgs[self.index]))
        )
        logger.info(
            f'{os.path.join(self.dir_path, self.all_imgs[self.index]), os.path.join(self.cls_dir[3], os.path.basename(self.all_imgs[self.index]))}')
        self.index += 1
        self.next_file()

    def class_5(self):
        logger.info(f'{self.index} {self.all_imgs[self.index]}')
        shutil.move(
            os.path.join(self.dir_path, self.all_imgs[self.index]),
            os.path.join(self.cls_dir[4], os.path.basename(self.all_imgs[self.index]))
        )
        logger.info(
            f'{os.path.join(self.dir_path, self.all_imgs[self.index]), os.path.join(self.cls_dir[4], os.path.basename(self.all_imgs[self.index]))}')
        self.index += 1
        self.next_file()

    def class_6(self):
        logger.info(f'{self.index} {self.all_imgs[self.index]}')
        shutil.move(
            os.path.join(self.dir_path, self.all_imgs[self.index]),
            os.path.join(self.cls_dir[5], os.path.basename(self.all_imgs[self.index]))
        )
        logger.info(
            f'{os.path.join(self.dir_path, self.all_imgs[self.index]), os.path.join(self.cls_dir[5], os.path.basename(self.all_imgs[self.index]))}')
        self.index += 1
        self.next_file()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    multiprocessing.freeze_support()
    myUI = MyMainWindow()
    MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())
    MainWindow.show()
    sys.exit(app.exec_())
