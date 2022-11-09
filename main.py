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

    # with open(fileName, encoding="utf8") as file:
    #     idx = 0
    #     for line in file:
    #         print("Line " + str(idx) + ":")
    #         idx += 1
    #         print([token for token in tokenGenerator(line, separators)])

    symbolTable = SymbolTable(97)
    pif = PIF()

    with open(fileName, encoding="utf8") as file:
        line_number = 0
        comment = False
        for line in file:
            line_number += 1
            was_last_token_identifier = False
            for token in tokenGenerator(line[0:-1], separators):
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
                elif isIdentifier(token):
                    if was_last_token_identifier:
                        raise Exception("Syntax error at line " + str(line_number) + ": 2 constants cannot be one right after another.")
                    id = symbolTable.add(token)
                    # print(codification['identifier'])
                    pif.add(codification['identifier'], id)
                    was_last_token_identifier = True
                elif isConstant(token):
                    id = symbolTable.add(token)
                    # print(codification['constant'])
                    pif.add(codification['constant'], id)
                    was_last_token_identifier = False
                else:
                    raise Exception('Unknown token ' + token + ' at line ' + str(line_number))

    print('Program Internal Form: \n', pif.stringWithNames())
    print('Symbol Table: \n', symbolTable.stringTableLook())
