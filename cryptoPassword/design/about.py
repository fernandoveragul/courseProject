# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\about.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ShowAbout(object):
    def setupUi(self, ShowAbout):
        ShowAbout.setObjectName("ShowAbout")
        ShowAbout.resize(700, 667)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(ShowAbout)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(ShowAbout)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 680, 647))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.aboutWindow = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.aboutWindow.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aboutWindow.sizePolicy().hasHeightForWidth())
        self.aboutWindow.setSizePolicy(sizePolicy)
        self.aboutWindow.setAlignment(QtCore.Qt.AlignCenter)
        self.aboutWindow.setObjectName("aboutWindow")
        self.verticalLayout.addWidget(self.aboutWindow)
        self.line_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.aboutAppSecretWord = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aboutAppSecretWord.sizePolicy().hasHeightForWidth())
        self.aboutAppSecretWord.setSizePolicy(sizePolicy)
        self.aboutAppSecretWord.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.aboutAppSecretWord.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.aboutAppSecretWord.setObjectName("aboutAppSecretWord")
        self.verticalLayout.addWidget(self.aboutAppSecretWord)
        self.line_4 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        self.aboutAuthor = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.aboutAuthor.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aboutAuthor.sizePolicy().hasHeightForWidth())
        self.aboutAuthor.setSizePolicy(sizePolicy)
        self.aboutAuthor.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.aboutAuthor.setFrameShadow(QtWidgets.QFrame.Raised)
        self.aboutAuthor.setAlignment(QtCore.Qt.AlignCenter)
        self.aboutAuthor.setObjectName("aboutAuthor")
        self.verticalLayout.addWidget(self.aboutAuthor)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)

        self.retranslateUi(ShowAbout)
        QtCore.QMetaObject.connectSlotsByName(ShowAbout)

    def retranslateUi(self, ShowAbout):
        _translate = QtCore.QCoreApplication.translate
        ShowAbout.setWindowTitle(_translate("ShowAbout", "??????????????"))
        self.aboutWindow.setText(_translate("ShowAbout", "<html><head/><body><p align=\"center\">?????????? ???? ???????????? ?????????? ?????????????? ???? ???????????????????????? ????????????????????</p></body></html>"))
        self.aboutAppSecretWord.setHtml(_translate("ShowAbout", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:14pt;\">    ?????????? </span><span style=\" font-family:\'Arial\'; font-size:14pt; text-decoration: underline;\">????????????????????????</span><span style=\" font-family:\'Arial\'; font-size:14pt;\">??????????????, ???????????????????? ???????????? ?????????????????? ?????????? ?? ???????????? ???????????? (?????????? ?????? ?????????????????? ?????????? ?????????????????????????????? ?????????????? ????????????????????). ?????????? ???????????? ?????????????????????????????? ???????????? ???? ???????????? ????????????, ???????????? ?????????????? ?????????? ???????????? ???????????????????????????? ?? ???????????? ???? ???????????? ??????????????????????????.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:14pt;\">??</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:14pt;\">    ?????????? </span><span style=\" font-family:\'Arial\'; font-size:14pt; text-decoration: underline;\">????????????????????????</span><span style=\" font-family:\'Arial\'; font-size:14pt;\">??????????????, ???????????????????? ???????????? ?????????????????? ?????????? ?? ???????????? ???????????? (?????????? ?????? ?????????????????? ?????????? ?????????????????????????????? ?????????????? ????????????????????). ?????????? ???????????? ?????????????????????????? ???????????? ???? ???????????? ????????????, ???????????????????? ?????????????? ?????????? ???????????? ???????????????????????????? ?? ???????????? ???? ???????????? ??????????????????????????.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:14pt;\">??</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:14pt;\">    ???????????????????? ????????????????????: ???????????? ???????????????????? ?????????????????????????? ?????? ?????????????????????? ?? ?????????????????????????? ???????????????????? ???? ???????????????????? ??????????, ?????????????? ?????????????????????? ???????????????? ?????????????????? ????????.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:14pt;\">??</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:14pt;\">    ???????????????????? ???? ???????? ???????????? ???????????? ?????????????????? ?????????????????? ??????????, ???? ?????????????? ?????????????????????????? ?????????????????? ??????????????????????:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:14pt;\">    1.???????????????????????? ?????????????????????????? ?????????????????? ???????????????? ?????????????????? ?????? ????????????????.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:14pt;\">    2.???????????????????????? ?????????????????????????? ???????????????? ???????????????? ?????????????????? ?????? ????????????????.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:14pt;\">    3.?????????????????????????? ?????????? ???????????????????? ?????????? ???? 8 ???? 32 ????????????????.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:14pt;\">    4.???????????????????????????? ?????????????????????? ???????????????? ?????? ???????????????? ???????? ???? ???????????????????? ????????????????????????.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:14pt;\">??</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:14pt; text-decoration: underline;\">????????????: ??????????????????????????????????, MySecretWord</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:14pt;\">??</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:14pt;\">    ???????????????????? ?????????????????? ???? ???????? ???????????? ???????????? ????????????, ?????????????? ???????????????????????? ???????? ??????????????????: ?? ?????????????????????????? ???????? ?? ?? ?????????????????????????????? ????????. ?????????? ???????????? ???????????? ?????????????????????? ?????????????????? ????????????????????????:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:14pt;\">    1.???????????????????????? ???????????????????? ???????????????? ????????.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:14pt;\">    2.???????????????????????? ???????????????????? ?????????????????????? ????????????????</span><span style=\" font-family:\'Arial\'; font-size:14pt; font-style:italic;\">??&lt;</span><span style=\" font-family:\'Arial\'; font-size:14pt;\">&quot;!</span><span style=\" font-family:\'Arial\'; font-size:14pt; color:#000000;\">@#$%^&amp;*_-: ;\'????()&gt;.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:14pt;\">    3.???????????????????????? ?????????????????????????? ?????????????????? ???????????????? ?????????????????? ?????? ????????????????.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:14pt;\">    4.???????????????????????? ?????????????????????????? ???????????????? ???????????????? ?????????????????? ?????? ????????????????.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:14pt;\">    5.?????????????????????????? ?????????? ???????????????????? ?????????? ???? 12 ???? 32 ????????????????.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:14pt;\">??</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:14pt; text-decoration: underline;\">????????????: ??????!????????????123, My!password123</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:10pt;\">?????????? ???????????????????? ???? ?????????? ?????????????????????????????? ???? ?????????????????????? ???????????? ?????? ???????????????????? ?????????? ????????????????????????.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:10pt;\">???????????????? ?????????????????? - ???????? ?????? ?????????? ??????????????????!</span></p></body></html>"))
        self.aboutAuthor.setText(_translate("ShowAbout", "<html><head/><body><p align=\"center\">@ Copyright (???????????? ???????????????????? ???????? ?????????????? ?????????????????? 4 ?????????? ?????????? ???? &quot;??????&quot; ???? ?????????????????????????? ?????? 2022)</p></body></html>"))
