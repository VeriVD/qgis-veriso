# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'base/settings/Ui_options.ui'
#
# Created: Sun Apr  5 12:29:22 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Options(object):
    def setupUi(self, Options):
        Options.setObjectName(_fromUtf8("Options"))
        Options.resize(539, 387)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Options.sizePolicy().hasHeightForWidth())
        Options.setSizePolicy(sizePolicy)
        self.gridLayout = QtGui.QGridLayout(Options)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.buttonBox = QtGui.QDialogButtonBox(Options)
        self.buttonBox.setEnabled(True)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 1)
        self.tabWidget = QtGui.QTabWidget(Options)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideLeft)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabGeneral = QtGui.QWidget()
        self.tabGeneral.setEnabled(True)
        self.tabGeneral.setObjectName(_fromUtf8("tabGeneral"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tabGeneral)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(self.tabGeneral)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_12 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_12.setObjectName(_fromUtf8("gridLayout_12"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.lineEditProjectsDatabase = QtGui.QLineEdit(self.groupBox)
        self.lineEditProjectsDatabase.setObjectName(_fromUtf8("lineEditProjectsDatabase"))
        self.gridLayout_3.addWidget(self.lineEditProjectsDatabase, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.btnBrowseProjectsDatabase = QtGui.QPushButton(self.groupBox)
        self.btnBrowseProjectsDatabase.setObjectName(_fromUtf8("btnBrowseProjectsDatabase"))
        self.gridLayout_3.addWidget(self.btnBrowseProjectsDatabase, 0, 2, 1, 1)
        self.btnBrowseProjectsRootDir = QtGui.QPushButton(self.groupBox)
        self.btnBrowseProjectsRootDir.setObjectName(_fromUtf8("btnBrowseProjectsRootDir"))
        self.gridLayout_3.addWidget(self.btnBrowseProjectsRootDir, 1, 2, 1, 1)
        self.lineEditProjectsRootDir = QtGui.QLineEdit(self.groupBox)
        self.lineEditProjectsRootDir.setObjectName(_fromUtf8("lineEditProjectsRootDir"))
        self.gridLayout_3.addWidget(self.lineEditProjectsRootDir, 1, 1, 1, 1)
        self.label_11 = QtGui.QLabel(self.groupBox)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_3.addWidget(self.label_11, 1, 0, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabGeneral, _fromUtf8(""))
        self.tabImport = QtGui.QWidget()
        self.tabImport.setObjectName(_fromUtf8("tabImport"))
        self.gridLayout_7 = QtGui.QGridLayout(self.tabImport)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.groupBox_3 = QtGui.QGroupBox(self.tabImport)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_8 = QtGui.QLabel(self.groupBox_3)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout.addWidget(self.label_8)
        self.lineEditImportJar = QtGui.QLineEdit(self.groupBox_3)
        self.lineEditImportJar.setObjectName(_fromUtf8("lineEditImportJar"))
        self.horizontalLayout.addWidget(self.lineEditImportJar)
        self.btnBrowseImportJar = QtGui.QPushButton(self.groupBox_3)
        self.btnBrowseImportJar.setObjectName(_fromUtf8("btnBrowseImportJar"))
        self.horizontalLayout.addWidget(self.btnBrowseImportJar)
        self.gridLayout_4.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_3, 1, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.tabImport)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_8 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.plainTextEditImportVMArguments = QtGui.QPlainTextEdit(self.groupBox_2)
        self.plainTextEditImportVMArguments.setPlainText(_fromUtf8(""))
        self.plainTextEditImportVMArguments.setObjectName(_fromUtf8("plainTextEditImportVMArguments"))
        self.gridLayout_8.addWidget(self.plainTextEditImportVMArguments, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_2, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tabImport, _fromUtf8(""))
        self.tabDatabase = QtGui.QWidget()
        self.tabDatabase.setObjectName(_fromUtf8("tabDatabase"))
        self.gridLayout_6 = QtGui.QGridLayout(self.tabDatabase)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.groupBox_5 = QtGui.QGroupBox(self.tabDatabase)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.gridLayout_11 = QtGui.QGridLayout(self.groupBox_5)
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
        self.gridLayout_10 = QtGui.QGridLayout()
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.lblDbAdminPwd = QtGui.QLabel(self.groupBox_5)
        self.lblDbAdminPwd.setObjectName(_fromUtf8("lblDbAdminPwd"))
        self.gridLayout_10.addWidget(self.lblDbAdminPwd, 6, 0, 1, 1)
        self.lineEditDbUserPwd = QtGui.QLineEdit(self.groupBox_5)
        self.lineEditDbUserPwd.setEchoMode(QtGui.QLineEdit.PasswordEchoOnEdit)
        self.lineEditDbUserPwd.setObjectName(_fromUtf8("lineEditDbUserPwd"))
        self.gridLayout_10.addWidget(self.lineEditDbUserPwd, 4, 1, 1, 1)
        self.lineEditDbPort = QtGui.QLineEdit(self.groupBox_5)
        self.lineEditDbPort.setObjectName(_fromUtf8("lineEditDbPort"))
        self.gridLayout_10.addWidget(self.lineEditDbPort, 2, 1, 1, 1)
        self.lblDbAdmin = QtGui.QLabel(self.groupBox_5)
        self.lblDbAdmin.setObjectName(_fromUtf8("lblDbAdmin"))
        self.gridLayout_10.addWidget(self.lblDbAdmin, 5, 0, 1, 1)
        self.lineEditDbAdminPwd = QtGui.QLineEdit(self.groupBox_5)
        self.lineEditDbAdminPwd.setEchoMode(QtGui.QLineEdit.PasswordEchoOnEdit)
        self.lineEditDbAdminPwd.setObjectName(_fromUtf8("lineEditDbAdminPwd"))
        self.gridLayout_10.addWidget(self.lineEditDbAdminPwd, 6, 1, 1, 1)
        self.lblDbPort = QtGui.QLabel(self.groupBox_5)
        self.lblDbPort.setObjectName(_fromUtf8("lblDbPort"))
        self.gridLayout_10.addWidget(self.lblDbPort, 2, 0, 1, 1)
        self.lineEditDbHost = QtGui.QLineEdit(self.groupBox_5)
        self.lineEditDbHost.setObjectName(_fromUtf8("lineEditDbHost"))
        self.gridLayout_10.addWidget(self.lineEditDbHost, 0, 1, 1, 1)
        self.lineEditDbDatabase = QtGui.QLineEdit(self.groupBox_5)
        self.lineEditDbDatabase.setObjectName(_fromUtf8("lineEditDbDatabase"))
        self.gridLayout_10.addWidget(self.lineEditDbDatabase, 1, 1, 1, 1)
        self.lineEditDbAdmin = QtGui.QLineEdit(self.groupBox_5)
        self.lineEditDbAdmin.setObjectName(_fromUtf8("lineEditDbAdmin"))
        self.gridLayout_10.addWidget(self.lineEditDbAdmin, 5, 1, 1, 1)
        self.lblDbUserPwd = QtGui.QLabel(self.groupBox_5)
        self.lblDbUserPwd.setObjectName(_fromUtf8("lblDbUserPwd"))
        self.gridLayout_10.addWidget(self.lblDbUserPwd, 4, 0, 1, 1)
        self.lblDbDatabase = QtGui.QLabel(self.groupBox_5)
        self.lblDbDatabase.setObjectName(_fromUtf8("lblDbDatabase"))
        self.gridLayout_10.addWidget(self.lblDbDatabase, 1, 0, 1, 1)
        self.lblDbHost = QtGui.QLabel(self.groupBox_5)
        self.lblDbHost.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblDbHost.setObjectName(_fromUtf8("lblDbHost"))
        self.gridLayout_10.addWidget(self.lblDbHost, 0, 0, 1, 1)
        self.lblDbUser = QtGui.QLabel(self.groupBox_5)
        self.lblDbUser.setObjectName(_fromUtf8("lblDbUser"))
        self.gridLayout_10.addWidget(self.lblDbUser, 3, 0, 1, 1)
        self.lineEditDbUser = QtGui.QLineEdit(self.groupBox_5)
        self.lineEditDbUser.setObjectName(_fromUtf8("lineEditDbUser"))
        self.gridLayout_10.addWidget(self.lineEditDbUser, 3, 1, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_10, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox_5, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabDatabase, _fromUtf8(""))
        self.tabModelrepos = QtGui.QWidget()
        self.tabModelrepos.setObjectName(_fromUtf8("tabModelrepos"))
        self.gridLayout_14 = QtGui.QGridLayout(self.tabModelrepos)
        self.gridLayout_14.setObjectName(_fromUtf8("gridLayout_14"))
        self.groupBox_4 = QtGui.QGroupBox(self.tabModelrepos)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout_13 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_13.setObjectName(_fromUtf8("gridLayout_13"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.listWidgetModelRepos = QtGui.QListWidget(self.groupBox_4)
        self.listWidgetModelRepos.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidgetModelRepos.setObjectName(_fromUtf8("listWidgetModelRepos"))
        item = QtGui.QListWidgetItem()
        self.listWidgetModelRepos.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidgetModelRepos.addItem(item)
        self.horizontalLayout_2.addWidget(self.listWidgetModelRepos)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.btnAddModelRepo = QtGui.QPushButton(self.groupBox_4)
        self.btnAddModelRepo.setEnabled(False)
        self.btnAddModelRepo.setObjectName(_fromUtf8("btnAddModelRepo"))
        self.verticalLayout_2.addWidget(self.btnAddModelRepo)
        self.btnDeleteModelRepo = QtGui.QPushButton(self.groupBox_4)
        self.btnDeleteModelRepo.setEnabled(False)
        self.btnDeleteModelRepo.setObjectName(_fromUtf8("btnDeleteModelRepo"))
        self.verticalLayout_2.addWidget(self.btnDeleteModelRepo)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.gridLayout_13.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.gridLayout_14.addWidget(self.groupBox_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabModelrepos, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 3, 0, 1, 1)

        self.retranslateUi(Options)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Options.reject)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Options.accept)
        QtCore.QMetaObject.connectSlotsByName(Options)

    def retranslateUi(self, Options):
        Options.setWindowTitle(_translate("Options", " Options", None))
        self.groupBox.setTitle(_translate("Options", "General options ", None))
        self.label.setText(_translate("Options", "Projects management: ", None))
        self.btnBrowseProjectsDatabase.setText(_translate("Options", "Browse", None))
        self.btnBrowseProjectsRootDir.setText(_translate("Options", "Browse", None))
        self.label_11.setText(_translate("Options", "Projects root directory: ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGeneral), _translate("Options", "General", None))
        self.groupBox_3.setTitle(_translate("Options", "Import application", None))
        self.label_8.setText(_translate("Options", "Jar file: ", None))
        self.btnBrowseImportJar.setText(_translate("Options", "Browse", None))
        self.groupBox_2.setTitle(_translate("Options", "VM arguments", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabImport), _translate("Options", "Import", None))
        self.groupBox_5.setTitle(_translate("Options", "Import database", None))
        self.lblDbAdminPwd.setText(_translate("Options", "Admin password", None))
        self.lblDbAdmin.setText(_translate("Options", "Admin", None))
        self.lblDbPort.setText(_translate("Options", "Port", None))
        self.lblDbUserPwd.setText(_translate("Options", "Password", None))
        self.lblDbDatabase.setText(_translate("Options", "Database", None))
        self.lblDbHost.setText(_translate("Options", "Host ", None))
        self.lblDbUser.setText(_translate("Options", "Username", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabDatabase), _translate("Options", "Database", None))
        self.groupBox_4.setTitle(_translate("Options", "Model repositories ", None))
        __sortingEnabled = self.listWidgetModelRepos.isSortingEnabled()
        self.listWidgetModelRepos.setSortingEnabled(False)
        item = self.listWidgetModelRepos.item(0)
        item.setText(_translate("Options", "http://www.catais.org/models/", None))
        item = self.listWidgetModelRepos.item(1)
        item.setText(_translate("Options", "http://models.geo.admin.ch/", None))
        self.listWidgetModelRepos.setSortingEnabled(__sortingEnabled)
        self.btnAddModelRepo.setText(_translate("Options", "Add", None))
        self.btnDeleteModelRepo.setText(_translate("Options", "Delete", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabModelrepos), _translate("Options", "Model repositories", None))

