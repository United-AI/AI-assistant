# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 13:47:36 2021

@author: mHiko
"""
from mod import ImportDoc as impdi
import re

class Manager():
    msg = ""
    usrNam = ""

    def __init__():
        """
        just launching stuff

        """
        Manager._requestMessage(Manager.usrNam)
        Manager._answer()

    def _requestMessage(name):
        """
        Formats the Output accordingly to the name inputted and asks for a message
        -------
        Asks for an Input and inserts following string: "User_name: "

        is launched by the main init

        """
        Manager.usrNam = name
        Manager.msg = input(f"{Manager.usrNam}: ")
        pass

    def _answer():
        """
        Is the Main Unit of sending out answers, it compares the 
        user message with the Dict and sends out an answer accordingly

        Returns the answer of the bot
        -------
        TYPE
            DESCRIPTION.

        Formats and acccesses the Dict and compares with "not in",
        if the from user inputted Message is part of the set
        Looks for ONLY the word, not more or less, is not case sensitive
        and should work for every string

        """
        impdi.Importer.inputDoc()
        botMSG = "error103"
        for check in impdi.Importer.helloDict:
            helloComp=check
            pattern = r'(^|[^\w]){}([^\w]|$)'.format(helloComp)
            pattern = re.compile(pattern, re.IGNORECASE)
            matches = re.search(pattern, Manager.msg.lower())
            if bool(matches):
                botMSG = "Hey, how are you?"
            else:
                pass
        for val in impdi.Importer.howAreYouDict:
            howAreComp=val
            pattern = r'(^|[^\w]){}([^\w]|$)'.format(howAreComp)
            pattern = re.compile(pattern, re.IGNORECASE)
            matches = re.search(pattern, Manager.msg.lower())
            if bool(matches):
                botMSG = "Thank you for using me, what can I help you with? "
            else:
                pass
            
        return print(f"UnitedAi Bot: {botMSG}")
