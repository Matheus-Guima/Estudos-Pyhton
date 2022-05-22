class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def registra_horas(self, horas):
        print(f"{horas} Horas registradas")

    def mostra_tarefas(self):
        print("Fez muita coisa")


class Caelum(Funcionario):
    def mostra_tarefas(self):
        print("Fez muita coisa, CAelumer")

    def busca_cursos_do_mes(self, mes=None):
        print(f"mostra cursos {mes}" if mes else "mostra cursos desse mês")


class Alura(Funcionario):
    def mostra_tarefas(self):
        print("Fez muita coisa, Alurete!")

    def busca_perguntas_sem_respostas(self):
        print("Mostra erguntas não respondidas de fórum")

class Hipster:  #MIXIN - CLASSES PEQUENAS - COMPARTILHAMENTO DE UM COMPORTAMENTO
    def __str__(self):
        return f"Hipster, {self.nome}"

class Junior(Alura):
    pass

class Pleno(Alura, Caelum):
    pass

class Senior(Alura, Caelum, Hipster):
    pass


jose = Junior("Junior")
jose.busca_perguntas_sem_respostas()

laun = Pleno("Luan")
laun.busca_perguntas_sem_respostas()
laun.busca_cursos_do_mes("Janeiro")

laun.mostra_tarefas()  #Procura penlo > Alura > Funcionario > Caelum > Funcionario   // MRO


mario = Senior("Mario")
print(mario)

