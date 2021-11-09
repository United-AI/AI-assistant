# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 12:08:04 2021

@author: mHiko
"""

class NluBasic():
    def requestMessage():
        msg = input("Please Input an answer: ")
        return msg
    
    def __init__(self):
        msg = NluBasic.requestMessage()
        return print(f"You wrote following message: {msg} ")

NluBasic()
    