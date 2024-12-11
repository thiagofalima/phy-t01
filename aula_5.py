#
#
# # Operadores de comparação
# #
# # Igual a: ==
#
# a = 10  # -->  Significa atribuição
#
# # a == 10 # --> Significa comparação
#
# print(10 == 2)
# print(2 == 2)
# print(2 == 2.0)
# print(2 == "2")
#
# # Diferente de: !=
#
# print(10 != 2)
# print(2 != 2)
# print(1000 != 100 * 10)
#
# print(100 != int("10" + "0"))
# a = int("100")
# print(a)
# print(type(a))
#
# # Maior que:
#
# print(10 > 2)
# print(0 > 2)
# print(100 > 10)
# print("senha123" > "123")
#
# senha = "password2152356"
#
# print(len(senha) >= 12)
#
# # Menor que:
#
# print(10 < 2)
# print(10 < 2 * 9)
# print("palavra pequena" < "palavra grande")
#
# # Maior ou igual a:
#
# print(10 >= 2)
# print(2 >= 2)
#
# # Menor ou igual a:
#
# print(10 <= 12)
# print(100 <= 12)
#
# # Operadores Lógicos
#
# condicao_1 = 10 > 0  # True
# print(condicao_1)
#
# condicao_2 = 2 == '2'   #True
# print(condicao_2)
#
# print(condicao_1 and condicao_2)
#
# resultado_and = condicao_1 and condicao_2
#
# print(resultado_and)
#
#
# authentic_user = True
# authentic_password = True
#
# libera_user = authentic_user and authentic_password
#
# print(libera_user)
#
# # Pagamento
#
# dinheiro = False
# cartao = False
#
# pagamento = dinheiro or cartao
#
# print(pagamento)
#
# print(5 > 2 or 3 <= 2 or 3 <= 2)

# print(not True)
# print(not False)
#

# caixa_cheia = False
#
# encher_caixa = not caixa_cheia
#
# print(encher_caixa)

# print(not 10 > 5 and 20 % 2 == 0 or 8 >= 4)


# if True:
#     código indentado

# Contexto 1 de funcionamento

# codigo_produto = input("Informe o código do produto: ").upper()
#
# quantidade_minima = 1000
# quantidade_maxima = 2500
#
# # # Contexto 1 de decisão
# if codigo_produto == "LED20":
#     quantidade_estoque = int(input(f"Informe a quantidade de {codigo_produto} em estoque: "))
#     if quantidade_estoque < quantidade_minima:
#         unidades_compra = quantidade_minima - quantidade_estoque
#         print(f"Compre {unidades_compra} unidades do produto {codigo_produto}.")
#
#     elif quantidade_estoque > quantidade_maxima:
#         unidades_venda = quantidade_estoque - quantidade_maxima
#         print(f"Venda {unidades_venda} unidades de {codigo_produto}.")
#
#     else:
#         print(f"Não há necessidade de comprar mais unidades de {codigo_produto}.")
# elif codigo_produto == "LED30":
#     quantidade_estoque = int(input(f"Informe a quantidade de {codigo_produto} em estoque: "))
#     if quantidade_estoque < quantidade_minima:
#         unidades_compra = 1400 - quantidade_estoque
#         print(f"Compre {unidades_compra} unidades do produto {codigo_produto}.")
#
#     elif quantidade_estoque > quantidade_maxima:
#         unidades_venda = quantidade_estoque - 2850
#         print(f"Venda {unidades_venda} unidades de {codigo_produto}.")
#
#     else:
#         print(f"Não há necessidade de comprar mais unidades de {codigo_produto}.")
# else:
#     print(f"{codigo_produto} não existe em nosso sistema.")


# velocidade = int(input("Valocidade: "))
#
#
# if velocidade > 50: multa = 500
# elif velocidade > 40: multa = 1000
# elif velocidade > 30: multa = 2000
# else: multa = 0
#
# print(f"Sua multa é de R$ {multa:,.2f}")
#
#
#
#
