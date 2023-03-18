import datetime
def AddLog(text):
  with open('server/日誌.txt', 'a') as flog:
    nowtime = datetime.datetime.now(
      tz=datetime.timezone(datetime.timedelta(hours=8)))
    return flog.write(str(nowtime).split('+')[0] + '：寫入日誌：' + text + '\n')