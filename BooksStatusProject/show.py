#! python3
# coding: utf-8

import base


def show():
    status = base.read()
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
