# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 16:58:59 2021

@author: mHiko
"""
import os


class Importer():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    helloDict = set()
    howAreYouDict = set()

    def inputDoc():
        """
        Fills our Sets with the Message databse that we collected/created.
        This live updates while the code is running.
        -------
        Opens the txt, formats it accordinlgy and inputs it line by line into the set, every line is one set slot
        (starting with set position 0 and line 1)

        Is launched by _answer()

        """

        with open(f'{Importer.dir_path}/ressources/helloDict.txt') as f:
            Importer.helloDict.clear()
            for line in f:
                key = line.strip()
                Importer.helloDict.add(key)
            f.close()
        with open(f'{Importer.dir_path}/ressources/howAreYouDict.txt') as f:
            Importer.howAreYouDict.clear()
            for line in f:
                key = line.strip()
                Importer.howAreYouDict.add(key)
            f.close()