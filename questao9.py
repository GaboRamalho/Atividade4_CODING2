# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um
# crime. As perguntas são:
# i) Telefonou para a vítima?
# ii) Esteve no local do crime?
# iii) Mora perto da vítima?
# iv) Devia para a vítima?
# v)Já trabalhou com a vítima?; 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a
# 2 questões ela deve ser classificada como "Suspeita",  entre 3 e 4 como
# "Cúmplice", e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente"

def perguntas():

    #variável necessária para o começo da contagem de pontos
    positivo = 0
    

    #definição da contagem de pontos
    status = {2 : "Suspeito(a)",
                3 : "Cúmplice",
                4 : "Cúmplice",
                5 : "Assassino"}

    #Perguntas inseridas em formato de lista 
    lista_perguntas = ["Você Telefonou para a vítima",
                        "Você Esteve no local do crime",
                        "Você Mora perto da vítima",
                        "Você Devia algum dinheiro para a vítima",
                        "Em algum mommento você Já trabalhou com a vítima"]


    #for para gerar as perguntas armazenadas em listas
    for c in (lista_perguntas):
        print (f"{c} Sim ou não?")
        resposta = input("Resposta:")
        
        #Se resposta for positiva então ele incrementa. 
        if resposta.lower() == 'sim':
            positivo += 1
            
    #Verificar o "nível" da pessoa de acordo com as resposta positivas
    if positivo in status:
        print (status[positivo])
    #caso seja inocente    
    else:
        print ("Relaxa, você é inocente")

perguntas()