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
        self.função = None
        self.salario = None
        self.salario_total = None
        self.horarios = None
        self.status = None

class Avaliação():
    def __init__(self):
        self.nota = "0"
        self.descrição = None
        self.faltas = "0"

class Pagamento():
    def __init__(self):
        self.salario_base = None
        self.beneficios = Beneficios()
        self.descontos = Descontos()

class Beneficios():
    def __init__(self):
        self.beneficios_totais = None
        self.alto_desempenho = None
        self.plano_de_saúde = None
        self.auxilios = None
        self.decimo_terceiro = None

class Descontos():
    def __init__(self):
        self.descontos_totais = None
        self.desempenho_ruim = None
        self.contribuição_inss = None
        self.impostos_de_renda = None
        self.faltas = None

def Adicionar_funcionário(lista_de_funcionários):
    while True:
        novo_funcionário = Funcionários()
        Adicionar_Informação(novo_funcionário.informações)
        avaliação = input("Deseja Realizar uma Avaliação sobre o novo Funcionário?\nSim ou Não: ").strip().lower() 
        if avaliação == "sim":
            Realizar_Avaliação_Funcionário(novo_funcionário)
        beneficios = input("Deseja Realizar o Registro dos Beneficios do Funcionário?\nSim ou Não: ").strip().lower() 
        if beneficios == "sim":
            Registrar_Beneficios(novo_funcionário)
        descontos = input("Deseja Realizar o Registro dos Descontos do Funcionário?\nSim ou Não: ").strip().lower() 
        if descontos == "sim":
            Registrar_Descontos(novo_funcionário)
        salario_total = input("Deseja Realizar o Registro dos Salario Total?\nSim ou Não: ").strip().lower() 
        if salario_total == "sim":
            Registrar_Salario_Total(novo_funcionário)
        if(lista_de_funcionários == None):
            lista_de_funcionários = novo_funcionário
        else:
            funcinário_atual = lista_de_funcionários
            while(funcinário_atual.proximo_funcionário != None):
                funcinário_atual = funcinário_atual.proximo_funcionário
            funcinário_atual.proximo_funcionário = novo_funcionário
            novo_funcionário.anterior_funcionário = funcinário_atual 
        choice = (input("Deseja continuar Contratando funcionarios(1)\nDeseja sair(-1)\n\n"))
        match choice:
            case '-1':
                return lista_de_funcionários
            case '1':  
                continue
            case _:
                print("Opção invalida\n")          

def Remover_Funcionário(lista_de_funcionários):#work in  progresss
        if lista_de_funcionários == None:
            print("Não tem funcionários cadastrados até o momento\n")
            return
        demitido_funcionário = lista_de_funcionários
        while True:
            busca = input("Deseja demitir todos os funcionários ou apenas um funcionários especifico\n\n").strip().lower() 
            while True:
                if busca == "todos":
                    return None
                else:
                    if demitido_funcionário.informações.nome == busca:
                        print(f"remover depois o funcionario {demitido_funcionário.informações.nome} foi encontrado")
                        if demitido_funcionário.anterior_funcionário == None:
                            demitido_funcionário = demitido_funcionário.proximo_funcionário
                            print(f"O Funcionário {demitido_funcionário.anterior_funcionário.informações.nome} foi demitido com sucesso\n")
                            demitido_funcionário.anterior_funcionário = None
                            choice = (input("Deseja continuar demitindo funcionarios(1)\nDeseja sair(-1)\n\n"))
                            match choice:
                                case '-1':
                                    return demitido_funcionário
                                case '1':
                                    break
                                case _:
                                    print("Opção invalida")
                        else:
                            demitido_funcionário.anterior_funcionário.proximo_funcionário = demitido_funcionário.proximo_funcionário
                            print(f"O Funcionário {demitido_funcionário.informações.nome} foi demitido com sucesso\n")
                            choice = (input("Deseja continuar demitindo funcionarios(1)\nDeseja sair(-1)\n\n"))
                            match choice:
                                case '-1':
                                    return lista_de_funcionários
                                case '1':
                                    break
                                case _:
                                    print("Opção invalida")
                    elif demitido_funcionário.proximo_funcionário == None:
                        print("O Funcionário procurado não foi encontrado, tente outra vez\n")
                        choice = (input("Deseja continuar demitindo funcionarios(1)\nDeseja sair(-1)\n\n"))
                        match choice:
                            case '-1':
                                return lista_de_funcionários
                            case '1':
                                break
                            case _:
                                print("Opção invalida")
                    else:
                        demitido_funcionário = demitido_funcionário.proximo_funcionário
            
def Adicionar_Informação(informações_funcionário):
    informações_funcionário.nome = input("Nome completo do funcionário: ")
    informações_funcionário.idade = input("idade do funcionário: ")
    informações_funcionário.função = input("função do funcionário: ")
    informações_funcionário.salario = input("salario do funcionário: ")
    informações_funcionário.horarios = input("carga horaria do funcionário: ")
    informações_funcionário.status  = "Ativo"

def Atualizar_Informações(lista_de_funcionários):
    if lista_de_funcionários == None:
        print("Não tem funcionários cadastrados até o momento\n\n")
        return
    funcinário_atualizado = lista_de_funcionários
    while True:
        busca = input("Deseja atualizas as informações todos os funcionários ou apenas um funcionários especifico\n\n").strip().lower()
        if busca == "todos":
            while True:
                Adicionar_Informação(funcinário_atualizado.informações)
                if funcinário_atualizado.proximo_funcionário == None:
                    choice = (input("Deseja continuar atualizando informações dos funcionarios(1)\nDeseja sair(-1)\n\n"))
                    match choice:
                        case '-1':
                            return lista_de_funcionários
                        case '1':  
                            continue   
                        case _:
                            print("Opção invalida")          
                else:
                    funcinário_atualizado = funcinário_atualizado.proximo_funcionário
        else:
            while True:
                if funcinário_atualizado.informações.nome == busca:
                    Adicionar_Informação(funcinário_atualizado.informações)
                    choice = (input("Deseja continuar atualizando informações dos funcionarios(1)\nDeseja sair(-1)\n\n"))
                    match choice:
                        case '-1':
                           return lista_de_funcionários
                        case '1':
                            break
                elif funcinário_atualizado.proximo_funcionário == None :
                    print("O Funcionário procurado não foi encontrado, tente outra vez\n")
                    choice = (input("Deseja continuar atualizando informações dos funcionarios(1)\nDeseja sair(-1)\n\n"))
                    match choice:
                        case '-1':
                           return
                        case '1':
                            continue
                        case _:
                            print("Opção invalida\n\n")
                else:
                    funcinário_atualizado = funcinário_atualizado.proximo_funcionário
            
def Realizar_Avaliação_Funcionário(lista_de_funcionários):
    if lista_de_funcionários == None:
        print("Não tem funcionários cadastrados até o momento\n\n")
        return
    funcionário_avaliado = lista_de_funcionários
    while True:
        busca = input("Deseja avaliar todos os funcionários ou apenas um funcionários especifico\n\n").strip().lower()
        if busca == "todos":
            while True:
                Avaliação_funcionário(funcionário_avaliado)
                if funcionário_avaliado.proximo_funcionário == None:
                    choice = (input("Deseja continuar avaliando funcionarios(1)\nDeseja sair(-1)\n\n"))
                    match choice:
                        case '-1':
                            return lista_de_funcionários
                        case '1':
                            break
                        case _:
                            print("Opção invalida\n\n")
                else:
                    funcionário_avaliado = funcionário_avaliado.proximo_funcionário
        else:
            while True:
                if funcionário_avaliado.informações.nome == busca:
                    Avaliação_funcionário(funcionário_avaliado)
                    choice = (input("Deseja continuar avaliando funcionarios(1)\nDeseja sair(-1)\n\n"))
                    match choice:
                        case '-1':
                            return lista_de_funcionários
                        case '1':
                            break
                        case _:
                            print("Opção invalida\n\n")

def Avaliação_funcionário(funcionário_avaliado):
    funcionário_avaliado.avaliação.nota = input(f"Em uma escala de zero a dez como você avaliaria o funcionário {funcionário_avaliado.informações.nome}: ")
    funcionário_avaliado.avaliação.descrição = input(f"como você descreveria o funcionário {funcionário_avaliado.informações.nome}: ")
    funcionário_avaliado.avaliação.faltas = input(f"quantas faltas o funcionário {funcionário_avaliado.informações.nome} teve nesse mês: ")               

def Registrar_Salario_Total(lista_de_funcionários):
    if lista_de_funcionários == None:
        print("Não tem funcionários cadastrados até o momento\n\n")
        return
    Salario_funcionário = lista_de_funcionários
    while True:
        busca = input("Deseja Calcular o Salario Total de todos os funcionários ou apenas um funcionários especifico\n\n").strip().lower()
        if busca == "todos":
            while True:
                Calculo_Salario_Total(Salario_funcionário)
                if Salario_funcionário.proximo_funcionário == None:
                    choice = (input("Deseja continuar Registrando o Salario Total dos funcionarios(1)\nDeseja sair(-1)\n\n"))
                    match choice:
                        case '-1':
                            return lista_de_funcionários
                        case '1':
                            break
                        case _:
                            print("Opção invalida\n\n")
                else:
                    Salario_funcionário = Salario_funcionário.proximo_funcionário
        else:
            while True:
                if Salario_funcionário.informações.nome == busca:
                    Calculo_Salario_Total(Salario_funcionário)
                    choice = (input("Deseja continuar Registrando o Salario dos funcionarios(1)\nDeseja sair(-1)\n\n"))
                    match choice:
                        case '-1':
                            return lista_de_funcionários
                        case '1':
                            break
                        case _:
                            print("Opção invalida\n\n")
        
def Calculo_Salario_Total(Salario_funcionário):
    salario_base = int(Salario_funcionário.informações.salario)
    beneficios = Calcular_Beneficios(Salario_funcionário)
    descontos = Calcular_Descontos(Salario_funcionário)
    salario_total = salario_base + beneficios - descontos
    Salario_funcionário.informações.salario_total = salario_total
    return salario_total

def Registrar_Beneficios_Funcionario(lista_de_funcionários):
    if lista_de_funcionários == None:
        print("Não tem funcionários cadastrados até o momento\n\n")
        return
    funcionário_beneficiado = lista_de_funcionários
    while True:
        busca = input("Deseja Registrar os Beneficio de todos os funcionários ou apenas um funcionários especifico\n\n").strip().lower()
        if busca == "todos":
            while True:
                Registrar_Beneficios(funcionário_beneficiado)
                if funcionário_beneficiado.proximo_funcionário == None:
                    choice = (input("Deseja continuar Registrando os Beneficios Recebidos funcionarios(1)\nDeseja sair(-1)\n\n"))
                    match choice:
                        case '-1':
                            return lista_de_funcionários
                        case '1':
                            break
                        case _:
                            print("Opção invalida\n\n")
                else:
                    funcionário_beneficiado = funcionário_beneficiado.proximo_funcionário
        else:
            while True:
                if funcionário_beneficiado.informações.nome == busca:
                    Registrar_Beneficios(funcionário_beneficiado)
                    choice = (input("Deseja continuar Registrando os Beneficios Recebidos funcionarios(1)\nDeseja sair(-1)\n\n"))
                    match choice:
                        case '-1':
                            return lista_de_funcionários
                        case '1':
                            break
                        case _:
                            print("Opção invalida\n\n")
     
def Registrar_Beneficios(funcionário_beneficiado):
    funcionário_beneficiado.pagamento.beneficios.alto_desempenho = input(f"O funcionário {funcionário_beneficiado.informações.nome} possui alto desempenho?\nSim ou Não: ").strip().lower()
    funcionário_beneficiado.pagamento.beneficios.plano_de_saúde = input(f"O funcionário {funcionário_beneficiado.informações.nome} possui possui plano de saúde?\nSim ou Não: ").strip().lower()
    funcionário_beneficiado.pagamento.beneficios.auxilios = input(f"O funcionário {funcionário_beneficiado.informações.nome} Recebe auxilios?\nSim ou Não: ").strip().lower()
    funcionário_beneficiado.pagamento.beneficios.decimo_terceiro = input(f"O funcionário {funcionário_beneficiado.informações.nome} irá receber o 13° salario esse mês?\nSim ou Não: ").strip().lower()

def Calcular_Beneficios(funcionário_beneficiado):
    beneficio_total = 0
    if funcionário_beneficiado.pagamento.beneficios.alto_desempenho == "sim":
        beneficio_total = beneficio_total + (int(funcionário_beneficiado.informações.salario) / 100 * 50)
    if funcionário_beneficiado.pagamento.beneficios.plano_de_saúde == "sim":
        beneficio_total = beneficio_total + (int(funcionário_beneficiado.informações.salario) / 100 * 20)
    if funcionário_beneficiado.pagamento.beneficios.auxilios == "sim":
        beneficio_total = beneficio_total + (int(funcionário_beneficiado.informações.salario) / 100 * 15)
    if funcionário_beneficiado.pagamento.beneficios.alto_desempenho == "sim":
        beneficio_total = beneficio_total + (int(funcionário_beneficiado.informações.salario) / 100 * 200)
    funcionário_beneficiado.pagamento.beneficios.beneficios_totais = beneficio_total
    return beneficio_total

def Registrar_Descontos_Funcionario(lista_de_funcionários):
    if lista_de_funcionários == None:
        print("Não tem funcionários cadastrados até o momento\n\n")
        return
    funcionário_descontado = lista_de_funcionários
    while True:
        busca = input("Deseja Registrar os Descontos de todos os funcionários ou apenas um funcionários especifico\n\n").strip().lower()
        if busca == "todos":
            while True:
                Registrar_Descontos(funcionário_descontado)
                if funcionário_descontado.proximo_funcionário == None:
                    choice = (input("Deseja continuar Registrando os Descontos Recebidos funcionarios(1)\nDeseja sair(-1)\n\n"))
                    match choice:
                        case '-1':
                            return lista_de_funcionários
                        case '1':
                            break
                        case _:
                            print("Opção invalida\n\n")
                else:
                    funcionário_descontado = funcionário_descontado.proximo_funcionário
        else:
            while True:
                if funcionário_descontado.informações.nome == busca:
                    Registrar_Descontos(funcionário_descontado)
                    choice = (input("Deseja continuar Registrando os Descontos Recebidos funcionarios(1)\nDeseja sair(-1)\n\n"))
                    match choice:
                        case '-1':
                            return lista_de_funcionários
                        case '1':
                            break
                        case _:
                            print("Opção invalida\n\n")

def Registrar_Descontos(funcionário_descontado):
    funcionário_descontado.pagamento.descontos.desempenho_ruim = input(f"O funcionário {funcionário_descontado.informações.nome} Possui Desempenho Ruim?\nSim ou Não: ").strip().lower()
    funcionário_descontado.pagamento.descontos.contribuição_inss = input(f"O funcionário {funcionário_descontado.informações.nome} Realiza Contribuição do Inss?\nSim ou Não: ").strip().lower()
    funcionário_descontado.pagamento.descontos.impostos_de_renda = input(f"O funcionário {funcionário_descontado.informações.nome} Paga Impostos de Renda?\nSim ou Não: ").strip().lower()
    funcionário_descontado.pagamento.descontos.faltas = funcionário_descontado.avaliação.faltas

def Calcular_Descontos(funcionário_descontado):
    desconto_total = int(0)
    if funcionário_descontado.pagamento.descontos.desempenho_ruim == "sim":
        desconto_total = desconto_total + (int(funcionário_descontado.informações.salario) / 100 * 20)
    if funcionário_descontado.pagamento.descontos.contribuição_inss == "sim":
        desconto_total = desconto_total + (int(funcionário_descontado.informações.salario) / 100 * 15)
    if funcionário_descontado.pagamento.descontos.impostos_de_renda == "sim":
        desconto_total = desconto_total + (int(funcionário_descontado.informações.salario) / 100 * 40)
    if int(funcionário_descontado.pagamento.descontos.faltas) > 0 :
        desconto_total = desconto_total + (int(funcionário_descontado.pagamento.beneficios.faltas) * 150)
    funcionário_descontado.pagamento.descontos.descontos_totais = desconto_total   
    return desconto_total

def Print_Informação_Funcionários(lista_de_funcionários):
    while True:
        if lista_de_funcionários == None:
            print("Não tem funcionários cadastrados até o momento\n\n")
            return
        funcinário_atual = lista_de_funcionários
        busca = input("Deseja Ver todos os funcionários ou apenas um funcionários especifico\n\n").strip().lower()
        if busca == "todos":
            while True:
                print(f"""
    Nome: {funcinário_atual.informações.nome}
    Idade: {funcinário_atual.informações.idade}
    Cargo: {funcinário_atual.informações.função}
    Salário Base: {funcinário_atual.informações.salario}
    Salário Total: {funcinário_atual.informações.salario_total}
    BeneficiosTotais: {funcinário_atual.pagamento.beneficios.beneficios_totais}
    Descontos Totais: {funcinário_atual.pagamento.descontos.descontos_totais}
    Horários: {funcinário_atual.informações.horarios}
    Status: {funcinário_atual.informações.status}\n""")
                if funcinário_atual.proximo_funcionário == None:
                    break
                funcinário_atual = funcinário_atual.proximo_funcionário
            choice = (input("Deseja continuar buscando funcionarios(1)\nDeseja sair(-1)\n\n"))
            match choice:
                case '-1':
                    return lista_de_funcionários
                case '1':
                    break
                case _:
                    print("Opção invalida\n\n")
        else:
            while True:
                if funcinário_atual.informações.nome == busca:
                    print(f"""
    Nome: {funcinário_atual.informações.nome}
    Idade: {funcinário_atual.informações.idade}
    Cargo: {funcinário_atual.informações.função}
    Salário Base: {funcinário_atual.informações.salario}
    Salário Total: {funcinário_atual.informações.salario_total}
    BeneficiosTotais: {funcinário_atual.pagamento.beneficios.beneficios_totais}
    Descontos Totais: {funcinário_atual.pagamento.descontos.descontos_totais}
    Horários: {funcinário_atual.informações.horarios}
    Status: {funcinário_atual.informações.status}\n""")
                    choice = (input("Deseja continuar buscando funcionarios(1)\nDeseja sair(-1)\n\n"))
                    match choice:
                        case '-1':
                            return lista_de_funcionários
                        case '1':
                            break
                elif funcinário_atual.proximo_funcionário == None :
                    print("O Funcionário procurado não foi encontrado, tente outra vez\n")
                    choice = (input("Deseja continuar buscando funcionarios(1)\nDeseja sair(-1)\n\n"))
                    match choice:
                        case '-1':
                            return lista_de_funcionários
                        case '1':
                            break
                        case _:
                            print("Opção invalida\n\n")
                else:
                    funcinário_atual = funcinário_atual.proximo_funcionário

def Print_Avaliação_Funcionários(lista_de_funcionários):
 while True:
        if lista_de_funcionários == None:
            print("Não tem funcionários cadastrados até o momento\n\n")
            return
        funcinário_atual = lista_de_funcionários
        busca = input("Deseja Ver todos os funcionários ou apenas um funcionários especifico\n\n").strip().lower()
        if busca == "todos":
            while True:
                print(f"""
    Nome: {funcinário_atual.informações.nome}
    Nota: {funcinário_atual.avaliação.nota}
    Descrição: {funcinário_atual.avaliação.descrição}
    Faltas: {funcinário_atual.avaliação.faltas}\n""")
                if funcinário_atual.proximo_funcionário == None:
                    break
                funcinário_atual = funcinário_atual.proximo_funcionário
            choice = (input("Deseja continuar buscando funcionarios(1)\nDeseja sair(-1)\n\n"))
            match choice:
                case '-1':
                    return lista_de_funcionários
                case '1':
                    break
                case _:
                    print("Opção invalida\n\n")
        else:
            while True:
                if funcinário_atual.informações.nome == busca:
                    print(f"""
    Nome: {funcinário_atual.informações.nome}
    Nota: {funcinário_atual.avaliação.nota}
    Descrição: {funcinário_atual.avaliação.descrição}
    Faltas: {funcinário_atual.avaliação.faltas}\n""")
                    choice = (input("Deseja continuar buscando funcionarios(1)\nDeseja sair(-1)\n\n"))
                    match choice:
                        case '-1':
                            return lista_de_funcionários
                        case '1':
                            break
                elif funcinário_atual.proximo_funcionário == None :
                    print("O Funcionário procurado não foi encontrado, tente outra vez\n")
                    choice = (input("Deseja continuar buscando funcionarios(1)\nDeseja sair(-1)\n\n"))
                    match choice:
                        case '-1':
                            return lista_de_funcionários
                        case '1':
                            break
                        case _:
                            print("Opção invalida\n\n")
                else:
                    funcinário_atual = funcinário_atual.proximo_funcionário

    