#Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.


#Esse código abaixo já funcionária. Mas vou pensar em outra solução. 
#for c in range (1, 51, 2):
#    print(c)

def print_impar():
    for c in range(1, 51, 2):
        print(f"{c}")

print_impar()