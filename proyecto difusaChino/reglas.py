import jugada



class Reglas:

    def __init__(self, valores):
        self.response = []
        self.valores = valores

    def regla_1(self):
        if self.valores[0] < 0.6 and self.valores[3] < 0.8:
            return 5
        else:
            return 0

    def regla_2(self):
        if self.valores[0] < 0.4 and self.valores[7] < 0.2:
            return 3
        else:
            return 0

    def revisar(self):
        self.response.append(self.regla_1())
        self.response.append(self.regla_2())
        return self.response


