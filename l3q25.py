 """Faça um programa que peça para n pessoas a sua idade, ao final o programa devera
   verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma
     é jovem, adulta ou idosa, conforme a média calculada"""
 z=0
 x=[]
 while z != -1:
    z = int(input('Digite a idade: '))

    if z != -1:
        x.append(z)

 if len(x) != 0:
    media = sum(x)/len(x)

 m = round(media,0)

 if 0 <= m <= 25:
    print('Populacao jovem')

 if 26 <= m <= 60:
    print('Populacao adulta')

 if m > 60:
    print('Populacao idosa')