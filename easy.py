import os
import shutil

# Задача-aaa:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

print('Ваща директория {}'.format(os.getcwd()))


def new_dir(i):
    os.mkdir('{}'.format(i))


def del_dir(i):
    os.rmdir('{}'.format(i))


def chdir(i):
    os.chdir(i)


for each in range(9):
    new_dir('dir_{}'.format(each + 1))
print(os.listdir())
for each in range(9):
    del_dir('dir_{}'.format(each + 1))


# Задача-bbb:
# Напишите скрипт, отображающий папки текущей директории.

def in_dir():
    print('Содержимое директории: {}'.format(os.listdir()))


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_file():
    shutil.copy('easy.py', 'easy_copy.py')


copy_file()
