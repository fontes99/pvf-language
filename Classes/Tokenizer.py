from .Token import Token

class Tokenizer:

    def __init__(self, origin, position, actual):
        self.origin = origin
        self.position = position
        self.actual = actual
        self.balance_paren = 0
        self.balance_brace = 0
        self.builtIns = ["printo", "reado", "ifo", "whilo", "elso", "returno"]
        self.types = ["int", "bool", "string"]
        self.tokenPosition = 0

    def selectNext(self):

        self.tokenPosition += 1
        
        def next_():
            self.position += 1

        char = lambda : self.origin[self.position]

        while self.position < len(self.origin) and (char() == ' ' or char() == '\n' or char() == '\t'):
            next_()

        if self.position == len(self.origin):
            self.actual = Token('EOF', '"')
            if self.balance_paren != 0: raise ValueError("Error in balancing '(' and ')'")
            if self.balance_brace != 0: raise ValueError("Error in balancing '{' and '}'")
            return

        elif char() == ',':
            self.actual = Token('SEP', char())
            next_()

        elif char() == '/':
            self.actual = Token('DIV', char())
            next_()

        elif char() == '*':
            self.actual = Token('MULT', char())
            next_()
        
        elif char() == '+':
            self.actual = Token('SUM', 1)
            next_()

        elif char() == '-':
            self.actual = Token('SUB', -1)
            next_()
        
        elif char() == '>':
            self.actual = Token('GRT', '>')
            next_()
                    
        elif char() == '<':
            self.actual = Token('LSS', '<')
            next_()

        elif char() == '!':
            self.actual = Token('NEG', '!')
            next_()

        elif char() == '&':
            next_()
            if char() != '&' : raise ValueError("Syntax error: &&")
            else: self.actual = Token('AND', '&&')
            next_()

        elif char() == '|':
            next_()
            if char() != '|' : raise ValueError("Syntax error: ||")
            else: self.actual = Token('OR', '||')
            next_()
        
        elif char() == '(':
            self.actual = Token('OPN', '(')
            self.balance_paren += 1
            next_()

        elif char() == ')':
            self.actual = Token('CLS', ')')
            self.balance_paren -= 1
            next_()

            if self.balance_paren < 0:
                raise ValueError

        elif char() == '{':
            self.actual = Token('BEG', '{')
            self.balance_brace += 1
            next_()

        elif char() == '}':
            self.actual = Token('END', '}')
            self.balance_brace -= 1
            next_()

            if self.balance_brace < 0:
                raise ValueError("Error in balancing '{' and '}'")

        elif char().isalpha():
            name = char()
            next_()
            while char().isalpha() or char().isnumeric() or char() == "_":
                name += char()
                next_()

            if name in self.builtIns: self.actual = Token('builtin', name)
            
            elif name in self.types: self.actual = Token('TYP', name)

            elif name == "true": self.actual = Token('BOOL', 1)

            elif name == "false": self.actual = Token('BOOL', 0)

            else : self.actual = Token('cons', name)

        elif char() == "=":
            next_()
            if char() != "=":
                self.actual = Token('atrib', '=')
            else:
                self.actual = Token('EQL', '==')
                next_()

        elif char() == ";":
            
            if self.balance_paren != 0:
                raise ValueError("Error in balancing '(' and ')'")
            
            self.actual = Token('end_line', ";")
            next_()

        elif char() == '"':
            next_()
            string = char()
            next_()

            while char() != '"':
                string += char()
                next_()

            self.actual = Token("STR", string)
            next_()

        else: 
            if self.position > 0 and self.actual.tipo == 'INT': raise ValueError("Can't have two INTs in a row")

            val = ""

            while(self.position < len(self.origin) and char().isnumeric()):
                val += char()
                next_()

            self.actual = Token('INT', int(val))