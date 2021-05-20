from Classes.Parser import Parser
from Classes.PrePro import PrePro
from Classes.Tokenizer import Tokenizer
from Classes.Token import Token
import sys

with open(sys.argv[1], 'r') as f:
    expression = f.read()

parser = Parser()
prepro = PrePro()

parser.tokenizer = Tokenizer(prepro.filter(expression), 0, Token('INIT', '-'))
parser.tokenizer.selectNext()

while parser.tokenizer.actual.tipo != "EOF":
    print(parser.tokenizer.tokenPosition, parser.tokenizer.actual.tipo, parser.tokenizer.actual.value)
    # print(parser.tokenizer.position, len(parser.tokenizer.origin))
    parser.tokenizer.selectNext()