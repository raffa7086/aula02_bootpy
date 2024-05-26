import math
# Programa que recebe dois números inteiros e imprime a divisão inteira do primeiro pelo segundo

# numero01 = int(input("Digite o primeiro número inteiro: "))
# numero02 = int(input("Digite o segundo número inteiro: "))
# resultado = numero01 // numero02
# print(resultado)

# Exercicio 2 (Calcular a área do círculo)


raio_circulo = float(input("Digite o raio do círulo: "))
area_circulo = math.pi * raio_circulo ** 2
format_area = "{:.2f}".format(area_circulo)
print(format_area)