from pytube import YouTube,Playlist
from os import system
from playsound import playsound
from win10toast import ToastNotifier


class color:
    red     = '\033[91m'      # For Alerts / msgs
    white   = '\033[97m'      # For Listting The Dir

def notification(msg):
	notifi = ToastNotifier()
	notifi.show_toast("Tube-Loader",msg,duration=5)

def fscreen():
	r = color.red   # red color
	w = color.white # white color
	logo = f"""
    {r} ▄▄▄▄▄▄▄▄▄▄▄▄▄
    {r}███████████████{w}  ████████╗██╗   ██╗██████╗ ███████╗        ██╗      ██████╗  █████╗ ██████╗ ███████╗██████╗
    {r}██████ ▀███████{w}  ╚══██╔══╝██║   ██║██╔══██╗██╔════╝        ██║     ██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
    {r}██████   ▀█████{w}     ██║   ██║   ██║██████╔╝█████╗   █████╗ ██║     ██║   ██║███████║██║  ██║█████╗  ██████╔╝
    {r}██████   ▄█████{w}     ██║   ██║   ██║██╔══██╗██╔══╝   ╚════╝ ██║     ██║   ██║██╔══██║██║  ██║██╔══╝  ██╔══██╗
    {r}██████ ▄███████{w}     ██║   ╚██████╔╝██████╔╝███████╗        ███████╗╚██████╔╝██║  ██║██████╔╝███████╗██║  ██║
    {r}███████████████{w}     ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝        ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝v0.1
    {r} ▀▀▀▀▀▀▀▀▀▀▀▀▀"""
	print(logo)

def get_video():
	url = str(input("URL~# "))
	yt = YouTube(url)
	video = yt.streams.first()
	print("Start Downloading .  . .")
	video.download('./')
	msg = f"{video.title} Complete"
	notification(msg)


system('cls')
fscreen()
get_video()
system("pause")