import random

print("=== Adivinhe o número ===\n")
secreto = random.randint(a=1, b=1000)
tentativas = 0
palpite = 0
while palpite != secreto :
    palpite = int(input("Seu palpite (1-100) : "))
    tentativas += 1
    if palpite < secreto :
        print("Muito baixo ! ")
    elif palpite > secreto :
        print("Muito alto ! ")
    else:
        print(f"Parabéns ! Acertou em {tentativas} tentativas")
