#!python
# coding: utf-8

from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import division

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
        print('Book id', book_id, 'not exist.')
        return
    book_status = status[book_id - base.base_id - 1]
    book_page_str = book_status['book_page']
    if int(book_page_str) < current_page:
        print('Incorrect page.')
        return
    current_page_str = str(current_page)
    origin_page_str = book_status['current_page']
    book_status['current_page'] = current_page_str
    book_name = book_status['book_name']
    base.write(status)
    print("Updated: %s %s/%s->%s/%s" % (
        book_name,
        origin_page_str, book_page_str,
        current_page_str, book_page_str
    ))


if __name__ == '__main__':
    read()
