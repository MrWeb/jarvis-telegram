import telegram_send
import listen
import netifaces as ni

telegram_send.send(["Jarvis accesso con IP: {}".format(ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr'])])
listen.main()