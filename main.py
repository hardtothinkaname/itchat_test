import itchat
from wxpy import *
import threading
import datetime
import my_book_task
import schedule
import time


def keep_alive():
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # print(time)
    text = "保持登录," + str(time)
    itchat.send(text, toUserName="filehelper")
    global timer2
    timer2 = threading.Timer(360*60, keep_alive)
    timer2.start()


if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    keep_alive()
    my_book_task.take_one_task_by_interval()
    while True:
        schedule.run_pending()
        time.sleep(1)

