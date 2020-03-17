import pickle
import os

from termdo.objects import Item, ToDoList
from termdo.threads import SaveCheckThread

DB_FILE_NAME = 'todo.db'


def add_item(todo_list):
    title = input("Title => ")
    new_item = Item(title)
    todo_list.add(new_item)


def all_items(todo_list):
    print('\n' + todo_list.as_str() + '\n')


def get_item(todo_list):
    try:
        id = int(input("ID => "))
        item = todo_list.get(id)
    except IndexError as err:
        print(err.args[0])
    except ValueError as err:
        print(err.args[0])
    else:
        print('\n' + str(item) + '\n')


def delete_item(todo_list):
    try:
        id = int(input("ID => "))
        item = todo_list.delete(id)
    except IndexError as err:
        print(err.args[0])
    except ValueError as err:
        print(err.args[0])


def change_item(todo_list):
    try:
        id = int(input("ID => "))
        new_title = input("New title => ")
        todo_list.change(id, new_title)
    except IndexError as err:
        print(err.args[0])
    except ValueError as err:
        print(err.args[0])


def clear_list(todo_list):
    todo_list.clear()


def exit(thread):
    thread._stop()


def get_help():
    print("\n\tadd => add new item with given title\n"
          "\tall => get all items in todo list\n"
          "\tget => get item with given id\n"
          "\tdelete => delete item with given id\n"
          "\tchange => change item with given id\n"
          "\tclear => delete all items in todo list\n"
          "\texit => exit from this program\n"
          "\thelp => this help\n")


def run():
    print("Type 'help' to see help information\n")
    cmd_dict = {
        'add': add_item,
        'all': all_items,
        'get': get_item,
        'delete': delete_item,
        'change': change_item,
        'clear': clear_list,
        'help': get_help,
    }

    if os.path.exists(DB_FILE_NAME):
        with open(DB_FILE_NAME, 'rb') as f:
            todo_list = pickle.load(f)
    else:
        todo_list = ToDoList()

    SaveCheckThread(todo_list, DB_FILE_NAME).start()

    while True:
        command = input("Give me a command => ").lower()
        if not command:
            continue
        elif command == 'exit':
            break
        elif command not in cmd_dict:
            print("WTF?")
        elif command == 'help':
            cmd_dict['help']()
        else:
            cmd_dict[command](todo_list)


if __name__ == '__main__':
    run()

