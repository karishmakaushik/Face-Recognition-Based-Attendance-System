# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Add_Student.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Model.add_students import Add_Student


class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(1054, 718)
                MainWindow.setMinimumSize(QtCore.QSize(1054, 718))
                MainWindow.setMaximumSize(QtCore.QSize(1054, 718))
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.label = QtWidgets.QLabel(self.centralwidget)
                self.label.setGeometry(QtCore.QRect(170, -20, 751, 141))
                font = QtGui.QFont()
                font.setFamily("MS UI Gothic")
                font.setPointSize(25)
                font.setBold(True)
                font.setUnderline(False)
                font.setWeight(75)
                self.label.setFont(font)
                self.label.setObjectName("label")
                self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
                self.graphicsView.setGeometry(QtCore.QRect(170, 120, 721, 441))
                self.graphicsView.setStyleSheet("QGraphicsView{\n"
        "    border:3px solid black;\n"
        "}")
                self.graphicsView.setObjectName("graphicsView")
                self.take_photo = QtWidgets.QPushButton(self.centralwidget)
                self.take_photo.setGeometry(QtCore.QRect(420, 310, 191, 31))
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                self.take_photo.setFont(font)
                self.take_photo.setStyleSheet("")
                self.take_photo.setObjectName("take_photo")
                self.add = QtWidgets.QPushButton(self.centralwidget)
                self.add.setGeometry(QtCore.QRect(780, 540, 101, 31))
                self.add.setStyleSheet("QPushButton{\n"
        "    background-color:rgb(188, 255, 202);\n"
        "    border: 1px solid rgb(0, 0, 0);\n"
        "}")
                self.add.setObjectName("add")
                self.discard = QtWidgets.QPushButton(self.centralwidget)
                self.discard.setGeometry(QtCore.QRect(180, 540, 101, 31))
                self.discard.setStyleSheet("QPushButton{\n"
        "    background-color:rgb(255, 220, 211);\n"
        "    border: 1px solid rgb(0, 0, 0);\n"
        "}")
                self.discard.setObjectName("discard")
                self.id = QtWidgets.QLineEdit(self.centralwidget)
                self.id.setGeometry(QtCore.QRect(250, 220, 561, 41))
                font = QtGui.QFont()
                font.setFamily("Gadugi")
                font.setPointSize(12)
                font.setBold(False)
                font.setWeight(50)
                self.id.setFont(font)
                self.id.setWhatsThis("")
                self.id.setAutoFillBackground(False)
                self.id.setStyleSheet("QLineEdit{\n"
        "    background-color:rgb(250, 255, 226);\n"
        "    border: 1px solid rgb(107, 29, 13);\n"
        "}")
                self.id.setText("")
                self.id.setMaxLength(40)
                self.id.setObjectName("id")
                self.label_2 = QtWidgets.QLabel(self.centralwidget)
                self.label_2.setGeometry(QtCore.QRect(250, 170, 211, 41))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(12)
                self.label_2.setFont(font)
                self.label_2.setObjectName("label_2")
                self.frame_delay = QtWidgets.QSpinBox(self.centralwidget)
                self.frame_delay.setGeometry(QtCore.QRect(340, 440, 91, 31))
                self.frame_delay.setMinimum(5)
                self.frame_delay.setMaximum(50)
                self.frame_delay.setSingleStep(5)
                self.frame_delay.setProperty("value", 15)
                self.frame_delay.setObjectName("frame_delay")
                self.label_3 = QtWidgets.QLabel(self.centralwidget)
                self.label_3.setGeometry(QtCore.QRect(340, 400, 111, 41))
                font = QtGui.QFont()
                font.setFamily("Comic Sans MS")
                font.setPointSize(8)
                font.setItalic(False)
                self.label_3.setFont(font)
                self.label_3.setObjectName("label_3")
                self.label_4 = QtWidgets.QLabel(self.centralwidget)
                self.label_4.setGeometry(QtCore.QRect(600, 400, 111, 41))
                font = QtGui.QFont()
                font.setFamily("Comic Sans MS")
                font.setPointSize(8)
                font.setItalic(False)
                self.label_4.setFont(font)
                self.label_4.setObjectName("label_4")
                self.no_of_images = QtWidgets.QSpinBox(self.centralwidget)
                self.no_of_images.setGeometry(QtCore.QRect(600, 440, 91, 31))
                self.no_of_images.setMinimum(40)
                self.no_of_images.setMaximum(200)
                self.no_of_images.setSingleStep(5)
                self.no_of_images.setProperty("value", 50)
                self.no_of_images.setObjectName("no_of_images")
                MainWindow.setCentralWidget(self.centralwidget)
                self.menubar = QtWidgets.QMenuBar(MainWindow)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 1054, 26))
                self.menubar.setObjectName("menubar")
                MainWindow.setMenuBar(self.menubar)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)

                self.add.clicked.connect(self.add_student)
                self.discard.clicked.connect(self.discard_fn)
                self.take_photo.clicked.connect(self.take_photo_fn)

                self.take_photo_flag = False
                self.start_flag = False

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "Add Students"))
                self.label.setText(_translate("MainWindow", "Face Recognition -Attendance System"))
                self.take_photo.setText(_translate("MainWindow", "Take Photos"))
                self.add.setText(_translate("MainWindow", "Add"))
                self.discard.setText(_translate("MainWindow", "Discard"))
                self.id.setPlaceholderText(_translate("MainWindow", "40 characters max", "Enter User Id"))
                self.label_2.setText(_translate("MainWindow", "Enter User ID"))
                self.label_3.setText(_translate("MainWindow", "set frame-delay"))
                self.label_4.setText(_translate("MainWindow", "total images"))

        def add_student(self):
                self.student_id = self.id.text()
                if self.student_id == "":
                        self.popup = QtWidgets.QMessageBox(self.menubar)
                        self.popup.setIcon(QtWidgets.QMessageBox.Warning)
                        self.popup.setText("Invalid User")
                        self.popup.setInformativeText("User cannot be empty string")
                        self.popup.setDefaultButton(QtWidgets.QMessageBox.Cancel)
                        self.popup.exec_()
                elif self.take_photo_flag == True:
                        self.popup = QtWidgets.QMessageBox(self.menubar)
                        self.popup.setIcon(QtWidgets.QMessageBox.Information)
                        self.popup.setText(self.student_id)
                        self.popup.setInformativeText("Added Successfully")
                        self.popup.setDefaultButton(QtWidgets.QMessageBox.Cancel)
                        self.popup.exec_()
                else:
                        self.start_flag = True
                        self.take_photo_fn()
                        

        def take_photo_fn(self):
                self.student_id = self.id.text()
                if self.student_id == "":
                        self.popup = QtWidgets.QMessageBox(self.menubar)
                        self.popup.setIcon(QtWidgets.QMessageBox.Warning)
                        self.popup.setText("Invalid User")
                        self.popup.setInformativeText("User cannot be empty string")
                        self.popup.setDefaultButton(QtWidgets.QMessageBox.Cancel)
                        self.popup.exec_()
                else:
                        add_student_obj = Add_Student(self.student_id, use_webcam=True, student_dir='./Model/student_dir_captured')
                        add_student_obj.capture_image(delay=int(self.frame_delay.text()), no_of_images=int(self.no_of_images.text()))

                        self.take_photo_flag = True

        def discard_fn(self):
                self.student_id = None
                self.id.setText("")
                self.take_photo_flag = False
                self.start_flag = False



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
