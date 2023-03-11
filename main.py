def get_cook_book(filename):
    cook_book = {}
    # Открываю файл
    with open(filename,'r',encoding='UTF-8') as file:
        # Цикл по каждому рецепту в отдельности
        for i in file.read().split('\n\n'):
            # Ключ наименования блюда
            cook_book[i.split('\n')[0]] = []
            ingredients = {}
            # Цикл по всем ингридиентам
            for line in range(int(i.split('\n')[1])):
                ingredient_name, quantity, measure = i.split('\n')[line+2].split('|')
                ingredients['ingredient_name'] = ingredient_name.strip()
                ingredients['quantity'] = quantity.strip()
                ingredients['measure'] = measure.strip() 
                # Добавляю ингдридиенты в список словаря блюда
                cook_book[i.split('\n')[0]].append(ingredients)
    return cook_book


def main():
    print(get_cook_book('recipes.txt'))


if __name__ == "__main__":
    main()