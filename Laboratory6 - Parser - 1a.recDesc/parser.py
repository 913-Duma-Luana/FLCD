from configuration import Configuration


class Parser:

    def __init__(self, grammar):
        self.config = Configuration('q', 1, 'epsilon', 'S')
        self.grammar = grammar
        self.another_try_index = 0
        # s = state of the parsing (q, b, f, e)

    def head(self, string):
        if len(string) == 0:
            return
        return string[0]

    def get_head(self):
        if ' ' in self.config.b:
            return self.config.b.split(' ')[0]
        return self.config.b

    def get_remaining(self):
        if ' ' in self.config.b:
            return self.config.b.split(' ', 1)[1]
        return ""

    def get_head_a(self):
        if ' ' in self.config.a:
            return self.config.a.split(' ')[-1]
        return self.config.a

    def get_remaining_a(self):
        if ' ' in self.config.a:
            items = self.config.a.split(' ')
            items.pop()
            string = ""
            for item in items:
                string += ' ' + item
            return string[1:]
        return ""

    def check_head(self, seq):
        index = self.config.i - 1
        items_list = seq.split(' ')
        if index >= len(items_list):
            return False
        if items_list[index] == self.get_head():
            return True
        return False

    def get_production(self, nt, idx):
        productions = self.grammar.prod_for_nonterminals(nt)
        if len(productions) == 0:
            return None
        string = ""
        for item in productions[idx][1]:
            string += ' ' + item
        return string[1:]

    def out_of_productions(self, nt, idx):
        productions = self.grammar.prod_for_nonterminals(nt)
        if idx == len(productions):
            return True
        return False

    def expand(self):
        # When the head of the input stack is a nonterminal
        print("expand |-- ", end='')
        if self.get_head() is None:
            print(self.config.b)
            return None
        if self.config.a == 'epsilon':
            self.config.a = self.get_head() + " 1"
        else:
            self.config.a += ' ' + self.get_head() + " 1"

        prod = self.get_production(self.get_head(), 0)
        if self.get_remaining() is None:
            if prod == 'epsilon':
                prod = ''
            self.config.b = prod
        elif prod == 'epsilon':
            self.config.b = self.get_remaining()
        else:
            self.config.b = prod + ' ' + self.get_remaining()
        print(self.config)

    def advance(self):
        print("advance |-- ", end='')
        if self.get_head() is None:
            return
        self.config.a += ' ' + self.get_head()

        if self.get_remaining() is None:
            self.config.b = ""
        else:
            self.config.b = self.get_remaining()

        self.config.i += 1
        print(self.config)

    def mom_insuccess(self):
        print("mom ins |-- ", end='')
        self.config.s = 'b'
        print(self.config)

    def back(self):
        print("back |-- ", end='')
        if self.get_head_a() is None:
            return
        self.config.b = self.get_head_a() + ' ' + self.config.b

        if self.get_remaining_a() is None:
            self.config.a = ""
        else:
            self.config.a = self.get_remaining_a()

        self.config.i -= 1
        print(self.config)

    def another_try(self):

        if self.config.i == 1 and len(self.config.a) == 0:
            self.config.s = 'e'
            return
        
        print("ant try |-- ", end='')
        index = int(self.get_head_a())

        self.config.a = self.get_remaining_a()
        nt = self.get_head_a()

        if self.out_of_productions(nt, index):
            self.config.a = self.get_remaining_a()
            self.config.b = nt + ' ' + self.get_remaining()
        else:
            prod = self.get_production(nt, index)
            prev_prod_nr_of_elements = 1
            if index > 0:
                prev_prod_nr_of_elements = self.get_production(nt, index - 1).count(' ') + 1
            print(prod, end=' -- ')
            for x in range(prev_prod_nr_of_elements):
                self.config.b = self.get_remaining()
            if prod != 'epsilon':
                self.config.b = prod + ' ' + self.config.b
            self.config.a += ' ' + str(index + 1)
            self.config.s = 'q'

        print(self.config)

    def success(self):
        print("success |-- ", end='')
        self.config.s = 'f'
        print(self.config)

    def algorithm(self, sequence):
        n = len(sequence.split(' '))
        print(self.config)
        while self.config.s != 'f' and self.config.s != 'e':
            if self.config.s == 'q':
                if self.config.i == n+1 and len(self.config.b) == 0:
                    self.success()
                elif self.config.is_head_nonterminal(self.grammar):  # head of the input stack is a nonterminal
                    self.expand()
                elif self.config.is_head_terminal(self.grammar) and self.check_head(sequence):  # head of input stack is a TERMINAL
                    self.advance()
                else:
                    self.mom_insuccess()  # head of stack is a terminal != a current symbol from input

            # back
            elif self.config.s == 'b':
                # print("head: " + self.get_head_a())
                # print("terminals: " + str(self.grammar.E))
                if self.get_head_a() in self.grammar.E:
                    self.back()
                else:
                    self.another_try()

        if self.config.s == 'e':
            return ''
        else:
            return self.build_string_of_productions()
        # build string of productions?

    def build_string_of_productions(self):
        items = self.config.a.split(' ')
        length = len(items)
        string = ""
        for i in range(length-1):
            if items[i] in self.grammar.N:
                string += items[i] + items[i+1] + ' '
                i += 1
        return string