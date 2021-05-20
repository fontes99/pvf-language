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