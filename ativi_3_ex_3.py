
# Receber os lados do triângulo

a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

# Verificar se os lados informados formam um triângulo

# a + b > c
# b + c > a
# c + a > b

print()

if a + b > c and b + c > a and  c + a > b:
    print(f'{a}, {b} e {c} formam um triângulo do tipo: ', end='')
    # Equilátero
    if a == b == c: print("Equilátero.")

    # Isóceles
    elif a == b or b == c or c == a: print("Isóceles.")

    # Escaleno
    elif a != b != c: print("Escaleno.")

else:
    print(f'{a}, {b} e {c} não formam um triângulo.')



