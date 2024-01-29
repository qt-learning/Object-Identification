# -*- coding: utf-8 -*-

import names


def main():
    startApplication("App_object_identification_section3")
    
    if (object.exists(names.o_Dialog)):
        #Get reference of object with waitForObject()
        button = waitForObject(names.my_Button_MyButton, 1000)
        snooze(1)
        
        #Write standard property
        button.text = "Text modified from test script"
        snooze(1)
        
        #Read standard property
        text = button.text
        test.log("MyButton text is \"{}\".".format(text))
        
        #Read and Write custom property
        button.myText = "My new text"
        newText = button.myText
        test.log("myText is \"{}\".".format(newText))
        
        
