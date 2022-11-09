from symbol_table import SymbolTable

if __name__ == '__main__':
    ST_identifiers = SymbolTable(13)  # 13 is a prime number
    ST_constants = SymbolTable(13)

    ST_identifiers.add('a')
    ST_identifiers.add('test')
    ST_identifiers.add('x')
    print(ST_identifiers)
    print(ST_identifiers.get('test'))
    ST_identifiers.delete('test')
    print(ST_identifiers)
    print()

    ST_constants.add(1)
    ST_constants.add("This is a text")
    ST_constants.add(-5)
    print(ST_constants)
    print(ST_constants.get(-5))
    ST_constants.delete(-5)
    print(ST_constants)
