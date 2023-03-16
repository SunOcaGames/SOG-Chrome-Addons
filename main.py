from flask import Flask
import server.firebase as fire
import time as t
import datetime

app = Flask('app')

def AddLog(text):
  with open('server/日誌.txt','a') as flog:
    nowtime= datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8)))
    return flog.write(str(nowtime).split('+')[0]+'：寫入日誌：'+text+'\n')

@app.route('/')
def home():
  return '<h2>這裡是你該來的地方嗎！走錯路了啦！<br>😤🤬👾<br>這裡不是每個人都能來的！</h2>'

@app.route('/UpTimeRobot')
def UpTimeRobot():
  AddLog('url-/UpTimeRobot被開啟了')
  return 'Hello UpTimeRobot!'

@app.route('/online/<name>')
def online(name):
  AddLog('url-/online/<name>被開啟了')
  fire.save(name)
  AddLog(name+'宣布在線，已上傳至firebase')
  return name + '在' + str(t.time()) + '時宣布在線，已上傳至firebase'


@app.route('/test')
def test():
  AddLog('url-/test被開啟了')
  data = fire.dowmdate('Scratch_Online/SOG')
  AddLog('已有人詢問有誰登入，已回復：上次驗證登入在' + format(t.time() - data['online_time'], '.2f') + '秒前')
  return '上次驗證登入在' + format(t.time() - data['online_time'], '.2f') + '秒前'

@app.route('/addons')
def addons():
  AddLog('url-/addons被開啟了')
  AddLog('已傳送addons/chrome.js檔')
  with open('addons/chrome.js','r') as f:
    return f.read()

@app.route('/log')
def log():
  AddLog('url-/log被開啟了')
  AddLog('已傳送server/日誌.txt檔')
  t.sleep(0.5)
  with open('server/日誌.txt','r') as f:
    a=''
    for line in f.readlines():
      a=line+'<br>'+a
    return '<h2>beta測試版</h2>太陽之海遊戲的chrome外掛程式伺服器的日誌'+a
app.run(host='0.0.0.0', port=8080)

