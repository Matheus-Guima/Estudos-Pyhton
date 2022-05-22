from abc import ABC   #Abstract Base Classes

from collections.abc import Sized

class MinhaListagem(Sized):
    def __init__(self, descricao):
        self.descricao = descricao

    def __len__(self):
        return len(self.descricao)

    def __str__(self):
        return f" A descrição do bagulhete é {self.descricao}"

blabla = MinhaListagem("amarelo")

print(blabla)
print(len(blabla))