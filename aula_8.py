
# minha_lista = []
#
# print(minha_lista)
# print(type(minha_lista))

#
# minha_lista = [10, 1.4, "OI", True]
#
# for elemento in minha_lista:
#     print(elemento)
#
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# # Índice
#
# print(numeros)
# print(numeros[0])
# print(numeros[5])
# print(numeros[-1])
#
# # Slicing
#
# print(numeros[::-1])
# print(numeros[2:8])
# print(numeros[2:8:2])
#
# numeros_2 = [10, 11, 12, 13, 14]
#
# lista_todos_os_numeros = numeros + numeros_2
#
# print(lista_todos_os_numeros)

# lista = list(range(500))
#
# print(lista)
#
# palavra = "paralelepipedo"
# #
# soletrando = list(palavra)
#
# outra_forma = ' - '.join(soletrando)
#
# print(soletrando)
# print(outra_forma)
#
# nome = input("Nome: ").split()
#
# print(nome)
#
# import time
#
# palavra = "paralelepipedo"
# l1 = 0
# l2 = 1
#
# for i in (range(len(palavra)//2)):
#     print(palavra[l1] + palavra[l2])
#     l1 += 2
#     l2 += 2
#     time.sleep(1)

#
# frutas = ['laranja', 'uva']
# print(len(frutas))
# # Métodos para inserção de elementos na lista
# nova_fruta = 'melancia'
# frutas.append(nova_fruta)
# print(frutas)
# print(len(frutas))
# # Mais itens de por vez
# frutas.extend(['banana', 'maçã', 'maçã',  'uva'])
# print(frutas)
# print(len(frutas))
# for fruta in frutas:
#     print(f"{frutas.count(fruta)}: {fruta}")
# frutas.insert(0, 'pêra')
# print(frutas)
# frutas[2] = 'abacaxi'
# print(frutas)
# # Remover itens de uma lista
# ultima_fruta = frutas.pop()
# print(ultima_fruta)
# print(frutas)
# print(len(frutas))
# # frutas.remove('maçã')
# # print(frutas)
# # print(len(frutas))
# del frutas[2]
# print(frutas)
# while 'maçã' in frutas:
#     frutas.remove('maçã')
# print(frutas)
# # frutas.clear()
# # print(frutas)
# # Ordenação de listas
# frutas.sort()
# print(frutas)
# frutas = sorted(frutas, reverse=True)
# print(frutas)
# matriz = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(matriz)

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# print(sum(numeros))
# print(max(numeros))
# print(min(numeros))

# minha_tupla = (1, 2, 3, 4, 5)
#
# print(minha_tupla)
# print(type(minha_tupla))
#
# print(len(minha_tupla))
#
# for i in minha_tupla:
#     print(i)
#
# print(sum(minha_tupla))
# print(max(minha_tupla))
# print(min(minha_tupla))

# Tuple Unpacking

# tupla = 1, 2, 3
#
# # print(tupla)
# # print(type(tupla))
#
# a, b, c = tupla
#
# print(a, b, c)
# print(type(a))
#
#
# a, b, c = 1, 2, 3


# lista_alunos = ["João", "Maria", "Ana", "Davi"]
# notas_alunos = [5, 7, 10, 9]
#
# print(list(enumerate(lista_alunos)))
#
# for posicao, nome in enumerate(lista_alunos):
#     if nome == 'João':
#         notas_alunos[posicao] = 7.5
#
# print(notas_alunos)


# Dicionários

meu_dicionario = {'b': 2, 'c': 3, 'a': 1}
print(type(meu_dicionario))
print(meu_dicionario['a'])
meu_dicionario['d'] = 4
print(meu_dicionario)
meu_dicionario['b'] = 5
print(meu_dicionario)
del meu_dicionario['c']
print(meu_dicionario)
meu_dicionario.update({'e': 6, 'f': 7, 'g': 8})
print(meu_dicionario)
print(meu_dicionario.items())
print(meu_dicionario.keys())
print(meu_dicionario.values())
for chave, valor in meu_dicionario.items():
    print(chave + ' ---- ' + str(valor))

print(sum(meu_dicionario.values()))