import pymongo
import datetime

book_tabke_name = 'bookTable'
BOOK_ID = 'bookId'
BOOK_NAME = 'bookName'
LAST_UPDATE_CHARTER = 'lastUpdateCharter'
LAST_UPDATE_TIME = 'lastUpdateTime'

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["runoobdb"]
book_table = mydb["novel"]


def insert_one_book(book_id, book_name, last_charter, last_update_time):
    novel = {BOOK_ID: book_id, BOOK_NAME: book_name, LAST_UPDATE_CHARTER: last_charter, LAST_UPDATE_TIME: last_update_time}
    book_table.insert_one(novel)


def find_book_by_book_id(book_id):
    book = book_table.find_one({BOOK_ID: book_id})
    return book


def update_one_book_by_book_id(book_id, book_name, last_charter, last_update_time):
    myquery = {BOOK_ID: book_id}
    novel = {"$set": {BOOK_NAME: book_name, LAST_UPDATE_CHARTER: last_charter, LAST_UPDATE_TIME: last_update_time}}
    book_table.update_one(myquery, novel)


def save_one_book(book_id, book_name, last_charter, last_update_time):
    book = find_book_by_book_id(book_id)
    if book is None:
        insert_one_book(book_id, book_name, last_charter, last_update_time)
    else:
        update_one_book_by_book_id(book_id, book_name, last_charter, last_update_time)


def save_one_book1(book):
    save_one_book(book[BOOK_ID], book[BOOK_NAME], book[LAST_UPDATE_CHARTER], book[LAST_UPDATE_TIME])




if __name__ == "__main__":

    # bookid = 1001
    # book_name = 'yyyy'
    # last_charter = '135ss'
    # last_update_time = '2018-05-02 11:12:65'
    # insert_one_book(bookid, book_name, last_charter, last_update_time)
    #
    # insert_one_book(1050, '10050', last_charter, last_update_time)


    book = find_book_by_book_id(1050)

    update_one_book_by_book_id(book[BOOK_ID], 'new', 'helo', 'alal')

    book = find_book_by_book_id(1000)
    print(book)
