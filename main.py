# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from hash_map import HashMap

# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    ST_identifiers = HashMap(13)  # 13 is a prime number
    ST_constants = HashMap(13)

    ST_identifiers.set_val('a', 'a')
    ST_identifiers.set_val('test', 'test')
    ST_identifiers.set_val('x', 'x')
    print(ST_identifiers)
    print(ST_identifiers.get_val('test'))
    ST_identifiers.delete_val('test')
    print(ST_identifiers)
    print()

    ST_constants.set_val(1, 1)
    ST_constants.set_val("This is a text", 'This is a text')
    ST_constants.set_val(-5, -5)
    print(ST_constants)
    print(ST_constants.get_val(-5))
    ST_constants.delete_val(-5)
    print(ST_constants)
