from datetime import datetime

from main import run
from objects import Item, ToDoList


def test_item_create():
    test_name = 'Item Create Test'
    test_date = datetime.now().date()
    test_string = 'test'
    test_item = Item(test_string)
    if test_item.title == test_string and test_item.pub_date == test_date:
        print(f'[ OK ] {test_name} complete')
    else:
        print(f'[ ERROR ] {test_name}')


def todolist_create_test():
    test_name = 'ToDoList Create Test'
    try:
        test_list = ToDoList([1,2,3])
    except ValueError:
        print(f'[ OK ] {test_name} complete')
    else:
        print(f'[ ERROR ] {test_name}')


def todolist_copy_test():
    test_name = 'ToDoList Copy Test'
    first_list = ToDoList([Item('First')])
    second_list = first_list.copy()
    if first_list is second_list:
        print(f'[ ERROR ] {test_name}')
    else:
        print(f'[ OK ] {test_name} complete')


def todolist_eq_test():
    test_name = 'ToDoList Equal and NotEqual Test'
    test_list_one = ToDoList([Item('First'), Item('Second')])
    test_list_two = test_list_one.copy()
    if not test_list_one == test_list_two:
        print(f'[ ERROR ] {test_name}')
        return

    test_list_two.add(Item('Third'))
    if not test_list_one != test_list_two:
        print(f'[ ERROR ] {test_name}')
        return

    try:
        result = not test_list_one == 5 and test_list_one != 5
    except AttributeError:
        print(f'[ ERROR ] {test_name}')
    else:
        print(f'[ OK ] {test_name} complete')


def todolist_add_test():
    test_name = 'ToDoList Add Test'
    test_list = ToDoList()
    try:
        test_list.add('test string')
    except ValueError:
        print(f'[ OK ] {test_name} complete')
    else:
        print(f'[ ERROR ] {test_name}')


if __name__ == '__main__':
    test_item_create()
    todolist_create_test()
    todolist_copy_test()
    todolist_eq_test()
    todolist_add_test()

