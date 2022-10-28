#007 -  Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda 
#ou vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são 
#ignorados. A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. 
#Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.

#função que recebe a sequência. 
def palindromo():
    sequencia = input('Escreva uma palavra ou frase: ').upper().replace(' ', '')
    sequencia_inv = sequencia[::-1]

    #teste para saber se expressão vai ser palindromo ou não. 
    if sequencia == sequencia_inv:
        print(f'É palíndromo, pois, {sequencia} é exatamente igual ao contrário: {sequencia} --> {sequencia_inv}')
    else:
        print('Não é palíndromo.')

palindromo()




