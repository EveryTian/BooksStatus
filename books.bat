@echo off
set FolderPath=D:\CmdDevelop\BooksStatusProject
if [%1] == [] (
	python "%FolderPath%\show.py"
	goto :eof
)
call :downcase %1 argv1
if "%argv1%" == "-h" (set /a help_option1 = 1) else (set /a help_option1 = 0)
if "%argv1%" == "--help" (set /a help_option2 = 1) else (set /a help_option2 = 0)
set /a help_option = help_option1 "|" help_option2
if %help_option% == 1 (
	echo Usage ^<Case Insensitive^>:
	echo   %0 -h/--help/help/^<IllegalOption^>
	echo      -^> [Print This Infomrmation]
	echo   %0 ^(-s/--show/show^)
	echo      -^> [Show Books' Status]
	echo   %0 ^(-r/--read/read^) ^<BookSerialNumber^> ^<NewPageNumber^>
	echo      -^> [Update Book's Status]
	echo   %0 -a/--add/add ^<BookName^> ^<BookPagesNumber^>
	echo      -^> [Add New Book]
	echo By: EveryTian ^(haotian_ren@outlook.com^)
	goto :eof
)
if "%argv1%" == "-s" (set /a show_option1 = 1) else (set /a show_option1 = 0)
if "%argv1%" == "--show" (set /a show_option2 = 1) else (set /a show_option2 = 0)
if "%argv1%" == "show" (set /a show_option3 = 1) else (set /a show_option3 = 0)
set /a show_option = show_option1 "|" show_option2 "|" show_option3
if %show_option% == 1 (
	python "%FolderPath%\show.py"
	goto :eof
)
if "%argv1%" == "-a" (set /a add_option1 = 1) else (set /a add_option1 = 0)
if "%argv1%" == "--add" (set /a add_option2 = 1) else (set /a add_option2 = 0)
if "%argv1%" == "add" (set /a add_option3 = 1) else (set /a add_option3 = 0)
set /a add_option = add_option1 "|" add_option2 "|" add_option3
if %add_option% == 1 (
	if [%2] == [] (
		%0 --help
	) else if [%3] == [] (
		%0 --help
	) else (
		python "%FolderPath%\add.py" %2 %3
	)
	goto :eof
)
if "%argv1%" == "-r" (set /a read_option1 = 1) else (set /a read_option1 = 0)
if "%argv1%" == "--read" (set /a read_option2 = 1) else (set /a read_option2 = 0)
if "%argv1%" == "read" (set /a read_option3 = 1) else (set /a read_option3 = 0)
set /a read_option = read_option1 "|" read_option2 "|" read_option3
if %read_option% == 1 (
	if [%2] == [] (
		%0 --help
	) else if [%3] == [] (
		%0 --help
	) else (
		python "%FolderPath%\read.py" %2 %3
	)
	goto :eof
)
if [%1] == [] (
	%0 --help
) else if [%2] == [] (
	%0 --help
) else (
	python "%FolderPath%\read.py" %1 %2
)
goto :eof

:DOWNCASE
SET "UP=A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
SET "DOWN=a b c d e f g h i j k l m n o p q r s t u v w x y z"
REM CALL :DOWNCASE %STR% RESULT
SETLOCAL ENABLEDELAYEDEXPANSION
SET $=&SET "#=%~1"
IF DEFINED # (
    FOR %%A IN (%DOWN%) DO SET #=!#:%%A=%%A!
)
ENDLOCAL&SET "%~2=%#%"&EXIT/B
