import os

class Bar:
    def __init__(self):
        self.dir = os.getcwd()

    def print_dir(self):
        # print(self.dir)
        print('updated', self.dir)