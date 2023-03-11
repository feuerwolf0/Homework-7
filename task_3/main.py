import os

def main():
    count_rows = {}
    sorted_count_rows = []
    # Указываю директорию где хранятся файлы
    directory = 'task_3/files/'
    # Создаю список файлов в директории
    files = [file for file in os.listdir(directory) if os.path.isfile(f'{directory}/{file}')]
    for file in files:
        txt = open(f'{directory}/{file}','r', encoding='UTF=8')
        # Считаю кол-во строк в файле и создаю словарь вида filename: кол-во строк
        count_rows[file] = len(txt.readlines())
        txt.close()
    # Сортирую получившийся словарь по значениям
    sorted_count_rows = sorted(count_rows,key=count_rows.get)

    for file in sorted_count_rows:
        txt = open(f'{directory}/{file}','rt',encoding="UTF-8")
        # Создаю файл out.txt
        with open('task_3/out.txt', 'a', encoding="UTF-8") as my_file:
            # Записываю название файла
            my_file.write(file + '\n')
            # Записываю кол-во строк в файле
            my_file.write(str(count_rows[file]) + '\n')
            # Записываю содержимое файла
            my_file.write(''.join(txt.readlines()) + '\n')
        txt.close()


if __name__ == "__main__":
    main()