# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 13:47:36 2021

@author: mHiko
"""
from mod import ImportDoc as impdi


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
        Is the Main Unit of sending out answers, it compares the user message with the Dict and sends out an answer accordingly

        Returns the answer of the bot
        -------
        TYPE
            DESCRIPTION.

        Formats and acccesses the Dict and compares with "not in", if the from user inputted Message is part of the set
        It is not case sensitive but for now it can only compare identical strings

        """
        impdi.Importer.inputDoc()
        botMSG = "error103"
        if Manager.msg.lower() not in impdi.Importer.helloDict:
            pass
        else:
            botMSG = "Hey, how are you?"
        if Manager.msg.lower() not in impdi.Importer.howAreYouDict:
            pass
        else:
            botMSG = "Thank you for using me, what can I help you with? "
        return print(f"UnitedAi Bot: {botMSG}")