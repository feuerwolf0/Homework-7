def get_shop_list_by_dishes(dishes, person_count):
    # Получаю рецепты
    cook_book = get_cook_book('recipes.txt')
    # Создаю шоп-лист словарь
    shop_list = {}
    for dish in dishes:
        for ingr in cook_book[dish]:
            ingredient_name, quantity, measure = ingr.values()
            # Если ингридиент уже есть, увеличиваю его кол-во
            if ingredient_name in shop_list:
                shop_list[ingredient_name]['quantity'] += int(quantity)*person_count
            else:
                shop_list[ingredient_name] = {'measure': measure, 'quantity': int(quantity)*person_count}
    return shop_list
    

def get_cook_book(filename):
    cook_book = {}
    # Открываю файл
    with open(filename,'r',encoding='UTF-8') as file:
        # Цикл по каждому рецепту в отдельности
        for i in file.read().split('\n\n'):
            # Ключ наименования блюда
            cook_book[i.split('\n')[0]] = []
            # Цикл по всем ингридиентам
            for line in range(int(i.split('\n')[1])):
                ingredients = {}
                ingredient_name, quantity, measure = i.split('\n')[line+2].split('|')
                ingredients['ingredient_name'] = ingredient_name.strip()
                ingredients['quantity'] = quantity.strip()
                ingredients['measure'] = measure.strip() 
                # Добавляю ингдридиенты в список словаря блюда
                cook_book[i.split('\n')[0]].append(ingredients)
    return cook_book


def main():
    print(get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 2))

if __name__ == "__main__":
    main()