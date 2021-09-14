from random import randint
import time

print('-='*20)
print('Vou rolar um dado de 20 e mostrarei o resultado do teste')
print('-='*20)
time.sleep(3)
resultado=randint(0,20)

if resultado<=1:
    print("Você tirou {} no dado".format(resultado))
    print("Você tirou um DESASTRE")

elif resultado<=9:
    print("Você tirou {} no dado".format(resultado))
    print("Você tirou um fracasso")

elif resultado<=15:
    print("Você tirou {} no dado".format(resultado))
    print('Vocé tirou um sucesso normal')

elif resultado<=18:
    print("Você tirou {} no dado".format(resultado))
    print("Você tirou um sucesso bom")

else:
    print("Você tirou {} no dado".format(resultado))
    print("Você tirou um sucesso EXTREMO")