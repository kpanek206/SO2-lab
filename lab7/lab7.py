#!/usr/bin/env python3

#W zadanym drzewie katalogów znaleźć podkatalogi, do których 
# właściciel nie ma prawa odczytu lub prawa wykonania, natomiast 
# ktoś inny (właściciel grupowy lub nie) ma prawo zapisu. 
# Skrypt nie powinien zakładać żadnych dodatkowych warunków 
# dotyczących praw dostępu.


import os
import sys
import stat

if len(sys.argv)!=2:
    print("Liczba argumentow jest niepoprawna")
else:
    if os.path.isdir(sys.argv[1]):
        for root, dirs, files in os.walk(sys.argv[1]):
            for name in dirs:
                pathname = os.path.join(root, name)
                mode = os.stat(pathname).st_mode
            
                checkOwnerRD = bool(mode & stat.S_IRUSR)
                checkOwnerEX = bool(mode & stat.S_IXUSR)
                checkOtherWR = bool(mode & (stat.S_IWGRP | stat.S_IWOTH))
                if (checkOwnerRD == False or checkOwnerEX == False) and checkOtherWR == True:
                    print(os.path.join(root, name))

    
