#! python3
# coding: utf-8
import os
import platform

books_file_name = os.path.join(os.path.dirname(__file__), 'BooksStatusData')
base_id = 10000

if platform.platform()[:7].lower() != 'windows':
    books_file_name = os.path.expanduser('~/.BooksStatusData')

def read():
    mode = 'r'
    if not os.path.exists(books_file_name):
        mode = 'w+'
    with open(books_file_name, mode=mode) as file_object:
        lines = [line.replace('\n', '').split('\t')
                 for line in file_object.readlines()]
    while lines.count(['']) != 0:
        lines.remove([''])
    return [{
        'id': base_id + 1 + i,
        'book_name': line[0],
        'book_page': line[1],
        'current_page': line[2]
    } for i, line in enumerate(lines)]


def write(book_status):
    with open(books_file_name, 'w') as file_object:
        for book in book_status:
            file_object.write(
                book['book_name'] + '\t' +
                book['book_page'] + '\t' +
                book['current_page'] + '\n')
