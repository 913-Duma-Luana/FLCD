white_space_separators = ['\t', ' ', '\n']
comment_start = "/*"
comment_end = "*/"
separators = ['\t', ' ', '\n', '[', ']', '{', '}', '(', ')', ';', ':']
operators = ['+', '-', '*', '/', '%', '<', '<=', '=', '>=', '>',
             '>>', '<<', '==', '&&', '||', '!', '!=', '&', '~',
             '|', '^', '++', '--', ',', '.', '/*', '*/']
reservedWords = ['function', 'read', 'write', 'return', 'input',
                 'number', 'if', 'while', 'for', 'break',
                 'array', 'append', 'remove', 'length']

everything = separators + operators + reservedWords
codification = dict([(everything[i], i + 2) for i in range(len(everything))])
codification['identifier'] = 0
codification['constant'] = 1