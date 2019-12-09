from apscheduler.schedulers.blocking import BlockingScheduler
import requests
import urllib.request

# 宣告一個排程
sched = BlockingScheduler()

# 定義排程 : 每 1 分鐘就做一次 def scheduled_jog()
"""
def scheduled_job():
    url = "https://catcattest.herokuapp.com/"
    connect = urllib.request.urlopen(url)
"""
def lineNotifyMessage():
    message = '[測試階段]Hello！各位～記得抓貓唷！'
    #message = '[LINE Notify]Hello！各位～記得抓貓唷！' # 要傳送的訊息內容
    token = 'nHiUiakxNdMzf9Kt05A1oWJTas9oZQ5Oa2gYF5bx5AK' # 權杖值
    headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }
    massage = {'message': message}
    #massage = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = massage)
    return r.status_code

    
if __name__ == '__main__':
    #message = '[LINE Notify] Hello World 記得抓貓唷' # 要傳送的訊息內容
    #token = 'nHiUiakxNdMzf9Kt05A1oWJTas9oZQ5Oa2gYF5bx5AK' # 權杖值
    #sched.add_job(lineNotifyMessage(token, message),'cron', day_of_week='mon-sun', minute='*/1')
    #sched.add_job(lineNotifyMessage,'cron', day_of_week='mon-sun', minute='*/1')
    
    sched.add_job(lineNotifyMessage,'cron',hour='1-23',minute=5)
    sched.add_job(lineNotifyMessage,'cron',hour='1-23',minute=6)
    
    #sched.add_job(lineNotifyMessage,'cron',hour='1-2,5-8,10-12',minute=4)
    #sched.add_job(lineNotifyMessage,'cron',hour='1-2,5-8,10-12',minute=5)
    
    #sched.add_job(scheduled_job,'cron', day_of_week='mon-sun', minute='*/1')
    #sched.add_job(scheduled_job,'cron',hour='9-10,13-16,18-20',minute=58)
    sched.start()  # 啟動排程

"""
import requests


def lineNotifyMessage(token, msg):
    headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }

    massage = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = massage)
    return r.status_code


if __name__ == '__main__':
  message = '[LINE Notify] Hello World 記得抓貓唷' # 要傳送的訊息內容
  token = 'nHiUiakxNdMzf9Kt05A1oWJTas9oZQ5Oa2gYF5bx5AK' # 權杖值

  lineNotifyMessage(token, message)
"""
