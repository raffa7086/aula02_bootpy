import math
# Programa que recebe dois números inteiros e imprime a divisão inteira do primeiro pelo segundo

# numero01 = int(input("Digite o primeiro número inteiro: "))
# numero02 = int(input("Digite o segundo número inteiro: "))
# resultado = numero01 // numero02
# print(resultado)

# Exercicio 2 (Calcular a área do círculo)


# raio_circulo = float(input("Digite o raio do círulo: "))
# area_circulo = math.pi * raio_circulo ** 2
# print(f"{area_circulo:.2f}")

# * Novo Exercicio: Crie um programa que peça ao usuário para digitar uma data no formato dd/mm/aaaa e em seguida imprima os valores dessa data separadamente

data_usuario = input("Digite a data no formato dd/mm/aaaa: ")
valores_lista_separado = data_usuario.split("/")
print(f"O primeiro valor é o: {valores_lista_separado[0]}")
print(f"O segundo valor é o: {valores_lista_separado[1]}")
print(f"O terceiro valor é o: {valores_lista_separado[2]}")

