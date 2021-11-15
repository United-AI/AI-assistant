# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 13:47:36 2021

@author: mHiko
"""
from mod import RequestName as rn
import os


class Manager():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    helloDict = set()
    howAreYouDict = set()
    msg = ""

    def _requestMessage():
        """
        Formats the Output accordingly to the name inputted and asks for a message
        -------
        Asks for an Input and inserts following string: "User_name: "
        
        is launched by the main init

        """
        Manager.msg = input(f"{rn.Name.usrName}: ")
        pass

    def _baseMessage():
        """
        Fills our Sets with the Message databse that we collected/created.
        This live updates while the code is running.
        -------
        Opens the txt, formats it accordinlgy and inputs it line by line into the set, every line is one set slot
        (starting with set position 0 and line 1)
        
        Is launched by _answer()

        """
        with open(f'{Manager.dir_path}/ressources/helloDict.txt') as f:
            Manager.helloDict.clear()
            for line in f:
                key = line.strip()
                Manager.helloDict.add(key)
            f.close()
        with open(f'{Manager.dir_path}/ressources/howAreYouDict.txt') as f:
            Manager.howAreYouDict.clear()
            for line in f:
                key = line.strip()
                Manager.howAreYouDict.add(key)
            f.close()

    def __init__():
        Manager._requestMessage()
        Manager._answer()
        return

    def _answer():
        """
        Is the Main Unit of sending out answers, it compares the user message with the Dict and sends out an answer accordingly

        Returns the answer of the bot
        -------
        TYPE
            DESCRIPTION.
                        BotAnswer
            
        Accesses the earlier formated Dict and compares with not in, if the from user inputted Message is part of the set
        It is not case sensitive but for now it can only compare identical strings

        """
        Manager._baseMessage()
        botMSG = "error103"
        if Manager.msg.lower() not in Manager.helloDict:
            pass
        else:
            botMSG = "Hey, how are you?"
        if Manager.msg.lower() not in Manager.howAreYouDict:
            pass
        else:
            botMSG = "Thank you for using me, what can I help you with? "
        return print(f"UnitedAi Bot: {botMSG}")
