# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 12:08:04 2021

@author: mHiko
"""
from mod import MessageManager as mm
from mod import RequestName as rn


class main():

    def __init__(self):
        rn.Name.requestName()
        while True:
            mm.Manager.__init__()


main()
