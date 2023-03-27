"""A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... 
Faça um programa que gere a série até que o valor seja maior que 500."""
termos = int(input("Digite o numero de termos da série de Fibonacci: "))
numero = 1
numero_anterior = 0
for _ in range(termos):
    print(numero)
    aux = numero
    numero += numero_anterior
    numero_anterior = aux