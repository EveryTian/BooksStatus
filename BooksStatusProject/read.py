#! python3
# coding: utf-8

from sys import argv
import base


def read():
    book_id = base.base_id
    current_page = 0
    try:
        book_id = int(argv[1])
    except Exception as e:
        print(argv[1], 'is not an integer.')
        return
    if book_id <= base.base_id:
        print(argv[1], 'is not an illegal id.')
        return
    try:
        current_page = int(argv[2])
    except Exception as e:
        print(argv[2], 'is not an integer.')
        return
    if current_page <= 0:
        print(argv[2], 'is not an positive integer.')
        return
    status = base.read()
    if book_id - base.base_id > len(status):
        print("Book id", book_id, "not exist.")
        return
    if int(status[book_id - base.base_id - 1]['book_page']) < current_page:
        print("Incorrect page.")
        return
    status[book_id - base.base_id - 1]['current_page'] = str(current_page)
    base.write(status)


if __name__ == '__main__':
    read()
