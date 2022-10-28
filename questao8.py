# Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que
# adivinhar uma palavra que será mostrada com as letras embaralhadas. O programa
# terá uma lista de palavras previamente definidas e escolherá uma aleatoriamente. O
# jogador terá seis tentativas para adivinhar a palavra. Ao final a palavra deve ser
# mostrada na tela, informando se o usuário ganhou ou perdeu o jogo.

from cgi import test
import random 

palavras = ['Domicilio', 'Porta', 'Abduzir']


# função que recebe um lista e transforma a lista em uma string concatenando ela.
def transform_string(embaralhada):
    embalharadastr = ''
    for c in embaralhada:
        embalharadastr = embalharadastr + str(c)
    return embalharadastr

# função lista de palavras e retorna uma lista com as palavras embaralhadas.
def embaralhar(list_palavra):
    aux = list_palavra
    random.shuffle(aux)
    return aux

def comp_escolhe(palavra):
    tentativas = 0 
    lista_palavra = []
    for i in palavra:
        lista_palavra.append(i)

    embaralhada = embaralhar(lista_palavra)
    retorno = transform_string(embaralhada)

    print("A palavra embaralhada é: " + retorno)
    while tentativas < 6:
        aux = input("Qual a palavra você acha que é: ")
        if aux.lower() == palavra.lower():
            tentativas = 7
        else:
            print("Você erro, tenta novamente. ")
            tentativas += 1

    if tentativas != 7:
        return "perdeu trouxa, a palavra correta é: " + palavra 

    return "palavra correta: " + palavra + " parabens vc ganhou"

#comando final
print(comp_escolhe(palavras[int(random.randrange(0, len(palavras)))]))