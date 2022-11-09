from specification import *

class PIF:
    def __init__(self):
        self.__content = []

    def add(self, code, id):
        self.__content.append((code, id))

    def __str__(self):
        final_str = ""
        for item in self.__content:
            final_str += str(item[0]) + " : " + str(item[1]) + "\n"
        return final_str

    def stringWithNames(self):
        final_str = ""
        for item in self.__content:
            final_str += str(item[0]) + " : " + str(item[1]) + "\n"
        return final_str

