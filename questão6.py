#Desenvolva um jogo de acerte o número, onde o computador escolhe um número
#inteiro aleatório de 0 a 20, e o usuário tem 5 tentativas para adivinhar o número


#importando biblioteca
import random;

#definição de variáveis
num_tent = ['Primeira tentativa', 'Segunda tentativa', 'Terceira tentativa', 'Quarta tentativa', 'Quinta tentativa']
tentativas = 0
computador = random.randint(0, 20)


#Mensagem de boas vindas ao game
print("Bem-vindx ao jogo.\n A regra é a seguinte, eu pensei em um número aleatório de 0 a 20 e você tem de acerta-lo em 5 tentativas.\n Será que você consegue adivinhar?")


#função para iniciar a gameplay
def gameplay():
    for c in range(5):
        jogador = int(input(f"{num_tent[c]}:"))
        palpite = tentativas =+ 1
        if jogador == computador:
            print("Acertou, mizeravi!")
            break
        else:
            if jogador > computador:
                print("Infelizmente não foi dessa vez, pense menor.")
            elif jogador < computador:
                print("Infelizmente não foi dessa vez, pense maior.")

gameplay()

