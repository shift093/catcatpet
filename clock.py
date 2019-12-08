from apscheduler.schedulers.blocking import BlockingScheduler
import urllib.request

# 宣告一個排程
sched = BlockingScheduler()

# 定義排程 : 每 1 分鐘就做一次 def scheduled_jog()
def scheduled_job():
    url = "https://catcattest.herokuapp.com/"
    connect = urllib.request.urlopen(url)
sched.add_job(scheduled_job,'cron', day_of_week='mon-sun', minute='*/1')
sched.start()  # 啟動排程
