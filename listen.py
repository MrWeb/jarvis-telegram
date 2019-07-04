import os
import time
import telepot
import datetime
from pprint import pprint
from telepot.loop import MessageLoop
# from gpiozero import MotionSensor

import netifaces as ni

#Chiave Bot
bot = telepot.Bot('860476951:AAEMtxxzxsmqVY3BuDGLB6S9h3CnVOJK9yQ')

def process_command(msg, content_type, chat_type, chat_id):
    bot.sendMessage(chat_id, switch(msg['text'], chat_id))

def switch(cmd, chat_id):
    # Runna la function cmd() calcolata da variabile togliendo \ iniziale
    return globals()[cmd[1:]](chat_id)

def start(chat_id):
    return 'Jarvis Bot Started'

def ip(chat_id):
    IP = ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr']
    return "Current Jarvis IP: {}".format(IP)

def reboot(chat_id):
    tm = datetime.datetime.now()
    bot.sendMessage(chat_id, "Reboot request received at {}...".format(tm))
    os.system('sudo reboot')

def shut(chat_id):
    tm = datetime.datetime.now()
    bot.sendMessage(chat_id, "Shutdown request received at {}...".format(tm))
    os.system('sudo shutdown now')

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        process_command(msg, content_type, chat_type, chat_id)

# def watch(chat_id):
#     pir = MotionSensor(4) #4 = il pin a cui è collegato sulla board madre
#     bot.sendMessage(chat_id, '[Sensor Armed]')
#     while True:
#         pir.wait_for_motion()
#         #print("Motion detected at {}".format(datetime.datetime.now()))
#         bot.sendMessage(chat_id, "Rilevato movimento: {}".format(datetime.datetime.now()))
#         time.sleep(30)

# def arm(chat_id):
#     watch(chat_id)

def main():
    MessageLoop(bot, handle).run_as_thread()
    while 1:
        time.sleep(10)

if __name__ == '__main__':
    main()
