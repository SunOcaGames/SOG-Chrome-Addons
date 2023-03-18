import time as t
from server.log import AddLog
import server.firebase as fire
def online(name):
  fire.save(name)
  AddLog(name + '宣布在線，已上傳至firebase')