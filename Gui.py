
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

from AudioRecorder import *
from Transcribe import *
from Translate import *
from Synthesizer import *
#from Prediction import *
import files_rc
import time
from prediction import *
from ibmWatson import *

guiAUD = RecAUD()


transcribed = ""
translated = ""
destLanguage = "ar"

class Worker(QObject):
    finished = pyqtSignal()
    #progress = pyqtSignal(int)

    def run(self):

        guiAUD.start_record()
        self.finished.emit()


class Ui_MainWindow(QWidget): #Qwidget instead of object
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.setFixedSize(1009, 722)
        MainWindow.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btn_play_output = QPushButton(self.centralwidget)
        self.btn_play_output.setObjectName(u"btn_play_output")
        self.btn_play_output.setGeometry(QRect(910, 20, 61, 61))
        self.btn_play_output.setStyleSheet(u"QPushButton {\n"
                                           "	border: 2px solid rgb(52, 59, 72);\n"
                                           "	border-radius: 30px;	\n"
                                           "	background-color: rgb(52, 59, 72);\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "	background-color: rgb(57, 65, 80);\n"
                                           "	border: 2px solid rgb(61, 70, 86);\n"
                                           "}\n"
                                           "QPushButton:pressed {	\n"
                                           "	background-color: rgb(0, 120, 215);\n"
                                           "	border: 2px solid rgb(43, 50, 61);\n"
                                           "}")
        icon = QIcon()
        icon.addFile(u"cil-volume-high.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_play_output.setIcon(icon)
        self.btn_open = QPushButton(self.centralwidget)
        self.btn_open.setObjectName(u"btn_open")
        self.btn_open.setGeometry(QRect(819, 580, 101, 30))
        self.btn_open.setMinimumSize(QSize(11, 11))
        palette = QPalette()
        brush = QBrush(QColor(210, 210, 210, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(52, 59, 72, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(210, 210, 210, 128))
        brush2.setStyle(Qt.SolidPattern)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
# endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
# endif
        brush3 = QBrush(QColor(120, 120, 120, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush4 = QBrush(QColor(0, 0, 0, 128))
        brush4.setStyle(Qt.SolidPattern)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
# endif
        self.btn_open.setPalette(palette)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(9)
        self.btn_open.setFont(font)
        self.btn_open.setStyleSheet(u"QPushButton {\n"
                                    "	border: 2px solid rgb(52, 59, 72);\n"
                                    "	border-radius: 5px;	\n"
                                    "	background-color: rgb(52, 59, 72);\n"
                                    "}\n"
                                    "QPushButton:hover {\n"
                                    "	background-color: rgb(57, 65, 80);\n"
                                    "	border: 2px solid rgb(61, 70, 86);\n"
                                    "}\n"
                                    "QPushButton:pressed {	\n"
                                    "	background-color: rgb(35, 40, 49);\n"
                                    "	border: 2px solid rgb(43, 50, 61);\n"
                                    "}")
        icon1 = QIcon()
        icon1.addFile(u":/16x16/icons/16x16/cil-folder-open.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.btn_open.setIcon(icon1)
        self.lineEdit_path = QLineEdit(self.centralwidget)
        self.lineEdit_path.setObjectName(u"lineEdit_path")
        self.lineEdit_path.setGeometry(QRect(544, 580, 291, 30))
        self.lineEdit_path.setMinimumSize(QSize(0, 30))
        palette1 = QPalette()
        brush5 = QBrush(QColor(27, 29, 35, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush5)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
# endif
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush5)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
# endif
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush5)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
# endif
        self.lineEdit_path.setPalette(palette1)
        self.lineEdit_path.setStyleSheet(u"QLineEdit {\n"
                                         "	background-color: rgb(27, 29, 35);\n"
                                         "	border-radius: 5px;\n"
                                         "	border: 2px solid rgb(27, 29, 35);\n"
                                         "	padding-left: 10px;\n"
                                         "}\n"
                                         "QLineEdit:hover {\n"
                                         "	border: 2px solid rgb(64, 71, 88);\n"
                                         "}\n"
                                         "QLineEdit:focus {\n"
                                         "	border: 2px solid rgb(91, 101, 124);\n"
                                         "}")
        self.Ptext_output = QPlainTextEdit(self.centralwidget)
        self.Ptext_output.setObjectName(u"Ptext_output")
        self.Ptext_output.setGeometry(QRect(530, 50, 411, 291))
        self.Ptext_output.setMinimumSize(QSize(200, 200))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush5)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
# endif
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush5)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
# endif
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush5)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
# endif
        self.Ptext_output.setPalette(palette2)
        font1 = QFont()
        font1.setPointSize(10)
        self.Ptext_output.setFont(font1)
        self.Ptext_output.setStyleSheet(u"QPlainTextEdit {\n"
                                        "	background-color: rgb(27, 29, 35);\n"
                                        "	border-radius: 5px;\n"
                                        "	padding: 10px;\n"
                                        "}\n"
                                        "QPlainTextEdit:hover {\n"
                                        "	border: 2px solid rgb(64, 71, 88);\n"
                                        "}\n"
                                        "QPlainTextEdit:focus {\n"
                                        "	border: 2px solid rgb(91, 101, 124);\n"
                                        "}")
        self.btn_play_input = QPushButton(self.centralwidget)
        self.btn_play_input.setObjectName(u"btn_play_input")
        self.btn_play_input.setGeometry(QRect(450, 20, 61, 61))
        self.btn_play_input.setStyleSheet(u"QPushButton {\n"
                                          "	border: 2px solid rgb(52, 59, 72);\n"
                                          "	border-radius: 30px;	\n"
                                          "	background-color: rgb(52, 59, 72);\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "	background-color: rgb(57, 65, 80);\n"
                                          "	border: 2px solid rgb(61, 70, 86);\n"
                                          "}\n"
                                          "QPushButton:pressed {	\n"
                                          "	background-color: rgb(0, 120, 215);\n"
                                          "	border: 2px solid rgb(43, 50, 61);\n"
                                          "}")
        self.btn_play_input.setIcon(icon)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(60, 370, 431, 271))
        self.frame.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
                                 "border-radius: 12px;\n"
                                 "")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget = QWidget(self.frame)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 10, 280, 251))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.rd_model4_2 = QRadioButton(self.verticalLayoutWidget)
        self.rd_model4_2.setObjectName(u"rd_model4_2")
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush6 = QBrush(QColor(41, 45, 56, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush6)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
# endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush6)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
# endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush6)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
# endif
        self.rd_model4_2.setPalette(palette3)
        self.rd_model4_2.setStyleSheet(u"QRadioButton::indicator {\n"
                                       "	border: 3px solid rgb(52, 59, 72);\n"
                                       "	width: 15px;\n"
                                       "	height: 15px;\n"
                                       "	border-radius: 10px;\n"
                                       "	background: rgb(44, 49, 60);\n"
                                       "}\n"
                                       "QRadioButton::indicator:hover {\n"
                                       "	border: 3px solid rgb(58, 66, 81);\n"
                                       "}\n"
                                       "\n"
                                       "QRadioButton::indicator:checked {\n"
                                       "	background: 3px solid rgb(39, 104, 156);\n"
                                       "	border: 3px solid rgb(52, 59, 72);\n"
                                       "}")

        self.verticalLayout.addWidget(self.rd_model4_2)

        self.rd_bestmodel = QRadioButton(self.verticalLayoutWidget)
        self.rd_bestmodel.setObjectName(u"rd_bestmodel")
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush6)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
# endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush6)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
# endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush6)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
# endif
        self.rd_bestmodel.setPalette(palette4)
        self.rd_bestmodel.setStyleSheet(u"QRadioButton::indicator {\n"
                                        "	border: 3px solid rgb(52, 59, 72);\n"
                                        "	width: 15px;\n"
                                        "	height: 15px;\n"
                                        "	border-radius: 10px;\n"
                                        "	background: rgb(44, 49, 60);\n"
                                        "}\n"
                                        "QRadioButton::indicator:hover {\n"
                                        "	border: 3px solid rgb(58, 66, 81);\n"
                                        "}\n"
                                        "\n"
                                        "QRadioButton::indicator:checked {\n"
                                        "	background: 3px solid rgb(39, 104, 156);\n"
                                        "	border: 3px solid rgb(52, 59, 72);\n"
                                        "}")

        self.verticalLayout.addWidget(self.rd_bestmodel)

        self.rd_deepspeach = QRadioButton(self.verticalLayoutWidget)
        self.rd_deepspeach.setObjectName(u"rd_deepspeach")
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush6)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
# endif
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush6)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
# endif
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush6)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
# endif
        self.rd_deepspeach.setPalette(palette5)
# if QT_CONFIG(statustip)
        self.rd_deepspeach.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
# if QT_CONFIG(whatsthis)
        self.rd_deepspeach.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
        self.rd_deepspeach.setStyleSheet(u"QRadioButton::indicator {\n"
                                         "	border: 3px solid rgb(52, 59, 72);\n"
                                         "	width: 15px;\n"
                                         "	height: 15px;\n"
                                         "	border-radius: 10px;\n"
                                         "	background: rgb(44, 49, 60);\n"
                                         "}\n"
                                         "QRadioButton::indicator:hover {\n"
                                         "	border: 3px solid rgb(58, 66, 81);\n"
                                         "}\n"
                                         "\n"
                                         "QRadioButton::indicator:checked {\n"
                                         "	background: 3px solid rgb(39, 104, 156);\n"
                                         "	border: 3px solid rgb(52, 59, 72);\n"
                                         "}")

        self.verticalLayout.addWidget(self.rd_deepspeach)

        self.rd_model5 = QRadioButton(self.verticalLayoutWidget)
        self.rd_model5.setObjectName(u"rd_model5")
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush6)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
# endif
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush6)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
# endif
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush6)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
# endif
        self.rd_model5.setPalette(palette6)
        self.rd_model5.setStyleSheet(u"QRadioButton::indicator {\n"
                                     "	border: 3px solid rgb(52, 59, 72);\n"
                                     "	width: 15px;\n"
                                     "	height: 15px;\n"
                                     "	border-radius: 10px;\n"
                                     "	background: rgb(44, 49, 60);\n"
                                     "}\n"
                                     "QRadioButton::indicator:hover {\n"
                                     "	border: 3px solid rgb(58, 66, 81);\n"
                                     "}\n"
                                     "\n"
                                     "QRadioButton::indicator:checked {\n"
                                     "	background: 3px solid rgb(39, 104, 156);\n"
                                     "	border: 3px solid rgb(52, 59, 72);\n"
                                     "}")

        self.verticalLayout.addWidget(self.rd_model5)

        self.rd_model4 = QRadioButton(self.verticalLayoutWidget)
        self.rd_model4.setObjectName(u"rd_model4")
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush6)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
# endif
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush6)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
# endif
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush6)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
# endif
        self.rd_model4.setPalette(palette7)
        self.rd_model4.setStyleSheet(u"QRadioButton::indicator {\n"
                                     "	border: 3px solid rgb(52, 59, 72);\n"
                                     "	width: 15px;\n"
                                     "	height: 15px;\n"
                                     "	border-radius: 10px;\n"
                                     "	background: rgb(44, 49, 60);\n"
                                     "}\n"
                                     "QRadioButton::indicator:hover {\n"
                                     "	border: 3px solid rgb(58, 66, 81);\n"
                                     "}\n"
                                     "\n"
                                     "QRadioButton::indicator:checked {\n"
                                     "	background: 3px solid rgb(39, 104, 156);\n"
                                     "	border: 3px solid rgb(52, 59, 72);\n"
                                     "}")

        self.verticalLayout.addWidget(self.rd_model4)

        self.rd_model3 = QRadioButton(self.verticalLayoutWidget)
        self.rd_model3.setObjectName(u"rd_model3")
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette8.setBrush(QPalette.Active, QPalette.Text, brush)
        palette8.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush6)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
# endif
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette8.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush6)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
# endif
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette8.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette8.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush6)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
# endif
        self.rd_model3.setPalette(palette8)
        self.rd_model3.setStyleSheet(u"QRadioButton::indicator {\n"
                                     "	border: 3px solid rgb(52, 59, 72);\n"
                                     "	width: 15px;\n"
                                     "	height: 15px;\n"
                                     "	border-radius: 10px;\n"
                                     "	background: rgb(44, 49, 60);\n"
                                     "}\n"
                                     "QRadioButton::indicator:hover {\n"
                                     "	border: 3px solid rgb(58, 66, 81);\n"
                                     "}\n"
                                     "\n"
                                     "QRadioButton::indicator:checked {\n"
                                     "	background: 3px solid rgb(39, 104, 156);\n"
                                     "	border: 3px solid rgb(52, 59, 72);\n"
                                     "}")

        self.verticalLayout.addWidget(self.rd_model3)

        self.rd_model2 = QRadioButton(self.verticalLayoutWidget)
        self.rd_model2.setObjectName(u"rd_model2")
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette9.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette9.setBrush(QPalette.Active, QPalette.Text, brush)
        palette9.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette9.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette9.setBrush(QPalette.Active, QPalette.Window, brush6)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
# endif
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette9.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette9.setBrush(QPalette.Inactive, QPalette.Window, brush6)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
# endif
        palette9.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette9.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette9.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette9.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette9.setBrush(QPalette.Disabled, QPalette.Window, brush6)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
# endif
        self.rd_model2.setPalette(palette9)
        self.rd_model2.setStyleSheet(u"QRadioButton::indicator {\n"
                                     "	border: 3px solid rgb(52, 59, 72);\n"
                                     "	width: 15px;\n"
                                     "	height: 15px;\n"
                                     "	border-radius: 10px;\n"
                                     "	background: rgb(44, 49, 60);\n"
                                     "}\n"
                                     "QRadioButton::indicator:hover {\n"
                                     "	border: 3px solid rgb(58, 66, 81);\n"
                                     "}\n"
                                     "\n"
                                     "QRadioButton::indicator:checked {\n"
                                     "	background: 3px solid rgb(39, 104, 156);\n"
                                     "	border: 3px solid rgb(52, 59, 72);\n"
                                     "}")

        self.verticalLayout.addWidget(self.rd_model2)

        self.rd_model1 = QRadioButton(self.verticalLayoutWidget)
        self.rd_model1.setObjectName(u"rd_model1")
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette10.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette10.setBrush(QPalette.Active, QPalette.Text, brush)
        palette10.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette10.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette10.setBrush(QPalette.Active, QPalette.Window, brush6)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
# endif
        palette10.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette10.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette10.setBrush(QPalette.Inactive, QPalette.Window, brush6)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
# endif
        palette10.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette10.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette10.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette10.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette10.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette10.setBrush(QPalette.Disabled, QPalette.Window, brush6)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
# endif
        self.rd_model1.setPalette(palette10)
        self.rd_model1.setStyleSheet(u"QRadioButton::indicator {\n"
                                     "	border: 3px solid rgb(52, 59, 72);\n"
                                     "	width: 15px;\n"
                                     "	height: 15px;\n"
                                     "	border-radius: 10px;\n"
                                     "	background: rgb(44, 49, 60);\n"
                                     "}\n"
                                     "QRadioButton::indicator:hover {\n"
                                     "	border: 3px solid rgb(58, 66, 81);\n"
                                     "}\n"
                                     "\n"
                                     "QRadioButton::indicator:checked {\n"
                                     "	background: 3px solid rgb(39, 104, 156);\n"
                                     "	border: 3px solid rgb(52, 59, 72);\n"
                                     "}")

        self.verticalLayout.addWidget(self.rd_model1)

        self.rd_model0 = QRadioButton(self.verticalLayoutWidget)
        self.rd_model0.setObjectName(u"rd_model0")
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette11.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette11.setBrush(QPalette.Active, QPalette.Text, brush)
        palette11.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette11.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette11.setBrush(QPalette.Active, QPalette.Window, brush6)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
# endif
        palette11.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette11.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette11.setBrush(QPalette.Inactive, QPalette.Window, brush6)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
# endif
        palette11.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette11.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette11.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette11.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette11.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette11.setBrush(QPalette.Disabled, QPalette.Window, brush6)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
# endif
        self.rd_model0.setPalette(palette11)
        self.rd_model0.setStyleSheet(u"QRadioButton::indicator {\n"
                                     "	border: 3px solid rgb(52, 59, 72);\n"
                                     "	width: 15px;\n"
                                     "	height: 15px;\n"
                                     "	border-radius: 10px;\n"
                                     "	background: rgb(44, 49, 60);\n"
                                     "}\n"
                                     "QRadioButton::indicator:hover {\n"
                                     "	border: 3px solid rgb(58, 66, 81);\n"
                                     "}\n"
                                     "\n"
                                     "QRadioButton::indicator:checked {\n"
                                     "	background: 3px solid rgb(39, 104, 156);\n"
                                     "	border: 3px solid rgb(52, 59, 72);\n"
                                     "}")

        self.verticalLayout.addWidget(self.rd_model0)

        # self.btn_apply = QPushButton(self.frame)
        # self.btn_apply.setObjectName(u"btn_apply")
        # self.btn_apply.setGeometry(QRect(260, 210, 141, 41))
        # self.btn_apply.setMinimumSize(QSize(11, 11))
        palette12 = QPalette()
        palette12.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette12.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette12.setBrush(QPalette.Active, QPalette.Text, brush)
        palette12.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette12.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette12.setBrush(QPalette.Active, QPalette.Window, brush1)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
# endif
        palette12.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette12.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette12.setBrush(QPalette.Inactive, QPalette.Window, brush1)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
# endif
        palette12.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette12.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette12.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette12.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette12.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette12.setBrush(QPalette.Disabled, QPalette.Window, brush1)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
# endif
#         self.btn_apply.setPalette(palette12)
#         self.btn_apply.setFont(font)
#         self.btn_apply.setStyleSheet(u"QPushButton {\n"
# "	border: 2px solid rgb(52, 59, 72);\n"
# "	border-radius: 10px;	\n"
# "	background-color: rgb(52, 59, 72);\n"
# "}\n"
# "QPushButton:hover {\n"
# "	background-color: rgb(57, 65, 80);\n"
# "	border: 2px solid rgb(61, 70, 86);\n"
# "}\n"
# "QPushButton:pressed {	\n"
# "	background-color: rgb(35, 40, 49);\n"
# "	border: 2px solid rgb(43, 50, 61);\n"
# "}")
#         self.btn_apply.setIcon(icon1)
        self.comboBox = QComboBox(self.frame)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(260, 60, 141, 41))
        palette13 = QPalette()
        palette13.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette13.setBrush(QPalette.Active, QPalette.Text, brush)
        palette13.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette13.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette13.setBrush(QPalette.Active, QPalette.Window, brush1)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
# endif
        palette13.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette13.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette13.setBrush(QPalette.Inactive, QPalette.Window, brush1)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
# endif
        palette13.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette13.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette13.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette13.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette13.setBrush(QPalette.Disabled, QPalette.Window, brush1)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
# endif
        self.comboBox.setPalette(palette13)
        self.comboBox.setFont(font)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(u"QComboBox{\n"
                                    "	background-color:  rgb(52, 59, 72);\n"
                                    "	border-radius: 5px;\n"
                                    "	border: 2px solid  rgb(52, 59, 72);\n"
                                    "	padding: 5px;\n"
                                    "	padding-left: 10px;\n"
                                    "}\n"
                                    "QComboBox:hover{\n"
                                    "	border: 2px solid rgb(64, 71, 88);\n"
                                    "}\n"
                                    "QComboBox::drop-down {\n"
                                    "	subcontrol-origin: padding;\n"
                                    "	subcontrol-position: top right;\n"
                                    "	width: 25px;\n"
                                    "	border-left-width: 3px;\n"
                                    "	border-left-color: rgba(39, 44, 54, 150);\n"
                                    "	border-left-style: solid;\n"
                                    "	border-top-right-radius: 3px;\n"
                                    "	border-bottom-right-radius: 3px;\n"
                                    "	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
                                    "	background-position: center;\n"
                                    "	background-repeat: no-reperat;\n"
                                    "}\n"
                                    "QComboBox QAbstractItemView {\n"
                                    "	color: rgb(85, 170, 255);	\n"
                                    "	background-color:  rgb(52, 59, 72);\n"
                                    "	padding: 10px;\n"
                                    "	selection-background-color: rgb(39, 44, 54);\n"
                                    "}")
        self.comboBox.setIconSize(QSize(16, 16))
        self.comboBox.setFrame(True)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(260, 35, 170, 20))
        palette14 = QPalette()
        brush7 = QBrush(QColor(85, 170, 255, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette14.setBrush(QPalette.Active, QPalette.WindowText, brush7)
        palette14.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette14.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette14.setBrush(QPalette.Active, QPalette.Window, brush6)
        palette14.setBrush(QPalette.Inactive, QPalette.WindowText, brush7)
        palette14.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette14.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette14.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        palette14.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette14.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette14.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette14.setBrush(QPalette.Disabled, QPalette.Window, brush6)
        self.label.setPalette(palette14)
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"")

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(520, 370, 421, 271))
        self.frame_2.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
                                   "border-radius: 12px;\n"
                                   "")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.btn_record = QPushButton(self.frame_2)
        self.btn_record.setObjectName(u"btn_record")
        self.btn_record.setGeometry(QRect(160, 40, 121, 121))
        self.btn_record.setStyleSheet(u"QPushButton {\n"
                                      "	border: 2px solid rgb(52, 59, 72);\n"
                                      "	border-radius: 60px;	\n"
                                      "	background-color: rgb(52, 59, 72);\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "	background-color: rgb(57, 65, 80);\n"
                                      "	border: 2px solid rgb(61, 70, 86);\n"
                                      "}\n"
                                      "QPushButton:pressed {	\n"
                                      "	background-color: rgb(139,0,0);\n"
                                      "	border: 2px solid rgb(43, 50, 61);\n"
                                      "}")
        icon2 = QIcon()
        icon2.addFile(u"cil-microphone.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_record.setIcon(icon2)
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(60, 20, 431, 331))
        self.frame_3.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
                                   "border-radius: 12px;\n"
                                   "")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.Ptext_input = QPlainTextEdit(self.frame_3)
        self.Ptext_input.setObjectName(u"Ptext_input")
        self.Ptext_input.setGeometry(QRect(10, 30, 411, 291))
        self.Ptext_input.setMinimumSize(QSize(200, 200))
        palette15 = QPalette()
        palette15.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette15.setBrush(QPalette.Active, QPalette.Text, brush)
        palette15.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette15.setBrush(QPalette.Active, QPalette.Window, brush5)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
# endif
        palette15.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette15.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette15.setBrush(QPalette.Inactive, QPalette.Window, brush5)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
# endif
        palette15.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette15.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette15.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette15.setBrush(QPalette.Disabled, QPalette.Window, brush5)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
# endif
        self.Ptext_input.setPalette(palette15)
        self.Ptext_input.setFont(font1)
        self.Ptext_input.setStyleSheet(u"QPlainTextEdit {\n"
                                       "	background-color: rgb(27, 29, 35);\n"
                                       "	border-radius: 5px;\n"
                                       "	padding: 10px;\n"
                                       "}\n"
                                       "QPlainTextEdit:hover {\n"
                                       "	border: 2px solid rgb(64, 71, 88);\n"
                                       "}\n"
                                       "QPlainTextEdit:focus {\n"
                                       "	border: 2px solid rgb(91, 101, 124);\n"
                                       "}")
        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(520, 20, 431, 331))
        self.frame_4.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
                                   "border-radius: 12px;\n"
                                   "")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 2, 2))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 0, 2, 2))
        self.gridLayout_2 = QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.layoutWidget2 = QWidget(self.centralwidget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(0, 0, 2, 2))
        self.gridLayout_3 = QGridLayout(self.layoutWidget2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.layoutWidget3 = QWidget(self.centralwidget)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(0, 0, 2, 2))
        self.formLayout = QFormLayout(self.layoutWidget3)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.layoutWidget1.raise_()
        self.layoutWidget1.raise_()
        self.layoutWidget1.raise_()
        self.layoutWidget1.raise_()
        self.frame_4.raise_()
        self.frame_3.raise_()
        self.frame_2.raise_()
        self.lineEdit_path.raise_()
        self.Ptext_output.raise_()
        self.btn_play_input.raise_()
        self.btn_play_output.raise_()
        self.frame.raise_()
        self.btn_open.raise_()
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1009, 21))
        MainWindow.setMenuBar(self.menubar)

        self.label2 = QLabel(self.frame_3)
        self.label2.setObjectName(u"label")
        self.label2.setGeometry(QRect(10, 0, 300, 23))
        self.label2.setPalette(palette14)
        self.label2.setFont(font2)
        self.label2.setStyleSheet(u"")
        self.label2.setText(QCoreApplication.translate(
            "MainWindow", u"Transcription of Spoken Language", None))
        
        self.label3 = QLabel(self.frame_4)
        self.label3.setObjectName(u"label")
        self.label3.setGeometry(QRect(10, 0, 300, 23))
        self.label3.setPalette(palette14)
        self.label3.setFont(font2)
        self.label3.setStyleSheet(u"")
        self.label3.setText(QCoreApplication.translate(
            "MainWindow", u"Translated Language", None))

        self.label4 = QLabel(self.frame_2)
        self.label4.setObjectName(u"label")
        self.label4.setGeometry(QRect(30, 180, 200, 23))
        self.label4.setPalette(palette14)
        self.label4.setFont(font2)
        self.label4.setStyleSheet(u"")
        self.label4.setText(QCoreApplication.translate(
            "MainWindow", u"Load Audio From PC", None))
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
        
    # setupUi
        ##############################
        ##############################
        ###############################
        self.btn_record.setCheckable(True)
        self.btn_record.clicked.connect(self.Record)
        self.btn_record.clicked.connect(self.changeColorRecBt)
        self.btn_play_input.setCheckable(True)
        # self.btn_play_input.clicked.connect(self.test)
        self.btn_play_input.clicked.connect(self.changeColorplyBt1)
        self.btn_play_output.setCheckable(True)
        self.btn_play_output.clicked.connect(self.changeColorplyBt2)
        self.btn_open.clicked.connect(self.BrowseAudioFile)
        # self.btn_apply.clicked.connect(self.checkConfiguration)

        ###############################
      
    def changeColorRecBt(self):

        # if button is checked
        if self.btn_record.isChecked():

            # setting background color
            self.btn_record.setStyleSheet("QPushButton {\n"
                                          "	border: 2px solid rgb(43, 50, 61);\n"
                                          "	border-radius: 60px;	\n"
                                          "	background-color: rgb(139,0,0);\n"
                                          "}\n")

        # if it is unchecked
        else:

            # set background color
            self.btn_record.setStyleSheet("QPushButton {\n"
                                          "	border: 2px solid rgb(52, 59, 72);\n"
                                          "	border-radius: 60px;	\n"
                                          "	background-color: rgb(52, 59, 72);\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "	background-color: rgb(57, 65, 80);\n"
                                          "	border: 2px solid rgb(61, 70, 86);\n"
                                          "}\n")

    def changeColorplyBt1(self):

        # if button is checked
        if self.btn_play_input.isChecked():

            # setting background color
            self.btn_play_input.setStyleSheet("QPushButton{	\n"
                                              "	background-color: rgb(0, 120, 215);\n"
                                              "	border-radius: 30px;	\n"
                                              "	border: 2px solid rgb(43, 50, 61);\n"
                                              "}")
        

        # if it is unchecked

        else:
            synthesize(transcribed, 'en')    
     
            # set background color
            self.btn_play_input.setStyleSheet("QPushButton {\n"
                                              "	border: 2px solid rgb(52, 59, 72);\n"
                                              "	border-radius: 30px;	\n"
                                              "	background-color: rgb(52, 59, 72);\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "	background-color: rgb(57, 65, 80);\n"
                                              "	border: 2px solid rgb(61, 70, 86);\n"
                                              "}\n")
                

    def changeColorplyBt2(self):

        # if button is checked
        if self.btn_play_output.isChecked():

            # setting background color
            self.btn_play_output.setStyleSheet("QPushButton{	\n"
                                               "	background-color: rgb(0, 120, 215);\n"
                                               "	border-radius: 30px;	\n"
                                               "	border: 2px solid rgb(43, 50, 61);\n"
                                               "}")

        # if it is unchecked
        else:
            synthesize(translated, destLanguage)    
            # set background color
            self.btn_play_output.setStyleSheet("QPushButton {\n"
                                               "	border: 2px solid rgb(52, 59, 72);\n"
                                               "	border-radius: 30px;	\n"
                                               "	background-color: rgb(52, 59, 72);\n"
                                               "}\n"
                                               "QPushButton:hover {\n"
                                               "	background-color: rgb(57, 65, 80);\n"
                                               "	border: 2px solid rgb(61, 70, 86);\n"
                                               "}\n")

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"Speech To Speech Translator", None))
        self.btn_play_output.setText("")
        self.btn_open.setText(QCoreApplication.translate(
            "MainWindow", u"Open ", None))
        self.lineEdit_path.setText("")
        self.lineEdit_path.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", u"Ex: E:\\Audio file\\sample.wav", None))
        self.Ptext_output.setPlainText("")
        self.btn_play_input.setText("")
        self.rd_model4_2.setText(QCoreApplication.translate(
            "MainWindow", u"IBM Watson Model [Online]", None))
# if QT_CONFIG(whatsthis)
        self.rd_bestmodel.setWhatsThis(QCoreApplication.translate(
            "MainWindow", u"FFFFFFFFFFFFFFFFFFFFFFFFFFFFF", None))
#endif // QT_CONFIG(whatsthis)
# if QT_CONFIG(accessibility)
        self.rd_bestmodel.setAccessibleName(
            QCoreApplication.translate("MainWindow", u"AAAAAAAAAAAAAAAA", None))
#endif // QT_CONFIG(accessibility)
# if QT_CONFIG(accessibility)
        self.rd_bestmodel.setAccessibleDescription(
            QCoreApplication.translate("MainWindow", u"XXXXXXXXXXXXXXXXX", None))
#endif // QT_CONFIG(accessibility)
        self.rd_bestmodel.setText(QCoreApplication.translate(
            "MainWindow", u"Model 5 [1000 Hours]", None))
# if QT_CONFIG(tooltip)
        self.rd_deepspeach.setToolTip("")
#endif // QT_CONFIG(tooltip)
# if QT_CONFIG(accessibility)
        self.rd_deepspeach.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.rd_deepspeach.setText(QCoreApplication.translate(
            "MainWindow", u"Model 5 [360 Hours]", None))
# if QT_CONFIG(tooltip)
        self.rd_model5.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.rd_model5.setText(QCoreApplication.translate(
            "MainWindow", u"Model 5 [10 Hours]", None))
# if QT_CONFIG(tooltip)
        self.rd_model4.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.rd_model4.setText(QCoreApplication.translate(
            "MainWindow", u"Model 4 BIRNN_TIMEDIST [10 Hours]", None))
# if QT_CONFIG(tooltip)
        self.rd_model3.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.rd_model3.setText(QCoreApplication.translate(
            "MainWindow", u"Model 3 DeeperRNN_TIMEDIST [10 Hours]", None))
# if QT_CONFIG(tooltip)
        self.rd_model2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.rd_model2.setText(QCoreApplication.translate(
            "MainWindow", u"Model 2 RNN_CNN_TIMEDIST [10 Hours]", None))
# if QT_CONFIG(tooltip)
        self.rd_model1.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.rd_model1.setText(QCoreApplication.translate(
            "MainWindow", u"Model 1 RNN_TIMEDIST [10 Hours]", None))  # if QT_CONFIG(tooltip)
        self.rd_model0.setToolTip("")  # endif // QT_CONFIG(tooltip)
        self.rd_model0.setText(QCoreApplication.translate(
            "MainWindow", u"Model 0 Simple RNN [10 Hours]", None))
        #self.btn_apply.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.comboBox.setItemText(0, QCoreApplication.translate(
            "MainWindow", u"\u0627\u0644\u0639\u0631\u0628\u064a\u0629", None))
        self.comboBox.setItemText(1, QCoreApplication.translate(
            "MainWindow", u"Fran\u00e7ais", None))
        self.comboBox.setItemText(
            2, QCoreApplication.translate("MainWindow", u"Deutsch", None))

        self.label.setText(QCoreApplication.translate(
            "MainWindow", u"Choose Language ", None))
        
        self.btn_record.setText("")
        self.Ptext_input.setPlainText("")


    # retranslateUi

    def clearTexts(self):
        self.lineEdit_path.setText("")
        transcribed = ""
        translated = ""
        self.Ptext_input.clear()
        self.Ptext_output.clear()

    def runLongTask(self):

        self.thread = QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.start()

    def checkConfiguration(self, path):
        global destLanguage
        # check on Language
        languageInndex = self.comboBox.currentIndex()
        
        if languageInndex == 0:
            destLanguage = "ar"

        elif languageInndex == 1:
            destLanguage = "fr"

        elif languageInndex == 2:
            destLanguage = "de"
        else:
            destLanguage = "en"

        if self.rd_model4_2.isChecked():
            return get_prediction_ibm(path)
        elif self.rd_bestmodel.isChecked():
            return Transcribe(path)
        elif self.rd_deepspeach.isChecked():
            return get_DS_prediction(path)
        elif self.rd_model5.isChecked():
            return get_predictions(path, model5, "./results/model_end.h5")
        elif self.rd_model4.isChecked():
            return get_predictions(path, model4, "./results/model_4.h5")
        elif self.rd_model3.isChecked():
            return get_predictions(path, model3, "./results/model_3.h5")
        elif self.rd_model2.isChecked():
            return get_predictions(path, model2, "./results/model_2.h5")
        elif self.rd_model1.isChecked():
            return get_predictions(path, model1, "./results/model_1.h5")
        elif self.rd_model0.isChecked():
            return get_predictions(path, model0, "./results/model_0.h5")
        else:
            return "No Model Selected"

    def Record(self):

        if self.btn_record.isChecked():
            #print("on")
            self.runLongTask()
        else:
            #print("off")
            guiAUD.stop()
            time.sleep(.1)
            global transcribed, translated
            transcribed = self.checkConfiguration("./test_recording.wav")
            translated = translate(transcribed, destLanguage,True)
            self.clearTexts()

            self.lineEdit_path.setText("./test_recording.wav")
            self.Ptext_input.insertPlainText(str(transcribed))
            self.Ptext_output.insertPlainText(translated)
            QCoreApplication.processEvents()
            self.playAudio()

    def BrowseAudioFile(self):

        fileName = QtWidgets.QFileDialog.getOpenFileName(
            None, 'Single File', '', '*.wav')
        path = fileName[0]
        if path !=  "":
                self.lineEdit_path.setText(path)
                global transcribed, translated
                transcribed = self.checkConfiguration(path)
                translated = translate(transcribed, destLanguage,True)
                self.clearTexts()
                self.Ptext_input.insertPlainText(str(transcribed))
                self.Ptext_output.insertPlainText(translated)
                QCoreApplication.processEvents()
                self.playAudio()

    def playAudio(self):
        synthesize(translated, 'ar')
     
