from FiniteAutomata import FiniteAutomata
from grammar import Grammar
from parser import Parser

grammar = Grammar("grammar1.txt")

parser = Parser(grammar)

string_of_prod = parser.algorithm("( int + int )")
if string_of_prod != '':
    print("Sequence accepted")
    print("String of productions: ", end='')
    print(string_of_prod)
else:
    print("Sequence not accepted")
