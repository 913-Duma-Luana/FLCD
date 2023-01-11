from grammar import Grammar
from parser import Parser

grammar1 = Grammar("grammar1.txt")
grammar2 = Grammar("grammar2.txt")

parser1 = Parser(grammar1)
parser2 = Parser(grammar2)

parser1.add_productions_to_file("( int + int )")
parser2.add_productions_to_file("< and or and >")

# print()
parser1.run_tests()
