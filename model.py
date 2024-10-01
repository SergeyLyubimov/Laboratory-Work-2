shop_list = {}


def add_shop(info):
    global shop_list
    shop_name, shop_items = info
    shop_list[shop_name] = shop_items
    return shop_name, shop_items


def show_shops():
    global shop_list
    result = '\n'.join([f'{shop_name}:\n\t{'\n\t'.join([f'{item_name}: {item_value}' for item_name, item_value in shop_items.items()])}' for shop_name, shop_items in shop_list.items()])
    return result

def save_money(info):
    global shop_list
    item_costs = {item[0]: ('none', -1, item[1]) for item in info}
    for shop_name, shop_items in shop_list.items():
        for item_name, item_value in item_costs.items():
            if shop_items.get(item_name) < item_value[1] or item_value[0] == 'none':
                item_costs[item_name] = (shop_name, shop_items.get(item_name), item_value[2])
    result = '\n'.join([f'{item_name} ({item_value[2]} шт.) находится в магазине {item_value[0]} за {item_value[1] * item_value[2]} рублей!' for item_name, item_value in item_costs.items()])
    result += f'\nИтого вы потратите {sum(item_value[1] * item_value[2] for item_value in item_costs.values())} рублей!'
    return result

def end_work():
    return exit()