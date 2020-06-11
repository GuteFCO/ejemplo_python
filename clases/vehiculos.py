class Vehiculo:
    def __init__(self, num_ruedas):
        self.num_ruedas = num_ruedas

    def print_num_ruedas(self):
        print(self.num_ruedas)


class Moto(Vehiculo):
    def __init__(self):
        Vehiculo.__init__(self, 2)
