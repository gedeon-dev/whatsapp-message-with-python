import os
import random
import pywhatkit as pwk
import time
import time
from datetime import datetime




list_num = ['+########', '+########', '+######', '+######', '+######', '+######', '+######', '+#####']       

for num in list_num:
  send_time = datetime.now()
  #These variables are to avoid whatsapp banning by span
  time_sleep_msg = random.randint(60, 150)  # Time wait
  my_wait_time = random.randint(20, 60)
  my_close_time = random.randint(5, 20)

  pwk.sendwhatmsg(num,"Your message",send_time.hour,(send_time.minute +1),  wait_time=my_wait_time, tab_close=True, close_time=my_close_time)

  time.sleep(2)
  try:
      os.system("taskkill /f /im chrome.exe")
      print('chrome close')
  except:
      print('chrome it was already closed')
  time.sleep(time_sleep_msg)