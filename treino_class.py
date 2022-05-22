class Funcionario:
    def __init__(self, nome, matricula):
        self.nome = nome
        self._matricula = matricula


class Mc_donalds(Funcionario):
    def __init__(self, nome, matricula, mes_de_entrada):
        super().__init__(nome, matricula)
        self.mes_de_entrada = mes_de_entrada

    def __str__(self):
        return f'Eu sou funcinário do Mc Donalds, meu nome é {self.nome}, entrei no mês {self.mes_de_entrada}'

class Bk(Funcionario):
    def imprime_algo(self):
        print(f"blblabla {self.nome}")

    def __str__(self):
        return f'Eu sou funcionário do Burguer King, meu nome é {self.nome}'

class Junior(Mc_donalds):
    pass

class Pleno(Bk):
    pass

class Senior(Mc_donalds, Bk): #Herança Multipla
    pass

xexa = Junior("Bochecha", 2424, "Janeiro")
#print(xexa)

thales = Pleno("Thales", 2525)
#print(thales)

mauricio = Senior("Mauricio", 2222, "Maio")

pessoas = [xexa, thales, mauricio]
for funcio_equipes in pessoas:
    print(funcio_equipes)
