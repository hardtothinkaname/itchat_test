import my_net
import novel_re
import time
import urllib.parse
from db_data import db_book



def get_book_info_by_book_name(book_name):
    is_book_updated = False

    novel_name_parse = urllib.parse.quote(book_name)
    url = "http://www.sodu.cc/result.html?searchstr=" + novel_name_parse
    html = my_net.get_html(url, 'utf-8')
    book_id_list = novel_re.get_book_id(html)
    if len(book_id_list) < 1:
        return False, None

    book_id = novel_re.get_book_id(html)[0]
    book_name = novel_re.get_book_name(html)[0]
    last_charter = novel_re.get_last_charter_name(html)[0]
    last_charter_update_time = novel_re.get_last_charter_time(html)[0]

    # 时间的处理
    time_tuple = time.strptime(last_charter_update_time, '%Y/%m/%d %H:%M:%S')

    time_long = time.mktime(time_tuple)
    newbook = {db_book.BOOK_ID: book_id,
               db_book.BOOK_NAME: book_name,
               db_book.LAST_UPDATE_CHARTER: last_charter,
               db_book.LAST_UPDATE_TIME: time_long}



    # 查找是否存在本书
    book_in_db = db_book.find_book_by_book_id(book_id)

    if book_in_db is None:
        is_book_updated = True
    else:
        is_book_updated = book_in_db[db_book.LAST_UPDATE_CHARTER] != last_charter

    if is_book_updated:
        # 存储
        # db_book.save_one_book(book_id, book_name, last_charter, time_long)
        db_book.save_one_book1(newbook)
        return is_book_updated, newbook
    else:
        return is_book_updated, book_in_db



if __name__ == '__main__':
    is_book_updated, book = get_book_info_by_book_name('修真聊天群')
    print(is_book_updated)
    print(book)