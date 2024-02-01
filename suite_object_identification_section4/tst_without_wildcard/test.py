# -*- coding: utf-8 -*-

import names


def main():
    startApplication("addressbook")
    clickButton(waitForObject(names.address_Book_New_QToolButton))
    clickButton(waitForObject(names.address_Book_Unnamed_Add_QToolButton))
    type(waitForObject(names.forename_LineEdit), "Qt")
    type(waitForObject(names.forename_LineEdit), "<Tab>")
    type(waitForObject(names.surname_LineEdit), "Company")
    type(waitForObject(names.surname_LineEdit), "<Tab>")
    type(waitForObject(names.email_LineEdit), "Qt")
    type(waitForObject(names.email_LineEdit), "<Tab>")
    type(waitForObject(names.phone_LineEdit), "0000")
    type(waitForObject(names.phone_LineEdit), "<Return>")
    mouseClick(waitForObject(names.o1_HeaderViewItem))
    clickButton(waitForObject(names.address_Book_Unnamed_Remove_QToolButton))
    clickButton(waitForObject(names.address_Book_Delete_Yes_QPushButton))
