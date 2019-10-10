# Задача-aaa:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# aaa. Перейти в папку
# bbb. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов aaa, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import sys
import os
from easy import new_dir, del_dir, in_dir, copy_file


# print(sys.argv)

def main():
    while True:
        print('''1 for change directory
2 for explore current directory
3 for remove directory
4 for create directory
q for quit''')
        task = input()

        if task == 'q':
            print('Bye!')
            break

        elif task == '1':
            dir_name = str(input('Enter the directory name: '))
            file_list = in_dir()
            print(file_list)
            if dir_name in file_list:
                os.chdir(dir_name)
                print('Moved to {} successfully'.format(dir_name), os.getcwd())
            else:
                print('No such directory!')

        elif task == '2':
            print(os.getcwd(), in_dir(dir_name))

        elif task == '3':
            dir_name = input('enter name of the directory: ')
            if del_dir(dir_name):
                print('{} removed successfully'.format(dir_name))

        elif task == '4':
            dir_name = input('enter name of the directory: ')
            if new_dir(dir_name):
                print('{} created successfully'.format(dir_name))


main()