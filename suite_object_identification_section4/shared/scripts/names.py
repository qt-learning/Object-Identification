# encoding: UTF-8

from objectmaphelper import *

address_Book_MainWindow = {"type": "MainWindow", "unnamed": 1, "visible": 1, "windowTitle": Wildcard("Address Book*")}
address_Book_New_QToolButton = {"text": "New", "type": "QToolButton", "unnamed": 1, "visible": 1, "window": address_Book_MainWindow}
#Duplicate
address_Book_Unnamed_MainWindow = {"type": "MainWindow", "unnamed": 1, "visible": 1, "windowTitle": "Address Book - Unnamed"}

#Should not use the duplicate of MainWindow
address_Book_Unnamed_Add_QToolButton = {"text": "Add", "type": "QToolButton", "unnamed": 1, "visible": 1, "window": address_Book_Unnamed_MainWindow}
address_Book_Add_QToolButton = {"text": "Add", "type": "QToolButton", "unnamed": 1, "visible": 1, "window": address_Book_MainWindow}

address_Book_Add_Dialog = {"type": "Dialog", "unnamed": 1, "visible": 1, "windowTitle": "Address Book - Add"}
address_Book_Add_Forename_QLabel = {"text": "Forename:", "type": "QLabel", "unnamed": 1, "visible": 1, "window": address_Book_Add_Dialog}
forename_LineEdit = {"buddy": address_Book_Add_Forename_QLabel, "type": "LineEdit", "unnamed": 1, "visible": 1}
address_Book_Add_Surname_QLabel = {"text": "Surname:", "type": "QLabel", "unnamed": 1, "visible": 1, "window": address_Book_Add_Dialog}
surname_LineEdit = {"buddy": address_Book_Add_Surname_QLabel, "type": "LineEdit", "unnamed": 1, "visible": 1}
address_Book_Add_Email_QLabel = {"text": "Email:", "type": "QLabel", "unnamed": 1, "visible": 1, "window": address_Book_Add_Dialog}
email_LineEdit = {"buddy": address_Book_Add_Email_QLabel, "type": "LineEdit", "unnamed": 1, "visible": 1}
address_Book_Add_Phone_QLabel = {"text": "Phone:", "type": "QLabel", "unnamed": 1, "visible": 1, "window": address_Book_Add_Dialog}
phone_LineEdit = {"buddy": address_Book_Add_Phone_QLabel, "type": "LineEdit", "unnamed": 1, "visible": 1}

#Should not use the duplicate of MainWindow
#address_Book_Unnamed_File_QToolBar = {"type": "QToolBar", "unnamed": 1, "visible": 1, "window": address_Book_Unnamed_MainWindow, "windowTitle": "File"}
address_Book_File_QToolBar = {"type": "QToolBar", "unnamed": 1, "visible": 1, "window": address_Book_MainWindow, "windowTitle": "File"}

#Should not use the duplicate of MainWindow
#address_Book_Unnamed_File_QTableWidget = {"aboveWidget": address_Book_Unnamed_File_QToolBar, "type": "QTableWidget", "unnamed": 1, "visible": 1, "window": address_Book_Unnamed_MainWindow}
address_Book_File_QTableWidget = {"aboveWidget": address_Book_File_QToolBar, "type": "QTableWidget", "unnamed": 1, "visible": 1, "window": address_Book_MainWindow}

#Should not use the duplicate of address_Book_File_QTableWidget
#file_QHeaderView = {"container": address_Book_Unnamed_File_QTableWidget, "orientation": 2, "type": "QHeaderView", "unnamed": 1, "visible": 1}
file_QHeaderView = {"container": address_Book_File_QTableWidget, "orientation": 2, "type": "QHeaderView", "unnamed": 1, "visible": 1}
o1_HeaderViewItem = {"container": file_QHeaderView, "text": 1, "type": "HeaderViewItem", "visible": True}

#Should not use the duplicate of MainWindow
address_Book_Unnamed_Remove_QToolButton = {"text": "Remove", "type": "QToolButton", "unnamed": 1, "visible": 1, "window": address_Book_Unnamed_MainWindow}
address_Book_Remove_QToolButton = {"text": "Remove", "type": "QToolButton", "unnamed": 1, "visible": 1, "window": address_Book_MainWindow}

address_Book_Delete_QMessageBox = {"type": "QMessageBox", "unnamed": 1, "visible": 1, "windowTitle": "Address Book - Delete"}
address_Book_Delete_Yes_QPushButton = {"text": "Yes", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": address_Book_Delete_QMessageBox}
address_Book_Add_Cancel_QPushButton = {"text": "Cancel", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": address_Book_Add_Dialog}
