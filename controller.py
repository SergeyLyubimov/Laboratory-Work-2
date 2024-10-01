import view as v
import model as m


def start():
    functions = [add_shop, print_shops, save_money, end]
    return functions[v.menu() - 1]()


def add_shop():
    return v.info(m.add_shop(v.input_shop()))


def print_shops():
    return v.info(m.show_shops())

def save_money():
    return v.info(m.save_money(v.input_items()))


def end():
    confirm = v.exit_confirm()
    if confirm == 1:
        return m.end_work()