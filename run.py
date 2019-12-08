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
