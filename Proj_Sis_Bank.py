#Funções
def Menu():
    menu = '''\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Escolha a operação desejada:
        [ D ] Depositar
        [ S ] Sacar
        [ E ] Extrato
        [ NC] Nova conta
        [ LC] Listar constas
        [ NU] Novo usuário
        [ Q ] Sair
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
=> '''
    return input(menu).lower()

def Deposito(saldo, deposito, extrato, /):
    if deposito > 0:
        saldo += deposito
        extrato += f"Depósito: R${deposito:.2f}\n"
        print("\nDepósito realizado com sucesso!")
    else:
        print("\nNão foi possivel realizar o depósito!\nValor não permitido.")

    return saldo, extrato

def Saque(*, saldo, saque, extrato, limite,  numero_saques, limite_saques):
    if saque > saldo:
        print("\nNão foi possivel realizar o saque!\n\nVocê não tem saldo suficiente.")

    elif saque > limite:
        print("\nNão foi possivel realizar o saque!\n\nValor acima do limite permitido.")

    elif numero_saques >= limite_saques:
            print("\nNão foi possivel realizar o saque!\n\nLimite de saques diários exedido.")

    elif saque > 0:
        saldo -= saque
        numero_saques += 1
        extrato += f"Saque: R${saque:.2f}\n"
        print("\nSaque realizado com sucesso!\n\nRetire o dinheiro na boca do caixa.")

    else:
        print("\nNão foi possivel realizar o saque!\n\nValor não permitido.")

    return saldo, extrato, numero_saques

def Extrato(saldo, /, *, extrato, numero_saques):
    print("\n=-=-=-=-= Extrato Bancário =-=-=-=-=")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaques realizados: {numero_saques}")
    print(f"Seu saldo atual é: R${saldo:.2f}")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

def Criar_user(usuarios):
    cpf = input("\nInforme o CPF (somente números): ")
    usuario = Listar_usuario(cpf, usuarios)
    if usuario:
        print("\nJá existe usuário com esse CPF!")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nº - bairro - cidade/estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("\nUsuário cadastrado com sucesso!")

def Listar_usuario(cpf, usuarios):
    usuarios_listados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_listados[0] if usuarios_listados else None

def Criar_conta(agencia, numero_conta, usuarios):
    cpf = input("\nInforme o CPF do usuário: ")
    usuario = Listar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\nUsuário não encontrado, por favor verifique os dados digitados.")

def Listar_contas(contas):
    print("\n=-=-=-=-= Contas cadastradas =-=-=-=-=")
    for conta in contas:
        linha = f"""
    Agência: {conta["agencia"]}
    C/C: {conta["numero_conta"]}
    Titular: {conta["usuario"]["nome"]}
"""
        print("=-" * 30)
        print(linha)

def main():
    #Constantes
    AGENCIA = "0001"
    LIMITE_SAQUES = 3
    #Variaveis
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    print("=-= Bem vindo ao DIOBANK =-=")
    while True:
        opcao = Menu()
        
        if opcao == "d":
            deposito = float(input("\nInforme o valor do depósito: R$"))
            saldo, extrato = Deposito(saldo, deposito, extrato)

        elif opcao == "s":
            saque = float(input("\nInforme o valor do saque: R$"))
            saldo, extrato, numero_saques = Saque(
                saldo = saldo,
                saque = saque,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES,
            )
            
        elif opcao == "e":
            Extrato(saldo, extrato = extrato, numero_saques = numero_saques)

        elif opcao == "nu":
            Criar_user(usuarios)
        
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = Criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            Listar_contas(contas)

        elif opcao == "q":
            print("=-" * 30)
            print("\nObrigado por usar nosso sistema!\n")
            print("=-" * 30)
            break

        else:
            print("Opção inválida, por favor informe novamente a opção desejada:")

#Programa
main()