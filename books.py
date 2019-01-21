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
python_cmd_prefix = "python3"
folder_path = os.path.join(os.path.dirname(__file__), 'BooksStatusProject')
args = os.sys.argv
args_lenth = len(args)


def get_file_path(file_name):
    return os.path.join(folder_path, file_name)

def cmd_show():
    os.system(' '.join((python_cmd_prefix, get_file_path('show.py'))))
    return True

def cmd_add():
    if args_lenth < 4:
        return False
    os.system(' '.join((python_cmd_prefix, get_file_path('add.py'), args[2], args[3])))
    return True

def cmd_read():
    if args_lenth < 4:
        return False
    os.system(' '.join((python_cmd_prefix, get_file_path('read.py'), args[2], args[3])))
    return True

def cmd_help():
    print(help_info)
    return True

if __name__ == '__main__':
    if args_lenth < 2:
        cmd_show()
    else:
        argv1 = args[1].lower()
        argv1_map = {
                '-s': cmd_show,
                '--show': cmd_show,
                'show': cmd_show,
                '-a': cmd_add,
                '--add': cmd_add,
                'add': cmd_add,
                '-r': cmd_read,
                '--read': cmd_read,
                'read': cmd_read,
                '-h': cmd_help,
                '--help': cmd_help,
                'help': cmd_help,
        }
        if not argv1_map.get(argv1, lambda: False)():
            cmd_help()

