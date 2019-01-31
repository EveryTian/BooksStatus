#!python
# coding: utf-8
import os

data_file_path = os.path.join(os.path.expanduser('~'), '.BooksStatusData')
base_id = 10000


def read():
    mode = 'r'
    if not os.path.exists(data_file_path):
        mode = 'w+'
    with open(data_file_path, mode=mode) as file_object:
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
    with open(data_file_path, 'w') as file_object:
        for book in book_status:
            file_object.write(
                book['book_name'] + '\t' +
                book['book_page'] + '\t' +
                book['current_page'] + '\n')


def get_data_file_path():
    return data_file_path


def get_project_folder_path():
    return os.path.dirname(os.path.dirname(__file__))

