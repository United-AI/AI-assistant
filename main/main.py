# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 12:08:04 2021

@author: mHiko
"""

from mod import MessageManager as mm
from mod import RequestName as rn


class Main():

    def __init__(self):
        """
        just launching stuff

        """
        mm.Manager.usrNam = rn.Name.requestName()
        while True:
            mm.Manager.__init__()


Main()