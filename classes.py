class onibus:
    def __init__(self):
        self.linha = input('A linha do ônibus: ')

    def __str__(self) -> str:
        return f'A linha do Ônibus é {self.linha}'

    def mudar_linha(self):
        self.linha = input('A nova linha do ônibus')

class fiscal:
    def __init__(self):
        self.nome = input('O nome do fiscal é: ')

    def __str__(self) -> str:
        return f'O nome do fiscal é {self.nome}'
    
    def mudar_fiscal(self):
        self.nome = input('O novo nome do fiscal')

class motorista:
    def __init__(self):
        self.nome = input('O nome do motorista é: ')


    def __str__(self) -> str:
        return f'O nome do motorista é {self.nome}'

    def mudar_motorista(self):
        self.nome = input('O novo nome do motorista')

class ponto:
    def __init__(self):
        self.nome = input('O nome da parada é: ')


    def __str__(self) -> str:
        return f'O nome da parada é {self.nome}'

    def mudar_ponto(self):
        self.nome = input('O novo nome do ponto')
