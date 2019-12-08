from apscheduler.schedulers.blocking import BlockingScheduler
import urllib

# 宣告一個排程
sched = BlockingScheduler()

# 定義排程 : 每 1 分鐘就做一次 def scheduled_jog()
@sched.scheduled_job('cron', day_of_week='mon – sun', minute='*/1')
def scheduled_job():
    url = "https://catcattest.herokuapp.com/"
    connect = urllib.request.urlopen(url)
    
sched.start()  # 啟動排程
