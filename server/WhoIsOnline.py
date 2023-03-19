import time as t
from server.log import AddLog
import server.firebase as fire
online_time=0 
def online(name):
  global online_time
  fire.save(name)
  online_time=t.time()
  AddLog(name + '宣布在線，已上傳至firebase')