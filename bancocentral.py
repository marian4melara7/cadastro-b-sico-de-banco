import os, time, random

lista_de_contas = []
def limpar_tela():
    os.system("clear")
def id_novo():
    return random.randint(1000, 9999)
def menu():
    print("BEM-VINDO AO BANCO CENTRAL")
    print("1 - Entrar")
    print("2 - Criar uma conta")
    print("3 - Listar contas")
    print("4 - Depositar")
    print("5 - Sacar")
    print("6 - Ver saldo")
    print("7 - Sair")

def criarconta():
    limpar_tela()
    print("Criar Conta")
    nome = input("Digite seu nome: ")
    senha = input("Crie uma senha: ")
    id = id_novo()

    while any(conta['id'] == id for conta in lista_de_contas):
        id = id_novo()

    conta_nova = {
        "Id": id,
        "Nome": nome,
        "Senha": senha,
        "Saldo": 0
    }

    lista_de_contas.append(conta_nova)
    print("Conta criada com sucesso")
    print(f"Seu ID da conta é: {id}")
    print("Bem-vindo ao Banco Central")
    time.sleep(2)

def listar():
    limpar_tela()
    print("Todas as Contas")

    if not lista_de_contas:
        print("Nenhuma conta cadastrada.")
    else:
        for conta in lista_de_contas:
            print(f"ID: {conta['id']} | Nome: {conta['nome']}")

    input("Pressione qualquer tecla para voltar")
    limpar_tela()

def entrar():
    limpar_tela()
    print("Entrar")

    try:
        id_conta = int(input("Digite o ID da sua conta: "))
        senha = input("Digite sua senha: ")

        for conta in lista_de_contas:
            if conta["id"] == id_conta and conta["senha"] == senha:
                print(f"Bem-vindo(a), {conta['nome']}!")
                return conta

        print("ID ou senha invalido")
        time.sleep(2)
        return None

    except ValueError:
        print("Somente numeros")
        time.sleep(2)
        return None

def deposito(conta):
    limpar_tela()
    print("Depositar")

    try:
        valor = float(input("Digite o valor para deposito: R$ "))
        if valor > 0:
            conta['saldo'] += valor
            print(f"Deposito efetuado com sucesso")
            print(f"Novo saldo: R${conta['saldo']}:.2f") 
        else: 
            print("Valor deve ser positivo")
    except ValueError:
        print("Valor inválido")
    
    time.sleep(2)

def sacar(conta):
    limpar_tela()
    print("Sacar Dinheiro")

    try:
        valor = float(input("Digite o valor para sacar: R$ "))
        if valor > 0:
            if valor <= conta['saldo']:
                conta['saldo'] -= valor
                print(f"Saque efetuado com sucesso")
                print(f"Novo saldo: R$ {conta['saldo']}:.2f")
            else:
                print("Saldo insuficiente")
        else:
            print("Valor deve ser positivo")
    except ValueError:
        print("Valor inválido")
    
    time.sleep(2)

def saldo(conta):
    limpar_tela()
    print("Saldo da conta")
    print(f"Titular: {conta['nome']}")
    print(f"Saldo atual: R$ {conta['saldo']:.2f}")
    input("Pressione qualquer tecla para voltar")

while True:
    limpar_tela()
    menu()

    try:
        opcao = int(input("Escolha uma opção: "))   

        if opcao == 1:
            conta_atual = entrar()
            if conta_atual:
                while True:
                    limpar_tela()
                    print(f"CONTA: {conta_atual['nome']}")
                    print("1 - Depositar")
                    print("2 - Sacar")
                    print("3 - Ver saldo")
                    print("4 - Voltar ao menu principal")

                    try:
                        opcao_interna = int(input("\nEscolha uma opção: "))
                        
                        if opcao_interna == 1:
                            deposito(conta_atual)
                        elif opcao_interna == 2:
                            sacar(conta_atual)
                        elif opcao_interna == 3:
                            saldo(conta_atual)
                        elif opcao_interna == 4:
                            break
                        else:
                            print("Opção inválida")
                            pausar()
                    except ValueError:
                        print("Digite um número válido")
                        time.sleep(2)

        elif opcao == 2:
            criarconta()
        elif opcao == 3:
            listar()
            print("Entre na conta primeiro")
        elif opcao == 4:
            deposito()
            print("Entre na conta primeiro")
        elif opcao == 5:
            sacar()
            print("Entre na conta primeiro")
        elif opcao == 6:
            saldo()
            print("Entre na conta primeiro")
        elif opcao == 7:
            print("Obrigado por usar o Banco Central")
            print(f"Até a próxima vez, {conta_atual['nome']}!")
            break
        else:
            print("Opção inválida")   
            time.sleep(2)
            
    except ValueError:
        print("Digite um número válido")
        time.sleep(2)