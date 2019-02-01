from setuptools import setup, find_packages
import platform

is_windows = platform.platform()[:3].lower() == 'win'


setup(
    name='books',
    version='1.0',
    description='CLI Reading Progress Management',
    url='https://github.com/EveryTian/BooksStatus',
    packages=find_packages(),
    author='EveryTian',
    author_email='haotian_ren@outlook.com',
    scripts=['books/books.bat' if is_windows else 'books/books'],
    zip_safe=False
)

try:
    from books import base 
    project_folder_path = base.get_project_folder_path()
    from subprocess import Popen, PIPE
    get_script_path_cmd = 'where books' if is_windows else 'which books'
    script_path = Popen(get_script_path_cmd, stdout=PIPE, shell=True).communicate()[0].strip()
    script_file_lines = []
    with open(script_path, 'r') as f:
        modified_flag = False
        for l in f:
            if not modified_flag and l.rstrip().endswith('#####'):
                the_line = script_file_lines[-1]
                script_file_lines[-1] = the_line[:the_line.index('=') + 1] + project_folder_path + '\n'
                modified_flag = True
            script_file_lines.append(l)
    with open(script_path, 'w') as f:
        f.writelines(script_file_lines)
except Exception as e:
    import sys
    sys.stderr.write(str(e))
