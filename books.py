#! python3
# coding: utf-8

import os


help_info = """Usage <Case Insensitive>:
  books -h/--help/help/<IllegalOption>
     -> [Print This Infomrmation]
  books (-s/--show/show)
     -> [Show Books' Status]
  books (-r/--read/read) <BookSerialNumber> <NewPageNumber>
     -> [Update Book's Status]
  books -a/--add/add <BookName> <BookPagesNumber>
     -> [Add New Book]
By: EveryTian (haotian_ren@outlook.com)"""
folder_path = os.path.join(os.path.dirname(__file__), 'BooksStatusProject')


def cmd_show():
    os.system("python %s" % os.path.join(folder_path, 'show.py'))

def cmd_read():
    pass

def cmd_add():
    pass


if __name__ == '__main__':
    if len(os.sys.argv) == 1:
        