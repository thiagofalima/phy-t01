
# i = 100000
# unidade = 1
#
# i += 1
#
# while i >= 1000:
#     print(i)
#     i -= 10
#     # i = i + 1
#
# somador = 0
#
# while somador < 100:
#     somador += int(input("Digite o número a ser somado: "))
#     print(somador)


# import time
#
# tempo = 3600
#
# while tempo > -1:
#     if tempo == 3600:
#         print("\r", end='1:00:00')
#     else:
#         print("\r", end=f"{tempo//3600}:{tempo//60}:{tempo%60}")
#     time.sleep(1)
#     tempo -= 1

# while True:
#
#     email = input("E-mail: ")
#
#     # if '.com' not in email:
#     if email[-4:] != '.com':
#         print('Falta o .com')
#         continue
#
#     else:
#         print('bem-vindo')
#         break

acesso = 'thiago_001'
controle_acesso = False

tentativas = 3

while not controle_acesso:
    chave_acesso = input("Informe sua credencial: ")

    if tentativas > 0:
        if chave_acesso == acesso:

            controle_acesso = True
            print("Bem vindo ao sistema!")
        else:
            tentativas -= 1
            continue
    else:
        print("Não deu.")
        break


