# utlizo """ para criar strings de multiplas linhas como o menu
menu = """

[d] depositar
[s] sacar
[e] extrato
[q] sair

=> """
# =>""" é uma convenção que significa que o usuario deve digitar algo
saldo = 0
limite = 500
extrato = ""  # "" significa que extrato recebe uma string
numero_saques = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        try:
            valor = float(input("Informe o valor do deposito: "))
        except ValueError:
            print("Operação não realizada. Valor inválido!")
            continue
        if valor > 0:
            saldo = saldo + valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
            # Uso  += porque se usar apenas = vai sobrescrever o valor anterior
            # Usando assim, ele vai acumulando (concatenando)
            print("\nDeposito realizado com sucesso")
        else:
            print("\nOperação não realizada. Valor inválido!")

    elif opcao == "s":
        try:
            saque = float(input("Qual o valor do saque: "))
        except ValueError:
            print("Operação não realizada. Valor inválido!")
            continue
        if saque > saldo:
            print("\nOperação Falhou. Limite insuficiente")
        elif saque > limite:
            print("\nA operação falhou. Valor acima do permitido.")
        elif numero_saques >= LIMITE_SAQUE:
            print("\nA operação falhou! Número de saques excedido.")

        elif saque > 0:
            saldo = saldo - saque
            extrato += f"Saque: R${saque:.2f}\n"
            numero_saques = numero_saques + 1
            print("\nSaque realizado com sucesso")
        else:
            print("Operação não realizada. Valor inválido!")

    elif opcao == "e":
        print("==============EXTRATO==============")
        if extrato == "":
            print("Não foram realizadas movimentações!")
        else:
            print(extrato)
            print(f"Seu Saldo é de R${saldo:.2f}")
            print("===================================")

    elif opcao == "q":
        break

    else:
        print("Operação invalida, por favor selecione novamente a operação desejada.")
