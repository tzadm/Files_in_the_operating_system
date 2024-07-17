def pywalker(path):
    import os
    import time
    for root, dirs, files in os.walk(path):
        for file_ in files:
            filepath = os.path.join(root, file_)
            filetime = os.path.getmtime(os.path.join(root, file_))
            formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
            filesize = os.path.getsize(os.path.join(root, file_))
            parent_dir = os.path.dirname(os.path.join(root, file_))
            parent_dir_ = parent_dir.split('\\')[-1]
            print(f'\n Обнаружен файл: {file_}\n Путь: {filepath}'
                  f'\n Размер: {filesize} байт\n Время изменения: {formatted_time}'
                  f'\n Родительская директория: {parent_dir_}\n')

