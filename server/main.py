from flask import Flask
import firebase as fire
import time as t

app = Flask('app')


@app.route('/')
def home():
  return '<h2>這裡是你該來的地方嗎！走錯路了啦！<br>😤🤬👾<br>這裡不是每個人都能來的！</h2>'


@app.route('/online/<name>')
def online(name):
  fire.save(name)
  return name + '在' + str(t.time()) + '時宣布在線，已上傳至firebase'


@app.route('/test')
def test():
  data = fire.dowmdate('Scratch_Online/SOG')
  return '上次驗證登入在' + format(t.time() - data['online_time'], '.2f') + '秒前'


app.run(host='0.0.0.0', port=8080)
