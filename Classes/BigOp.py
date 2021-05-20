from .Node import Node

class BigOp(Node):

    def evaluate(self):
        for i in self.children:
            i.evaluate()