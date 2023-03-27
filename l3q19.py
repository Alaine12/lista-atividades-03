""" Altere o programa anterior para que ele aceite apenas números entre 0 e 1000."""
while(n <=0)or(n>100):

    n=int(input("digite um numero maior que 0 e menor que 1000.Quantos numeros  voce deseja digitar?""))
                

 while(i<=n):
  x=int(input("digite um numero:"))                

  s=s+x
  i+=1
  ifi==1:
      m=a=x
else:
   ifx>m:
   m=x

   ifx<=a:
    a=x

    i+=1

    print("o maior numero é{}e o menor é{}."format(m,a))
    print("a soma dos numeros e{}".format(s))