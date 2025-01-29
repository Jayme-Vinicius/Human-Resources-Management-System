def build_profile(nome, idade, função, salario, horario, beneficios):
    user_profile = {"nome":nome,'idade': idade, "função": função, 'salario': salario, 'horario': horario, 'beneficios': beneficios}
    return user_profile    

def profile_avaliation(nota, descrição, faltas):
    user_avaliation = {"nota": nota, "descrição" : descrição, "faltas" : faltas}
    return user_avaliation

nome = input("Nome do novo funcionario: ").capitalize()
idade = input("idade do novo funcionario: ")
função = input("função do novo funcionario: ").capitalize()
salario = input("salario do novo funcionario: ")
horario = input("carga horaria do novo funcionario: ")
beneficios = input("Beneficios do novo funcionario: ").capitalize()
user_profile = build_profile(nome, idade, função, salario, horario, beneficios)
print(user_profile)
resposta = input("deseja avaliar o novo funcionario ? S ou N: ")
if(resposta == 'S'):
    nota = input("avalie o funcionario com uma nota: ")
    descrição = input("descreva o funcionario: ").capitalize
    faltas = input("quantas faltas o funcionario teve: ")
    avaliação_do_funcionario = profile_avaliation(nota , descrição, faltas)
    print(avaliação_do_funcionario)
    print("funcionario registrado com sucesso ")
else:
    print("funcionario registrado com sucesso ")
