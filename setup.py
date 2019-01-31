from setuptools import setup, find_packages
import platform

is_windows = platform.platform()[:3].lower() == 'win'


s = setup(name='books',
    # version='0.1',
    description='CLI Reading Progress Management',
    url='https://github.com/EveryTian/BooksStatus',
    packages=find_packages(),
    author='EveryTian',
    author_email='haotian_ren@outlook.com',
    scripts=['books/books.bat' if is_windows else 'books/books'],
    zip_safe=False)
print  s.command_obj['install'].install_lib

import books

