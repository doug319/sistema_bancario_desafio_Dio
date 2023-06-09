menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
            print("Deposito realizado com sucesso!")
        else:
            print("Operação Falhou: O valor informado é inválido")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUE

        if excedeu_saldo:
            print("Operação Falhou! Saldo Insuficiente!")
        elif excedeu_limite:
            print("Operação Falhou! Valor acima do limite diário!")
        elif excedeu_saques:
            print("Operação Falhou! Número de máximo de saques diário excedido")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1 
            print("Saque realizado com sucesso!")
        else:
            print("Operação Falhou: O valor informado é inválido") 

    elif opcao == "e":
        print("\n***************Extrato***************")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("***********************************")
    elif opcao == "q":
        break
    else:
        print("Operação Inválida, por favor selecione novamente a operação desejada.")
    
    