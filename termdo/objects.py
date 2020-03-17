from datetime import datetime


class Item:

    def __init__(self, title):
        self.title = title
        self.pub_date = datetime.now().date()

    def __str__(self):
        return f'\t> {self.title} ({self.pub_date})'

    def __repr__(self):
        return f'<Item: {self.title} ({self.pub_date})>'


class ToDoList:

    def __init__(self, todo_list=[]):
        for item in todo_list:
            self._check_item_class(item)

        self.todo_list = todo_list

    def __repr__(self):
        return f'<ToDoList: {self.todo_list}>'

    def __eq__(self, other):
        try:
            return self.todo_list == other.todo_list
        except AttributeError:
            return False

    def __ne__(self, other):
        try:
            return self.todo_list != other.todo_list
        except AttributeError:
            return True

    def copy(self):
        return ToDoList(self.todo_list.copy())

    def add(self, item):
        self._check_item_class(item)
        self.todo_list.append(item)

    def delete(self, id):
        self._check_id(id)
        self.todo_list.pop(id-1)

    def change(self, id, new_title):
        self._check_id(id)
        self.todo_list[id-1] = Item(new_title)

    def clear(self):
        self.todo_list.clear()

    def as_str(self):
        string = '\t> %d) %s (%s)'
        all_items = [
            string % (id+1, item.title, item.pub_date)
            for id, item in enumerate(self.todo_list)
        ]
        return '\n'.join(all_items)

    def get(self, id):
        self._check_id(id)
        return self.todo_list[id-1]

    def _check_id(self, id):
        if id < 1 or id > len(self.todo_list):
            raise IndexError("ID can't be lower then 1 and biggest "
                             "then list length")

    def _check_item_class(self, item):
        if not isinstance(item, Item):
            raise ValueError('Item can only "Item" instance')

