from .Node import Node
from .ConsTable import consTable

class VarOp(Node):

    def evaluate(self):
        if self.value == 'constant':
            return consTable.getConsValue(self.children[0], self.func)