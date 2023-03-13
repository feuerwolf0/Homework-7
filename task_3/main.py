import os

def main():
    count_rows = {}
    txt_content = {}
    sorted_count_rows = []
    # Указываю директорию где хранятся файлы
    directory = 'files/'
    # Создаю список файлов в директории
    files = [file for file in os.listdir(directory) if os.path.isfile(f'{directory}/{file}')]
    for file in files:
        with open(f'{directory}/{file}','r', encoding='UTF=8') as txt:
            # Считаю кол-во строк в файле и создаю словарь вида filename: кол-во строк
            count_rows[file] = len(txt.readlines())
            # Перемещаю указатель на начало документа
            txt.seek(0)
            # Создаю словарь вида filename:content
            txt_content[file] = txt.readlines()
    # Сортирую получившийся словарь по значениям
    sorted_count_rows = sorted(count_rows,key=count_rows.get)

    for file in sorted_count_rows:
        # Создаю файл out.txt
        with open('out.txt', 'a', encoding="UTF-8") as my_file:
            # Записываю название файла
            my_file.write(file + '\n')
            # Записываю кол-во строк в файле
            my_file.write(str(count_rows[file]) + '\n')
            # Записываю содержимое файла
            my_file.write(''.join(txt_content[file]) + '\n')


if __name__ == "__main__":
    main()