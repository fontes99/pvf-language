from .Tokenizer import Tokenizer
from .Token import Token
from .TriOp import TriOp
from .BinOp import BinOp
from .VarOp import VarOp
from .BigOp import BigOp
from .TypeOp import TypeOp
from .UnOp import UnOp
from .IntVal import IntVal
from .StringVal import StringVal
from .NoOp import NoOp

class Parser:

    def __init__(self):
        self.tokenizer = None
        self.token_tipo = lambda : self.tokenizer.actual.tipo
        self.token_valor = lambda : self.tokenizer.actual.value


    def parseFactor(self):
        self.tokenizer.selectNext()

        if self.token_tipo() == 'INT':
            tmp = IntVal(self.token_valor(), [])
            self.tokenizer.selectNext()
            return tmp

        elif self.token_tipo() == 'STR':
            tmp = StringVal(self.token_valor(), [])
            self.tokenizer.selectNext()
            return tmp

        elif self.token_tipo() == 'SUM' or self.token_tipo() == 'SUB' or self.token_tipo() == 'NEG':
            tmp = self.token_tipo()
            return UnOp(tmp, [self.parseFactor()]) 

        elif self.token_tipo() == 'OPN':

            tmp = self.OREXPR()
            self.tokenizer.selectNext()
            
            return tmp

        elif self.token_tipo() == 'cons':
            tmp = VarOp(self.token_valor(), [])
            self.tokenizer.selectNext()
            return tmp

        elif self.token_valor() == "readln":
            self.tokenizer.selectNext()

            if self.token_tipo() != "OPN" : raise ValueError("sem ( depois de readln")
            self.tokenizer.selectNext()
            
            tmp = IntVal(int(input()), [])
            self.tokenizer.selectNext()
            return tmp

        else:
            raise ValueError(f'{self.token_tipo()}')


    def parseTerm(self):

        res = self.parseFactor()

        while self.token_tipo() == 'DIV' or self.token_tipo() == 'MULT':
            
            if self.token_tipo() == 'DIV' or self.token_tipo() == 'MULT':
                res = BinOp(self.token_tipo(), [res, self.parseFactor()])
            
            else: raise ValueError('not DIV or MULT')
            
        return res



    def parseExpression(self):

        res = self.parseTerm()

        while self.token_tipo() == 'SUM' or self.token_tipo() == 'SUB':
            
            if self.token_tipo() == 'SUM' or self.token_tipo() == 'SUB':
                res = BinOp(self.token_tipo(), [res, self.parseTerm()])

            else: raise ValueError('not SUM or SUB')
            
        return res


    def RELEXPR(self):

        res = self.parseExpression()

        while self.token_tipo() == 'GRT' or self.token_tipo() == 'LSS':
            
            if self.token_tipo() == 'GRT' or self.token_tipo() == 'LSS':
                res = BinOp(self.token_tipo(), [res, self.parseTerm()])

            else: raise ValueError('not GRT or LSS')
            
        return res


    def EQEXPR(self):

        res = self.RELEXPR()

        while self.token_tipo() == 'EQL':
            
            if self.token_tipo() == 'EQL':
                res = BinOp(self.token_tipo(), [res, self.parseTerm()])

            else: raise ValueError('not EQL')
            
        return res


    def ANDEXPR(self):

        res = self.EQEXPR()

        while self.token_tipo() == 'AND':
            
            if self.token_tipo() == 'AND':
                res = BinOp(self.token_tipo(), [res, self.parseTerm()])

            else: raise ValueError('not AND')
            
        return res


    def OREXPR(self):

        res = self.ANDEXPR()

        while self.token_tipo() == 'OR':
            
            if self.token_tipo() == 'OR':
                res = BinOp(self.token_tipo(), [res, self.parseTerm()])

            else: raise ValueError('not OR')
            
        return res


    def println(self):
        print_valor = self.token_valor()
        self.tokenizer.selectNext()

        if self.token_tipo() != 'OPN' : raise ValueError('não abriu parenteses no println')

        tree = self.OREXPR()
        self.tokenizer.selectNext()

        return UnOp(print_valor, [tree])

    def identifier(self):
        cons_name = self.token_valor()

        self.tokenizer.selectNext()

        if self.token_tipo() != 'atrib' : raise ValueError(f'não tem = depois de variavel {cons_name}')

        tree = self.OREXPR()

        return BinOp('atrib', [str(cons_name), tree])

    def Typing(self):
        tmp = self.token_valor()

        self.tokenizer.selectNext()
        if self.token_tipo() != 'cons' : raise ValueError(f"Invalid constant name {self.token_valor()}")

        return TypeOp(tmp, [self.token_valor()])

    def ifEXPR(self):
        self.tokenizer.selectNext()
        if self.token_tipo() != 'OPN' : raise ValueError('não abriu parenteses no if')

        condition = self.OREXPR()
        self.tokenizer.selectNext()

        iftrue = self.command()

        if self.token_valor() == 'elso':
            self.tokenizer.selectNext()
            elsee = self.command()

        elif self.token_tipo() == 'END':
            elsee = NoOp('nop', [])

        else: 
            elsee = self.command()
        
        return TriOp('ifo', [condition, iftrue, elsee])

    def whileEXPR(self):
        self.tokenizer.selectNext()
        if self.token_tipo() != 'OPN' : raise ValueError('não abriu parenteses no while')

        condition = self.OREXPR()
        self.tokenizer.selectNext()

        instru = self.command()

        return BinOp('whilo', [condition, instru])
        

    def command(self):

        if self.token_tipo() == 'builtin':

            if self.token_valor() == 'printo':
                tree = self.println()
                
                if self.token_tipo() != 'end_line' : raise ValueError('não tem ;')
                self.tokenizer.selectNext()
                
                return tree

            elif self.token_valor() == 'ifo':
                return self.ifEXPR()

            elif self.token_valor() == 'whilo':
                return self.whileEXPR()

            else : raise ValueError(f"builtin {self.token_valor()} not valid")

        elif self.token_tipo() == 'cons':
            tree = self.identifier()

            if self.token_tipo() != 'end_line' : raise ValueError('não tem ;')
            self.tokenizer.selectNext()
           
            return tree

        elif self.token_tipo() == 'TYP':
            tree = self.Typing()

            self.tokenizer.selectNext()
            if self.token_tipo() != 'end_line' : raise ValueError('não tem ;')
            self.tokenizer.selectNext()
           
            return tree

        elif self.token_tipo() == 'end_line':
            self.tokenizer.selectNext()
            return NoOp('pass', [])

        elif self.token_tipo() == 'BEG':
            return self.block()
        
        else : raise ValueError(f"Syntax error : {self.token_tipo()} token {self.tokenizer.tokenPosition}")


    def block(self):
        if self.token_tipo() != 'BEG' : raise ValueError('bloco não começa com {')
        self.tokenizer.selectNext()

        commands_in_block = []

        while self.token_tipo() != 'END':
            commands_in_block.append(self.command())
        
        self.tokenizer.selectNext()
        return BigOp('block', commands_in_block)


    def run(self, code):
        self.tokenizer = Tokenizer(code, 0, Token('INIT', '-'))
        self.tokenizer.selectNext()

        compiled = self.block()
        compiled.evaluate()

