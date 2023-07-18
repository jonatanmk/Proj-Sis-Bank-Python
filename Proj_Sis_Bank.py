menu = '''=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Escolha a operação desejada:
      [D] Depositar
      [S] Sacar
      [E] Extrato
      [Q] Sair
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
=>'''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

print("=-= Bem vindo ao DIOBANK =-=")
while True:
    opcao = input(menu).lower()
    
    if opcao == "d":
        deposito = float(input("Informe o valor do depósito: R$"))
        if deposito > 0:  
            saldo += deposito
        
            extrato += f"Depósito: R${deposito:.2f}\n"

            print("\nDepósito realizado com sucesso!")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        else:
            print("\nNão foi possivel realizar o depósito!\nValor não permitido.")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

    elif opcao == "s":
        saque = float(input("Informe o valor do saque: R$"))
        if saque > saldo:
            print("\nNão foi possivel realizar o saque!\nVocê não tem saldo suficiente.")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        
        elif saque > limite:
            print("\nNão foi possivel realizar o saque!\nValor acima do limite permitido.")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

        elif numero_saques >= LIMITE_SAQUES:
            print("\nNão foi possivel realizar o saque!\nLimite de saques diários exedido.")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

        elif saque > 0:    
            saldo -= saque

            numero_saques += 1

            extrato += f"Saque: R${saque:.2f}\n"
            print("\nSaque realizado com sucesso!\nRetire o dinheiro na boca do caixa.")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

        else:
            print("\nNão foi possivel realizar o saque!\nValor não permitido.")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        
    elif opcao == "e":
        print("=-=-= Extrato Bancário =-=-=")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saques realizados: {numero_saques}")
        print(f"Seu saldo atual é: R${saldo:.2f}")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

    elif opcao == "q":
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("Obrigado por usar nosso sistema!")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        break

    else:
        print("Opção inválida, por favor informe novamente a opção desejada:")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")