class ConsTable:

    def __init__(self, table):
        self.table = table
        self.tipinhos = ["int", "bool", "string"]

    def setCons(self, cons):
        self.table[cons] = {'value' : None, 'type' : None}


    def getConsValue(self, cons):
        return self.table[cons]['value']

    def getConsType(self, cons):
        return self.table[cons]['type']

    def setConsValue(self, cons, value):

        if (type(value) == str and self.getConsType(cons) != 'string') or (type(value) == int and self.getConsType(cons) != 'int') or (type(value) == bool and self.getConsType(cons) != 'bool'):
            raise ValueError(f"Invalid operation for type {self.getConsType(cons)}")

        try:
            self.table[cons]['value'] = value
        except:
            raise ValueError(f"Constant {cons} not assigned")
    
    def setConsType(self, cons, tipo):
        self.setCons(cons)
        self.table[cons]['type'] = tipo

    def getTable(self):
        return self.table


global consTable 
consTable = ConsTable({})