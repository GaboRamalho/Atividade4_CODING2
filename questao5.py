#Faça um programa que leia 5 números e informe o maior número.

#declaração de variável
espaco = ['primeiro número: ', 'segundo número: ', 'terceiro número: ', 'quarto número: ', 'quinto número: ']
num = []

#função para receber número e armazena-los em lista
def recebe_numero():
    for c in range(5):
        num.append(
            float(input(f"Insira o {espaco[c]}"))
        )

recebe_numero()

#função para definir o maior número
def maior_numero():
    print("O maior número é:",max(num))

maior_numero()