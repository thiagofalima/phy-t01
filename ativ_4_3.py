from click import clear
# from os import system
# system('cls')
# Sistema de banco
saldo = 1000
print()
print("------- Bem-vindo ao Banco Mais Grana -------")
print(f"Saldo em conta: R$ {saldo:,.2f}")
# Menu com operações
tentativas = 3
while True:
    if tentativas > 0:
        operacao = input("""
        [ 1 ] - Depósito
        [ 2 ] - Saque
        ['s'] - Sair
        """).lower()
        if operacao == "s":
            clear()
            break
        elif operacao == '1':
            clear()
            valor = float(input("Valor a ser depositado: "))
            saldo += valor
            print(f"Saldo atual: R$ {saldo:,.2f}")
            continue
        elif operacao == '2':
            clear()
            valor = float(input("Valor a ser sacado: "))
            if valor > saldo:
                print("Saldo insuficiente.")
                continue
            else:
                saldo -= valor
                print(f"Saldo atual: R$ {saldo:,.2f}")
                continue
        else:
            clear()
            print("Opção inválida!")
            tentativas -= 1
            continue
    else:
        print("Tentativas excedidas.")
        break


print("fim")
