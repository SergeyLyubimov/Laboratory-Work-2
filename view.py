def start():
    functions = [add_shop, shop_shop, save_money, end]
    return functions[menu() - 1]()

def separate():
    return "\n" + "=" * 20

def menu():
    print(separate())
    print('Введите необходимое действие')
    print('1. Добавить магазин')
    print('2. Показать магазины')
    print('3. Сэкономить деньги')
    print('4. Закончить работу')
    return int(input("Введите номер необходимого действия: "))

def end():
    confirm = exit_confirm()
    if confirm == 1:
        exit()

def exit_confirm():
    print(separate())
    print("Вы точно хотите выйти? Все несохраненные данные будут потеряны.")
    print("1. Да")
    print("2. Нет")
    return int(input("Введите номер необходимого действия: "))

def info(message):
    print(separate())
    print(message)

def input_shop():
    print(separate())
    shop_name = input("Название магазина: ")
    shop_items = {}
    loop = True
    while loop:
        print(separate())
        print("1. Добавить новый товар")
        print("2. Завершить создание")
        action = int(input("Введите номер необходимого действия: "))
        if action == 1:
            print(separate())
            item_name = input("Название продукта: ")
            item_cost = int(input("Стоимость продукта: "))
            shop_items[item_name] = item_cost
        else:
            loop = False
    return shop_name, shop_items

def input_items():
    items = []
    loop = True
    while loop:
        print(separate())
        print("1. Добавить новый товар")
        print("2. Завершить создание")
        action = int(input("Введите номер необходимого действия: "))
        if action == 1:
            print(separate())
            item_name = input("Название продукта: ")
            item_count = int(input("Количество продукта: "))
            items.append((item_name, item_count))
        else:
            loop = False
    return items