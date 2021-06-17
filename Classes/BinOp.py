from .Node import Node
from .ConsTable import consTable

class BinOp(Node):

    def evaluate(self):

        if self.value != 'atrib' and self.value != 'while':
            if (type(self.children[0].evaluate()) == str and type(self.children[1].evaluate()) != str) or (type(self.children[0].evaluate()) != str and type(self.children[1].evaluate()) == str) : raise ValueError(f"Invalid operation between {type(self.children[0].evaluate())} and {type(self.children[1].evaluate())}")

        if self.value == 'SUM':
            return self.children[0].evaluate() + self.children[1].evaluate()

        if self.value == 'SUB':
            return self.children[0].evaluate() - self.children[1].evaluate()
        
        if self.value == 'MULT':
            return self.children[0].evaluate() * self.children[1].evaluate()
        
        if self.value == 'DIV':
            return int(self.children[0].evaluate() / self.children[1].evaluate())
        
        if self.value == 'EQL':
            return self.children[0].evaluate() == self.children[1].evaluate()

        if self.value == 'AND':
            return bool(self.children[0].evaluate() and self.children[1].evaluate())

        if self.value == 'OR':
            return self.children[0].evaluate() or self.children[1].evaluate()

        if self.value == 'GRT':
            return self.children[0].evaluate() > self.children[1].evaluate()

        if self.value == 'LSS':
            return self.children[0].evaluate() < self.children[1].evaluate()

        if self.value == 'atrib':
            consTable.setConsValue(self.children[0], self.children[1].evaluate(), self.func)

        if self.value == 'whilo':
            while  self.children[0].evaluate():
                x = self.children[1].evaluate()
                if x == 'break' : break
                