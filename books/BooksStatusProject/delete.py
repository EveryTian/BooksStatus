#!python
# coding: utf-8

from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import division

from sys import argv
import base

try:
    input = raw_input
except NameError as e:
    pass

def delete():
    book_id = base.base_id
    try:
        book_id = int(argv[1])
    except Exception as e:
        print(argv[1], 'is not an integer.')
        return
    if book_id <= base.base_id:
        print(argv[1], 'is not an illegal id.')
        return
    status = base.read()
    if book_id - base.base_id > len(status):
        print('Book id', book_id, 'not exist.')
        return
    deleted_book = status.pop(book_id - base.base_id - 1)
    try:
        affirmative = input("Delete item:\n  %s %s/%s\nSure? (Y/else) " % (
            deleted_book['book_name'], deleted_book['current_page'], deleted_book['book_page']
        ))
    except KeyboardInterrupt:
        print('\nCanceled.')
        return
    if affirmative == 'Y':
        base.write(status)
        print('Deleted.')
    else:
        print('Canceled.')


if __name__ == '__main__':
    delete()
