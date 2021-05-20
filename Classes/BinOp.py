from .Node import Node
from .ConsTable import consTable

class BinOp(Node):

    def evaluate(self):


        if self.value == 'SUM':
            if type(self.children[0].evaluate()) != type(self.children[1].evaluate()) : raise ValueError(f"Invalid operation between {type(self.children[0].evaluate())} and {type(self.children[1].evaluate())}")
            return self.children[0].evaluate() + self.children[1].evaluate()

        if self.value == 'SUB':
            if type(self.children[0].evaluate()) != type(self.children[1].evaluate()) : raise ValueError(f"Invalid operation between {type(self.children[0].evaluate())} and {type(self.children[1].evaluate())}")
            return self.children[0].evaluate() - self.children[1].evaluate()
        
        if self.value == 'MULT':
            if type(self.children[0].evaluate()) != type(self.children[1].evaluate()) : raise ValueError(f"Invalid operation between {type(self.children[0].evaluate())} and {type(self.children[1].evaluate())}")
            return self.children[0].evaluate() * self.children[1].evaluate()
        
        if self.value == 'DIV':
            if type(self.children[0].evaluate()) != type(self.children[1].evaluate()) : raise ValueError(f"Invalid operation between {type(self.children[0].evaluate())} and {type(self.children[1].evaluate())}")
            return int(self.children[0].evaluate() / self.children[1].evaluate())
        
        if self.value == 'EQL':
            if type(self.children[0].evaluate()) != type(self.children[1].evaluate()) : raise ValueError(f"Invalid operation between {type(self.children[0].evaluate())} and {type(self.children[1].evaluate())}")
            return self.children[0].evaluate() == self.children[1].evaluate()

        if self.value == 'AND':
            if type(self.children[0].evaluate()) != type(self.children[1].evaluate()) : raise ValueError(f"Invalid operation between {type(self.children[0].evaluate())} and {type(self.children[1].evaluate())}")
            return self.children[0].evaluate() and self.children[1].evaluate()

        if self.value == 'OR':
            if type(self.children[0].evaluate()) != type(self.children[1].evaluate()) : raise ValueError(f"Invalid operation between {type(self.children[0].evaluate())} and {type(self.children[1].evaluate())}")
            return self.children[0].evaluate() or self.children[1].evaluate()

        if self.value == 'GRT':
            if type(self.children[0].evaluate()) != type(self.children[1].evaluate()) : raise ValueError(f"Invalid operation between {type(self.children[0].evaluate())} and {type(self.children[1].evaluate())}")
            return self.children[0].evaluate() > self.children[1].evaluate()

        if self.value == 'LSS':
            if type(self.children[0].evaluate()) != type(self.children[1].evaluate()) : raise ValueError(f"Invalid operation between {type(self.children[0].evaluate())} and {type(self.children[1].evaluate())}")
            return self.children[0].evaluate() < self.children[1].evaluate()

        if self.value == 'atrib':
            consTable.setConsValue(self.children[0], self.children[1].evaluate())

        if self.value == 'whilo':
            while  self.children[0].evaluate():
                 self.children[1].evaluate()