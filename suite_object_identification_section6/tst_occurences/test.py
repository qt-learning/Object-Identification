# -*- coding: utf-8 -*-

import names


def main():
    startApplication("MyApp")
    mouseClick(waitForObject(names.my_Application_Rectangle))
    mouseClick(waitForObject(names.my_Application_Rectangle_2))
    mouseClick(waitForObject(names.my_Application_Rectangle_3))
