#Faça um Programa que leia 4 notas, mostre as notas e a média.

#declaração de variáveis
tempo = ['1° Bimestre', '2° Bimestre', '3° Bimestre', '4° Bimestre']
nota = []

#Função para receber e armazenar as notas em listas 
def recebe_nota():
    for c in range(4):
        nota.append(
        float(input(f"Insira a nota do {tempo[c]}: "))
        )

recebe_nota()


#Qual método utilizar? um for pritando nota por nota ou transformr as listas em dicionários? 
def nota_media():
    for c in range(4):
        print(f"A nota do {tempo[c]} foi igual a: {nota[c]}")
    media = sum(nota) / 4
    print(f"A nota média do aluno é igual a: {media:.2f}")

    #para saber se o aluno foi aprovado ou reprovado.
    if media >= 7:
        print("Com essa média, o aluno está APROVADO.")
    else:
        print("Com essa média, o aluno está REPROVADO.")

nota_media()


    



