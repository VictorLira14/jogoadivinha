print("********************************")
print("bem vindo ao jogo de adivinhação")
print("********************************")


chute = int(input("Digite o número secreto"))

numero_secreto = 14 
acertou = numero_secreto == chute
chute_maior = chute > numero_secreto
chute_menor = chute < numero_secreto

print(f"você digitou {chute}")

if(acertou):
    print("você acertou!")
else:
    if(chute_maior):
        print("Você errou! Seu número foi maior do que o número secreto")
    elif(chute_menor):
       print("Você errou! Seu número foi menor que o número secreto")
        
    print("Você errou")

    print("***********")
    print("Fim de jogo")
    print("***********")