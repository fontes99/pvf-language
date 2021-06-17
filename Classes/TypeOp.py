from .Node import Node
from .ConsTable import consTable

class TypeOp(Node):

    def evaluate(self):

        consTable.setConsType(self.children[0], self.value, self.func)
