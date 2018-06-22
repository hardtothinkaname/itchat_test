import book_info_query_from_net
import threading
from db_data import db_book
import time
import itchat
import schedule


def my_book_task():
    book_list = ['修真聊天群', '星辰之主', '永夜君王', '牧神记', '剑来', '原血神座']
    update_book_list = []
    notification_str = ''
    for book_name in book_list:
        is_book_updated, book = book_info_query_from_net.get_book_info_by_book_name(book_name)
        print(book[db_book.BOOK_NAME] + '已下载！')
        if is_book_updated:
            update_book_list.append(book)
            time_local = time.localtime(book[db_book.LAST_UPDATE_TIME])
            str_time = time.strftime('%Y-%m-%d %H:%M:%S', time_local)
            notification_str = notification_str + str_time + ',' + book[db_book.BOOK_NAME] + '已经更新啦！\n' \
                               + '最新章节:' + book[db_book.LAST_UPDATE_CHARTER] + '\n'
    itchat.send(notification_str, toUserName="filehelper")
    return notification_str, update_book_list


def take_one_task_by_interval():

    schedule.every(10).minutes.do(my_book_task)
    # print("----执行一次任务")
    # notification_str, update_book_list = my_book_task()
    # itchat.send(notification_str, toUserName="filehelper")
    # time.sleep(2)
    # timer3 = threading.Timer(10 * 60, take_one_task_by_interval())
    # timer3.start()