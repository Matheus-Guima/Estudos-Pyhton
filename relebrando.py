
class Programa:
    def __init__(self, nome, ano):
        self._nome = nome
        self._ano = ano
        self._like = 0

    @property
    def mostra_ano(self):
        return self._ano

    @property
    def nome(self):
        return self._nome.title()

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome


    def dar_like(self):
        self._like += 1

    @property
    def like(self):
        return self._like

    def __str__(self):
        return f"{self.nome} - {self._ano} - Likes: {self.like}"


class Filme(Programa):
    def __init__(self, nome, ano, tempo_de_filme):
        super().__init__(nome, ano)
        self._tempo_de_filme = tempo_de_filme

    # @property
    # def retorna_tempo_do_filme(self):
    #     return self._tempo_de_filme

    def __str__(self):
        return f"{self.nome} - {self._ano} - {self._tempo_de_filme} - Likes: {self.like}"



class Serie(Programa):
    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self._temporada = temporada

    @property
    def retorna_temporada(self):
        return self._temporada

    def __str__(self):
        return f"{self.nome} - {self._ano} - {self._temporada} - Likes: {self.like}"




class PLaylist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item): #Torna Iterável
        return self._programas[item] #Repassando um item para lista de programas interna

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)


vingadores = Filme("Vingadores", 2020, "3 horas de filme")
bob_esponja = Serie("bob esponja", 1990, "10 temporadas")
td_mundo_em_panico = Filme("Todo mundo em Pânico", 1990, "2h de filme")
demolidor = Serie("Demolidor", 2018, "3 temporadas")

bob_esponja.dar_like()
bob_esponja.dar_like()
demolidor.dar_like()


filmes_e_serie = [vingadores, bob_esponja, demolidor, td_mundo_em_panico]

play_list_fim_de_semana = PLaylist("Fim de Semana", filmes_e_serie)

print(f"Tamanho da playlist: {len(play_list_fim_de_semana)} Filmes/ Séries")

for programa in play_list_fim_de_semana:
    print(programa)




