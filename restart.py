# importing libraries
import os 
import time
import requests

# Running a command 
def run(command):
    os.system(command)

# Telegram function for notification
def telegram_send(chat):
  bot_token = "6164636818:AAEgHAPXUbax8AOtMtMRDmr4a3nAhlrwB_U"
  bot_chat_id = "380163757"
  chat_message = 'https://api.telegram.org./bot' + bot_token + '/sendMessage?chat_id=' + bot_chat_id +'&text=' + chat # type: ignore
  response = requests.get(chat_message)
  return response.json()    

# File path of found key
cd = os.getcwd()
file_path = f"{cd}\\KEYFOUNDKEYFOUND.txt"

# Checking for found key file and restarting the keyhunt every 15 minutes 
while True:
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
            telegram_send(content)
            run('taskkill /F /IM keyhunt.exe')
            break
    else:
        time.sleep(300)
        continue