class Configuration:
    def __init__(self, s, i, a, b):
        self.s = s  # state of the parsing
        # (q - normal, b - back,f - final, e-error)
        self.i = i  # position of current symbol
        self.a = a  # working stack
        self.b = b  # input stack

    def is_head_nonterminal(self, fa):
        input_stack = self.b
        if len(input_stack) > 0:
            symbol = input_stack[0]
            if symbol in fa.alphabet:
                return True
        return False
