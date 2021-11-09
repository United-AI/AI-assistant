# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 12:08:04 2021

@author: mHiko
"""

class NluBasic():
    helloDict = set()
    howAreYouDict = set()
    with open('helloDict.txt') as f:
        for line in f:
            key= line.strip()
            helloDict.add(key)
    with open('howAreYouDict.txt') as f:
        for line in f:
            key= line.strip()
            howAreYouDict.add(key)
    msg = ""
    def requestMessage():
        NluBasic.msg = input("Please Input an answer: ")
        pass
    
    def _answer():
        if NluBasic.msg in NluBasic.helloDict:
            botMSG = "Hey, how are you?"
        elif NluBasic.msg in NluBasic.howAreYouDict:
            botMSG = "Thank you for using me, what can I help you with? "
        else:
           botMSG ="error103"
        return print(f"UnitedAi Bot: {botMSG}")
    
    def __init__(self):
        while True:
            NluBasic.requestMessage()
            NluBasic._answer()

NluBasic()
    
