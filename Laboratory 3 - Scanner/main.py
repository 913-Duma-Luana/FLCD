from pif import PIF
from scanner import *
from specification import *
from symbol_table import SymbolTable

if __name__ == '__main__':
    fileName = input("Insert file name: ")
    try:
        file = open(fileName, encoding="utf8")
        print("\nINPUT FILE CONTENT")
        for line in file:
            print(line, end="")
        print()
    except:
        print("The file could not be read.")
        exit(1)

    symbolTable = SymbolTable(97)
    pif = PIF()

    with open(fileName, encoding="utf8") as file:
        line_number = 0
        comment = False
        for line in file:
            line_number += 1
            for token in separate_into_tokens(line[0:-1], separators):
                if token == comment_start:
                    comment = True
                    continue
                if comment:
                    if token == comment_end:
                        comment = False
                    continue
                if token in white_space_separators:
                    pif.add(codification[token], -1)
                elif token in separators + operators + reservedWords:
                    pif.add(codification[token], -1)
                    was_last_token_identifier = False
                elif is_identifier(token):
                    if was_last_token_identifier:
                        raise Exception("Lexical error at line " + str(line_number)
                                        + ": 2 identifiers cannot be one right after another.")
                    id = symbolTable.add(token)
                    # print(codification['identifier'])
                    pif.add(codification['identifier'], id)
                    was_last_token_identifier = True
                elif is_constant(token):
                    id = symbolTable.add(token)
                    # print(codification['constant'])
                    pif.add(codification['constant'], id)
                    was_last_token_identifier = False
                else:
                    raise Exception('Unknown token ' + token + ' at line ' + str(line_number))

    print('Program Internal Form: \n', pif.stringWithNames())
    print('Symbol Table: \n', symbolTable.stringTableLook())

    with open("PIF.txt", "w") as file:
        file.write(str(pif))

    with open("ST.txt", "w") as file:
        file.write(str(symbolTable))
