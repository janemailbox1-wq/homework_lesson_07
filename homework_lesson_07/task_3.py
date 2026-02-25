#Задание 3.    Написать функцию, которая создаёт абсолютный путь к файлу. Позиционные аргументы: название диска, неограниченное количество папок, имя файла (без расширения). Ключевые аргументы: ext — расширение файла, sep — разделитель (по умолчанию '/').

def create_path(drive, *parts, ext=None, sep='/'):
    folders = parts[:-1] #все элементы в parts - папки
    file_name = parts[-1] #последний элемент в parts - имя файла
    if ext:
        file_name = f"{file_name}.{ext}" #добавляем к имени файла расширение
    path_parts = [drive] + list(folders) + [file_name] #собираем путь
    return sep.join(path_parts) #склеиваем путь через разделитель

print(create_path('D:', 'Users', 'Jane', 'My_docs', 'file', ext='txt')) #вызываем функцию,задаем аргументы.

