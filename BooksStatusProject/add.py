#! python3
# coding: utf-8

from sys import argv
import base


def add():
    status = base.read()
    page_number = 0
    try:
        page_number = int(argv[2])
    except Exception as e:
        print(argv[2], 'is not an integer.')
        return
    if page_number <= 0:
        print(argv[2], 'is not an positive integer.')
        return
    status.append({'book_name': argv[1].replace('\t', ' '),
                   'book_page': str(page_number),
                   'current_page': '0'})
    base.write(status)


if __name__ == '__main__':
    add()
