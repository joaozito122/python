from os import system
system("cls")

print("Vamos calcular a raiz quadrada")
numero = input("informe um número:")
print("O número é numérico?", numero.isnumeric())
calculo = float(numero) ** (1/2)
print('A raiz quadrada de {} é {}'.format(numero,calculo))
