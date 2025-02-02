#import os.system("cls") from os (pra apagar os coisa deipóis kkkkk)
#ver dicinarios e torcer para mudar tudo a tempo

import Funções

class Funcionários():
    def __init__(self):
        self.informações = Informação()
        self.avaliação = Avaliação()
        self.pagamento = Pagamento()
        self.anterior_funcionário = None
        self.proximo_funcionário = None

class Informação():
    def __init__(self):
        self.nome = None
        self.idade = None
        self.cargo = None
        self.salario_total = None
        self.horarios = None
        self.status = None

class Avaliação():
    def __init__(self):
        self.nota = None
        self.descrição = None
        self.faltas = None

class Pagamento():
    def __init__(self):
        self.salario_base = None
        self.beneficios = None
        self.descontos = None

print("Olá seja bem vindo ao gerenciador de RH\n")
lista_de_funcionários = None
while (1):
    choice_1 = (input("""
Selecione a opção que desejar:
Visualizar opções(0)\n\n"""))
    match choice_1:
        case '0':
            print("""
Visualizar sobre Funcionários(1)
Visualizar Sobre Pagamentos, Beneficios e Descontos(2)
Sair(-1)\n""")
        case '1':
            choice_2 = (input("""
Visualizar Lista de Funcionários (1)
Contratar Funcionários (2)
Demitir Funcionários (3)
Atualizar o Perfil dos Funcionários(4)
Ver Avaliação Funcionários                              
Avaliar os Funcionários(6)
Voltar(-1)\n\n"""))
            match choice_2:
                case '1':
                    lista_de_funcionários = Funções.Print_Informação_Funcionários(lista_de_funcionários)
                case '2':
                    lista_de_funcionários = Funções.Adicionar_funcionário(lista_de_funcionários)
                case '3':
                    lista_de_funcionários = Funções.Remover_Funcionário(lista_de_funcionários)
                case '4':
                     lista_de_funcionários = Funções.Atualizar_Informações(lista_de_funcionários)
                case '5':
                    lista_de_funcionários = Funções.Print_Avaliação_Funcionários(lista_de_funcionários)
                case '6':
                    lista_de_funcionários = Funções.Realizar_Avaliação_Funcionário(lista_de_funcionários)
                case '-1':
                    continue
                case _:
                    print("Opção invalida\n\n")
        case '2':
            choice_2 = (input("""
Registrar Salario Total (1)
Registrar Beneficios (2)
Registrar Descontos (3)
Voltar(-1)\n\n"""))
            match choice_2:
                case '1':
                    lista_de_funcionários = Funções.Registrar_Salario_Total(lista_de_funcionários)
                case '2':
                    lista_de_funcionários = Funções.Registrar_Beneficios_Funcionario(lista_de_funcionários)
                case '3':
                    lista_de_funcionários = Funções.Registrar_Descontos_Funcionario(lista_de_funcionários)
        case '-1':
            print("Obrigado pela preferencia :)")
            break
        case '_':
            print("Opção invalida")
