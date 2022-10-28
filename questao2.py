#Faça um programa que receba a temperatura média de cada mês do ano e armazene-
#as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as
#temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês
#por extenso: 1 – janeiro, 2 – fevereiro, . . .).

#Em todos os exercícíos irei utilizar a maior quantidade de funções que puder, Professora. Talvez o código não fique tão limpo assim, mas estou realmente precisando treinar funções.
#Espero que possa considerar os códigos e fico aberto a todos os comentários. 


#INICIO DO CÓDIGO

#Definição das listas
mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
temp = []


#função para receber as temperaturas e armazena-las em listas
def temp_mes():
    for c in range (12):
        temp.append(
            float(input(f"Qual foi a temperatura de {mes[c]} em °c? "))
        )

temp_mes()

media = sum(temp) / 12

#função para exibir média de temperatura anual 
def media_anual():
    print(f"A média anual em °c é igual a: {media:.2f}") 

media_anual()


#função para apresentar qual mês teve temperatura acima da média
def acima_media():
   for c in range(12):
    if temp[c] > media:
        print(f"{c+1} - {mes[c].capitalize()} com {temp[c]:.2f}°c")

acima_media()









