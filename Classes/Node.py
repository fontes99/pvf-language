class Node:
    def __init__(self, value, func, children:list):
        self.value = value
        self.func = func
        self.children = children

    def evaluate(self):
        pass