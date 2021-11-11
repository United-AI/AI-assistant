# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 09:07:35 2021

@author: mHiko
"""


class Name():
    usrName = "User"

    def requestName():
        qst = input("Hello User, may I ask your name? (Yes/No)")
        if qst.lower() == ("yes"):
            Name.usrName = input("please state your name: ")
            Name.usrName = Name.usrName.capitalize()
        elif qst.lower() == ("no"):
            Name.usrName = "User"
            pass
        else:
            print("I couldn't understand your answer, please try again.")
            return Name.requestName()
        print(f"Thank you, I will call you now  {Name.usrName}")
        print(" ")
        print("Feel free to ask any questions!")
        return
