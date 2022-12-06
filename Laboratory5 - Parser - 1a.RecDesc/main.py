from grammar import Grammar

grammar = Grammar("my_grammar.txt")
grammar.print_nonterminals()
grammar.print_terminals()
grammar.print_productions()
grammar.print_productions_for_nonterminal('iostmt')
