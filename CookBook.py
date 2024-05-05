recipes_book = {}
with open('recipes.txt', "r+", encoding="utf8") as f:
    stop = 0
    while stop < 2:
        """Завершить цикл если получил 2 пустые строки"""
        key_name = f.readline().strip()
        if len(key_name) >= 1:
            """Пропуск пустых строк и создание ключа с пустым значением"""
            recipes_book[key_name] = None
            result = []
            for i in range(int(f.readline())):
                """Сбор значений для ключа (блюда)"""
                res = {}
                data = f.readline().strip().split("|")
                res['ingredient_name'] = data[0].rstrip()
                res['quantity'] = data[1].strip()
                res['measure'] = data[2].lstrip()
                result.append(res)
            recipes_book[key_name] = result
            stop -= 1
        else:
            stop += 1

    print(recipes_book)

def get_shop_list_by_dishes(dishes, person_count):
    """Функция вывода ингридиентов с увеличенным объемом ингридиентов на количество персон"""
    shop_list = {}
    for dish in dishes:
        for ingredient in recipes_book[dish]:
            # result = []
            shop_list[ingredient["ingredient_name"]] = None
            # print(ingredient["ingredient_name"])
            ingredient["quantity"] = int(ingredient["quantity"]) * person_count
            # ingredient: {"measure": ingredient["measure"], "quantity": ingredient["quantity"]}
            # result.append()
            # print(ingredient["quantity"])


            shop_list[ingredient["ingredient_name"]] = {"measure": ingredient["measure"], "quantity": ingredient["quantity"]}
    print(shop_list)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 2)


