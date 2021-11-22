from datetime import date, time, datetime, timedelta

class Empregado:
    '''
    Define a classe Empregado e seus métodos
    '''
    def __init__(self, nome, sobrenome, registro):
        '''
        Método de inicialização das propriedades da classe Empregado
        '''
        self.nome = nome
        self.sobrenome = sobrenome
        self.registro = str(registro)
        self.horario_entrada = None
        self.horario_saida = None
        self.almoco_start = None
        self.almoco_end = None
        self.no_trabalho = False
           
    def __repr__(self):
        '''
        Método de representação da classe Empregado
        '''
        return "Empregado:\nNome:'{}', Sobrenome: '{}', N° de Registro:'{}'".format(self.nome, self.sobrenome, self.registro)

    def __str__(self):
        '''
        Método para a representação por strings da classe empregado
        '''
        return ("{} - {} - {}".format(self.nome, self.sobrenome, self.registro))
        

    def bate_ponto(self):
        '''
        Método da classe que vai controlar e logar os horários de ponto do funcionário
        '''
        registro = int(input("Qual o resgitro que deseja fazer?\n (1) Entrada\n(2) Almoço (saída)\n(3) Almoço (volta)\n(4) Saída"))

        if registro == 1:
            self.no_trabalho = True
            self.horario_entrada = datetime.now()
            print(f"Bem-vindo {self.nome}!")
        elif registro == 2:
            self.no_trabalho = False
            self.almoco_start = datetime.now()
            print("Bom almoço.")
        elif registro == 3:
            self.no_trabalho = True
            self.almoco_end = datetime.now()
            duracao = self.almoco_end - self.almoco_start
            if (duracao == timedelta(hours=1)):
                print("Bem-vindo de volta.")
            elif (duracao < timedelta(hours=1)):
                print("Fique atento aos seus horários.\nO RH será notificado!")
            else:
                print("Almoços longo, né? Será nosso segredo. ;)")
        elif registro == 4:
            self.no_trabalho = False
            self.horario_saida = datetime.now()
            print(f"Até amanhã, {self.nome}.")
        else:
            print("Entrada inválida. tente novamente: ")
