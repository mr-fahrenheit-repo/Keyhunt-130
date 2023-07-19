# Importing Libraries 
import os
import time
import random

# Running a command function
def run(command):
    os.system(command)

# Range parameter
start = 884734153994440035227919469688326717440 # 3/10 from range on puzzle number 130
end = 1156960047531190745552328174902282551296 # 7/10 from range on puzzle number 130

# Path to file list of public key to check
cd = os.getcwd()
path = f"{cd}\\pubkey.txt"

# Turn integer number into bitcoin hexadecimal
def int_to_hex(value):
    hex = format(value, '064x')
    return hex

# Looping the whole process
while True:
    run('cls')
    x = random.randint(start, end)
    range_start = int_to_hex(x)
    range_end = int_to_hex(x + 49258120924364800)
    command_to_execute = f'keyhunt.exe -m bsgs -f {path} -t 8 -r {range_start}:{range_end} -q -k 256 -B sequential -s 10 -S'
    run(command_to_execute)
    time.sleep(3)