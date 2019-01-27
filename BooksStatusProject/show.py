#!python
# coding: utf-8

from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import division

import base


def show():
    status = base.read()
    if status == []:
        print("No books. Use '--add' option to add a book.")
    i = base.base_id + 1
    for book in status:
        percent_info = "%3d%%" % (
            int(float(book['current_page']) / float(book['book_page']) * 100))
        page_info = "%03d/%03d" % (int(book['current_page']),
                                   int(book['book_page']))
        print('No.' + str(i), percent_info,
              page_info, book['book_name'], sep='  ')
        i += 1


if __name__ == '__main__':
    show()
