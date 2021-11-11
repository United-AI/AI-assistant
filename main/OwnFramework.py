# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 12:08:04 2021

@author: mHiko
"""
from mod import RequestName as rn


class NluBasic():
    helloDict = set()
    howAreYouDict = set()
    with open('ressources/helloDict.txt') as f:
        for line in f:
            key = line.strip()
            helloDict.add(key)
    with open('ressources/howAreYouDict.txt') as f:
        for line in f:
            key = line.strip()
            howAreYouDict.add(key)
    msg = ""

    def _requestMessage():
        NluBasic.msg = input(f"{rn.Name.usrName}: ")
        return

    def _answer():
        if NluBasic.msg.lower() in NluBasic.helloDict:
            botMSG = "Hey, how are you?"
        elif NluBasic.msg in NluBasic.howAreYouDict:
            botMSG = "Thank you for using me, what can I help you with? "
        else:
            botMSG = "error103"
        return print(f"UnitedAi Bot: {botMSG}")

    def __init__(self):
        rn.Name.requestName()
        while True:
            NluBasic._requestMessage()
            NluBasic._answer()


NluBasic()
