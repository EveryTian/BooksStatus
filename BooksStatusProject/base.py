#! python3
# coding: utf-8
import os

books_file_name = "D:\CmdDevelop\BooksStatusProject\BooksStatusData"
base_id = 10000


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
        'book_name': line[0],
        'book_page': line[1],
        'current_page': line[2]
    } for line in lines]


def write(book_status):
    with open(books_file_name, 'w') as file_object:
        for book in book_status:
            file_object.write(
                book['book_name'] + '\t' +
                book['book_page'] + '\t' +
                book['current_page'] + '\n')
