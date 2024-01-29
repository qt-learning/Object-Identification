# -*- coding: utf-8 -*-

import names


def main():
    startApplication("App_object_identification_section3")
    
    if (object.exists(names.o_Dialog)):
        #Get reference of object with waitForObject()
        button = waitForObject(names.my_Button_MyButton, 1000)
        snooze(1)
        
        #Call standard method
        button.setText("Text set from test script")
        snooze(1)
        
        #Call custom method (slot)
        button.setMyButtonText(button.myText)
        snooze(1)

        