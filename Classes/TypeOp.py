from .Node import Node
from .ConsTable import consTable

class TypeOp(Node):

    def evaluate(self):

        if self.value == 'int':
            consTable.setConsType(self.children[0], 'int')
        
        if self.value == 'bool':
            consTable.setConsType(self.children[0], 'bool')
        
        if self.value == 'string':
            consTable.setConsType(self.children[0], 'string')
