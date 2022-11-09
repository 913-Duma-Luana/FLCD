from specification import *

class PIF:
    def __init__(self):
        self.__content = {}

    def add(self, code, id):
        self.__content[code] = id

    def __str__(self):
        return str(self.__content).replace('{', '').replace('}', '').replace(',', '\n')

    def stringWithNames(self):
        final_str = ""
        for key in self.__content:
            value = {i for i in codification if codification[i]==key}
            final_str += str(key) + ":" + str(self.__content[key]) + " --> " + str(value) + '\n'
        return final_str

