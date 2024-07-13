import os
import time


def print_file(file):
    filepath = root
    filetime = os.path.getmtime(file)
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    filesize = os.path.getsize(file)
    parent_dir = os.path.dirname(root)
    print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, '
          f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')


directory = os.path.join('C:\\', 'Python_project', 'university', 'urbanUniversityHomeWork', 'Module7')
os.chdir(directory)
for root, dirs, files in os.walk(directory):
    for file in files:
        if os.path.isfile(file):
            print_file(file)
        else:
            continue
    for dir in dirs:
        for file in files:
            os.chdir(os.path.join(directory, dir))
            if os.path.isfile(file):
                print_file(file)
            else:
                continue
