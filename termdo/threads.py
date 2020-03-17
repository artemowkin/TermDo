import pickle

from threading import Thread, Lock


class SaveCheckThread(Thread):

    def __init__(self, todo_list, dbfilename):
        self.todo_list = todo_list
        self.dbfilename = dbfilename
        super().__init__(daemon=True)

    def run(self):
        older_todo = self.todo_list.copy()
        while True:
            if self.todo_list != older_todo:
                with open(self.dbfilename, 'wb') as f:
                    pickle.dump(self.todo_list, f)

                older_todo = self.todo_list.copy()

