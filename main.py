# Importing Libraries 
import os
import time
import requests

# Range parameter
start = 1 
end = 73786976294838206463 # end of range for puzzle number 66

# Telegram function for notification
def telegram_send(chat):
  bot_token = "6164636818:AAEgHAPXUbax8AOtMtMRDmr4a3nAhlrwB_U"
  bot_chat_id = "380163757"
  chat_message = 'https://api.telegram.org./bot' + bot_token + '/sendMessage?chat_id=' + bot_chat_id +'&text=' + chat # type: ignore
  response = requests.get(chat_message)
  return response.json() 

# Running a command function
def run(command):
    os.system(command)

# Path to file list of public key to check
cd = os.getcwd()
path = f"{cd}\\pubkey.txt"

# Turn integer number into bitcoin hexadecimal
def int_to_hex(value):
    hex = format(value, '064x')
    return hex

# main function
def main():
    run('cls')
    range_start = int_to_hex(start)
    range_end = int_to_hex(end)
    command_to_execute = f'keyhunt.exe -m bsgs -f {path} -t 16 -r {range_start}:{range_end} -q -k 512 -B sequential -s 10 -S'
    run(command_to_execute)
    time.sleep(1)
  
# Run the main function  
if __name__ == '__main__':
    main()
    telegram_send(f"Run Finished! Range : {start} - {end}")