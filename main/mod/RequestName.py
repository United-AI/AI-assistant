# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 09:07:35 2021

@author: mHiko
"""


class Name():
    usrName = "User"
    stndMSG = "Thank you, I will call you now"
    def requestName():
        """
        Request the name of the user and gives the possibility to not give a name

        Returns
        -------
        TYPE
            DESCRIPTION.
            
            Asks if you want to give a name and only accepts "Yes" or "No"
            If yes, you have the possibility to insert a Name and automatically capitalises the answer for the output
            If no, you get the name "User" that has been set before, so outer classes can access this

        """
        qst = input("Hello User, may I ask your name? (Yes/No): ")
        if qst.lower() == ("yes"):
            Name.usrName = input("please state your name: ")
            Name.usrName = Name.usrName.capitalize()
        elif qst.lower() == ("no"):
            Name.usrName = "User"
            Name.stndMSG = "I am sorry to hear that, then I will call you"
            pass
        else:
            print("I couldn't understand your answer, please try again.")
            return Name.requestName()
        print(f"{Name.stndMSG} {Name.usrName}")
        print(" ")
        print("Feel free to ask any questions!")
        return Name.usrName
