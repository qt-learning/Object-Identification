# -*- coding: utf-8 -*-

import names


def main():
    startApplication("MyApp")
    mouseClick(waitForObject(names.my_Application_Rectangle), 46, 55, Qt.LeftButton)
    mouseClick(waitForObject(names.my_Application_Rectangle_2), 58, 71, Qt.LeftButton)
    mouseClick(waitForObject(names.my_Application_Rectangle_3), 42, 71, Qt.LeftButton)
