import random

print('===========================================')
print('Bem Vindo(a) ao Jogo De Adivinhações Master')
print('===========================================')

numero = round(random.randrange(1,19))
total_de_tentativas = 3
pontos = 1000

print('Qual o nível desejado?\n')
print('(1) Fácil (2) Médio (3) Difícil')

nível = int(input('Digite o nível desejado: '))

if(nível == 1):
    total_de_tentativas = 20
elif(nível == 2):
    total_de_tentativas = 10

else:
    total_de_tentativas = 5



for rodada in range (1,total_de_tentativas + 1):
    print(f'Tentativa {rodada} de {total_de_tentativas}')
    chute = int(input('Digite um numero entre 1 e 30: '))

    if(chute < 1 or chute > 30):
        print('você deve digitar um número entre 1 e 30')
        continue

    acertou = numero == chute
    chute_maior = chute > numero
    chute_menor = chute < numero

    print(f'Você Digitou {chute}')
        
    if(acertou):
        print(f'Você acertou! Sua pontuação foi {pontos} pontos')
        break
        
    else: 
        if(chute_maior):
            (print('Seu Número foi maior que o Número Escolhido'))

        elif(chute_menor):
            (print('Seu número foi menor que o Número Escolhido'))
            pontos_perdidos = abs(numero - chute)
            pontos = pontos - pontos_perdidos

print('0---------0')
print('fim de jogo')
print('0---------0')