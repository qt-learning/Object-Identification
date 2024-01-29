# -*- coding: utf-8 -*-

import names

"""
qtwrapper_descriptor.xml modified not to use windowTitle in the real name of MainWindow objects
<descriptor>
    <type name="MainWindow"/>
    <realidentifiers>
        <property exclude="yes">windowTitle</property>
    </realidentifiers>
</descriptor>
"""

def main():
    startApplication("addressbook")
    clickButton(waitForObject(names.new_QToolButton))
    clickButton(waitForObject(names.add_QToolButton))
    type(waitForObject(names.forename_LineEdit), "Qt")
    type(waitForObject(names.forename_LineEdit), "<Tab>")
    type(waitForObject(names.surname_LineEdit), "Company")
    type(waitForObject(names.surname_LineEdit), "<Tab>")
    type(waitForObject(names.email_LineEdit), "Qt")
    type(waitForObject(names.email_LineEdit), "<Tab>")
    type(waitForObject(names.phone_LineEdit), "0000")
    type(waitForObject(names.phone_LineEdit), "<Return>")
    mouseClick(waitForObject(names.o1_HeaderViewItem), 14, 15, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.remove_QToolButton))
    clickButton(waitForObject(names.address_Book_Delete_Yes_QPushButton))
