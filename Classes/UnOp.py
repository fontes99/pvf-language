from Classes.ConsTable import consTable
from .Node import Node

class UnOp(Node):

    def evaluate(self):

        if self.value == 'SUM':
            return self.children[0].evaluate()

        elif self.value == 'SUB':
            return -self.children[0].evaluate()

        elif self.value == 'NEG':
            return not self.children[0].evaluate()

        elif self.value == 'printo':
            print(self.children[0].evaluate())
        
        elif self.value == 'returno':
            consTable.return_["type"] = consTable.table_func[self.func]['return_type']
            consTable.return_["value"] = self.children[0].evaluate()