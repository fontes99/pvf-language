from .Node import Node
from .ConsTable import consTable

class FuncOp(Node):

    def evaluate(self):

        if self.value == 'def':
            return

        elif self.value == 'call':
            consTable.runFunc(self.children[1])
            if (type(consTable.return_["value"]) != consTable.return_["type"]) and (self.children[2] == 'factor') : raise ValueError(f"Invalid return {type(consTable.return_['value'])} for return type {consTable.return_['type']}")
            return consTable.return_["value"]

        elif self.value == 'param': 
            for i in range(len(self.children[0])):
                consTable.setConsValue(consTable.getParams(self.children[1])[i], self.children[0][i].evaluate(), self.func)

            consTable.runFunc(self.children[1])
            if (type(consTable.return_["value"]) != consTable.return_["type"]) and (self.children[2] == 'factor') : raise ValueError(f"Invalid return {type(consTable.return_['value'])} for return type {consTable.return_['type']}")
            return consTable.return_["value"]