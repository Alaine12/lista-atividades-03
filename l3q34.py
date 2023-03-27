"""Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é aquele que é divisível apenas por um e por ele mesmo.
 Faça um programa que peça um número inteiro e determine se ele é ou não um número primo."""
 num = int(input ("\nDigite um numero inteiro para saber se é primo: "))
cont = 0
div = []

for i in range(num):

    if num%(i+1) == 0:

        cont += 1
        div.append(i+1)

    else:

        cont
        

if cont == 2:

    print ("O numero é primo divisivel por ",div)

else:

    print ("O numero não é primo pois é divisivel por ",div)
        