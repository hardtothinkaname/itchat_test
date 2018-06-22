import my_net
import novel_re
import time
import urllib.parse
from db_data import db_book
import book_info_query_from_net

if __name__ == '__main__':
    novel_name = '修真聊天群'
    # novel_name_parse = urllib.parse.quote(novel_name)
    #
    # url = "http://www.sodu.cc/result.html?searchstr=%E6%B0%B8%E5%A4%9C%E5%90%9B%E7%8E%8B"
    # url = "http://www.sodu.cc/result.html?searchstr=" + novel_name_parse
    # html = my_net.get_html(url, 'utf-8')
    # book_id_list = novel_re.get_book_id(html)
    # book_list = novel_re.get_book_name(html)
    # charter_list = novel_re.get_last_charter_name(html)
    # charter_time_list = novel_re.get_last_charter_time(html)
    #
    # # 时间的处理
    # timeTuple = time.strptime(charter_time_list[0], '%Y/%m/%d %H:%M:%S')
    # time_long = time.mktime(timeTuple)
    # time_local = time.localtime(time_long)
    # strtime= time.strftime('%Y-%m-%d %H:%M:%S', time_local)
    #
    # # 存储
    # db_book.save_one_book(book_id_list[0], book_list[0], charter_list[0], time_long)
    #
    # list1 = list(map(lambda x, w, y, z: [x, w, y, z], book_id_list, book_list, charter_list, charter_time_list))

    # , '永夜君王', '牧神记'
    book_list = ['修真聊天群', '星辰之主']

    update_book_list = []
    notification_str = ''
    for book_name in book_list:
        is_book_updated, book = book_info_query_from_net.get_book_info_by_book_name(book_name)
        if is_book_updated:
        # if True:
            update_book_list.append(book)
            time_local = time.localtime(book[db_book.LAST_UPDATE_TIME])
            strtime= time.strftime('%Y-%m-%d %H:%M:%S', time_local)
            notification_str = notification_str + strtime + ',' + book[db_book.BOOK_NAME] + '已经更新啦！\n' \
                               + '最新章节:' + book[db_book.LAST_UPDATE_CHARTER] + '\n'

    print(update_book_list)
    print(notification_str)