

# Ternários

# n1 = int(input("N1: "))
# n2 = int(input("N2: "))
#
# media = (n1 + n2) / 2
# status = "Aprovado" if media >= 7 else "Reprovado"
#
# print(f"Sua média foi: {media:.2f} pontos. Você foi {status}")

# chuva = True
# guarda_chuva = "Aberto" if chuva else "Fechado"
# print(guarda_chuva)

# Match Case

# dia = int(input("Informe o dia da semana de 1 a 7: "))
#
# match dia:
#     case 1: print("Domingo")
#     case 2: print("Segunda")
#     case 3: print("Terça")
#     case 4: print("Quarta")
#     case 5: print("Quinta")
#     case 6: print("Sexta")
#     case 7: print("Sábado")
#     case _: print("dia inválido")
#
# farol = "Verde"
#
# match farol:
#     case "Verde":
#         velocidade = int(input("Velocidade: "))
#         print("Pode ir")
#     case "Amarelo": print("Reduza")
#     case "Vermelho": print("Pare!")
#     case _: print("Cada um por si!")


#     print("Domingo")
# elif dia == 2:
#     print("Segunda-feira")
# elif dia == 3:
#     print("Terça-feira")
# elif dia == 4:
#     print("Quarta-feira")
# elif dia == 5:
#     print("Quinta-feira")
# elif dia == 6:
#     print("Sexta-feira")
# elif dia == 7:
#     print("Sábado")
# else:
#     print("Dia inválido.")

# For:

# for cada_elemento in algum_iteravel:
#     blco indentado

# texto = "Por exemplo"
#
# conta_letras = 0
#
# for letra in texto:
#     # print(caracter, end=' ')
#     # print("OI")
#     if letra == ' ': pass
#     else:
#         conta_letras = conta_letras + 1
#
# print(conta_letras)

# numero_repeticoes = int(input("Informe o n° de repetições: "))

# for i in range(numero_repeticoes):
#     # print(f"Contando {i}")
#     if i % 2 == 0: print(i, "par")
#
#     else: print(i, "ímpar")

# for i in range(5, 40, 2):
#     print(i)
#
# for i in range(5 + 1, 1000 // 10, 2 * 2):
#     print(i)

# for i in range(10, -1, -1):
#     print(i)





# i = 0
#
# while i < 10:
#     i = i + 1
#     print(i)
#
# # for i in range(5, 40, 2):
# #     print(i)

# user = input("User: ")
# password = input("Password: ")
#
# if user == 'thiago': valid_user = True
# else: valid_user = False
#
# if password == '123': valid_password = True
# else: valid_password = False
#
# limite = 3
#
# while not valid_user and not valid_password:
#     user = input("User: ")
#     password = input("Password: ")
#     if limite > 0:
#         if user == 'thiago': valid_user = True
#         else: valid_user = False
#
#         if password == '123': valid_password = True
#         else: valid_password = False
#
#         limite = limite - 1
#     else:
#         print('excedeu o n de chances.')

user = input("User: ")
password = input("Password: ")

for i in range(3):

    if user == "thiago" and password == '123':
        print("bem-vindo")
    else:
        print('tente outra vez')