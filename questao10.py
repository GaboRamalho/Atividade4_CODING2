# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar
# se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo,
# se ele é: equilátero, isósceles ou escaleno. Dicas:
# i) Três lados formam um triângulo quando a soma de quaisquer dois lados for
# maior que o terceiro;
# ii) Triângulo Equilátero: três lados iguais;
# iii) Triângulo Isósceles: quaisquer dois lados iguais;
# iv) Triângulo Escaleno: três lados diferentes;


#função que recebe 
def recebelado():
        lado1 = float(input(" Insira a primeira medida: "))
        lado2 = float(input(" Insira a segunda medida: "))
        lado3 = float(input(" Insira a terceira medida: "))

        return lado1, lado2, lado3 


#define o que é um triângulo e apresenta ao usuário.
def triangulo():
    lado1, lado2, lado3 = recebelado()
    if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
        print("Com essas medidas pode-se formar um triângulo!")
        if lado1 == lado2 == lado3:
            print("Esse triângulo é do tipo equilátero!")     
        elif lado1 != lado2 != lado3:
            print("Esse triângulo é do tipo Escaleno")       
        else:
            print("Esse triângulo é do tipo Isósceles")
    else:
        print("As medidas inseridas NÃO podem formar um triângulo.")


triangulo()