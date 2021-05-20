from Classes.Parser import Parser
from Classes.PrePro import PrePro
import sys

with open(sys.argv[1], 'r') as f:
    expression = f.read()

parser = Parser()
prepro = PrePro()

parser.run(prepro.filter(expression))