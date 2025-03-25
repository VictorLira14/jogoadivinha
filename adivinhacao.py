import random 


print("********************************")
print("bem vindo ao jogo de adivinhação")
print("********************************")


numero_aleatorio = round(random.random(1,51))
total_de_tentantivas = 3
pontos = 4500

print("qual o nivel desejado?\n")
prnt("(1)facil (2)médio (3)dificil")

nivel = int(input("digite o nivel desejado"))

if(nivel == 1):
    total_de_tentantivas = 25
elif(nivel == 2):
    total_de_tentantivas = 15
else:
    (nivel == 3)
    total_de_tentantivas = 5


print(numero_aleatorio)

for rodada in range(1,total_de_tentantivas +1):
    print(f"tentativas {rodada} de {total_de_tentantivas} ")
    chute = int(input("Digite um número de 1 e 50:"))

    if(chute < 1 or chute > 50):
        print("Você deve digitar um número entre 1 e 50:!") 
        continue

numero_secreto = 14 
acertou = numero_secreto == chute
chute_maior = chute > numero_secreto
chute_menor = chute < numero_secreto

print(f"você digitou {chute}")

if(acertou):
    print("Você acertou sua pontuação foi {pontos} pontos!")
else:
    if(chute_maior):
        print("Você errou! Seu número foi maior do que o número secreto")
    elif(chute_menor):
       print("Você errou! Seu número foi menor que o número secreto")
       pontos_perdidos = abs(numero_secreto - chute)
       pontos = pontos - pontos_perdidos
        
    print("Você errou")

    print("***********")
    print("Fim de jogo")
    print("***********")