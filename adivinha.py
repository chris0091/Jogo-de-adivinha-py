from random import randint
from time import sleep  
computador = randint(0,5) # Faz o computador pensar
print("Olá, eu sou seu computador...")
sleep(1)
print("Acabei de pensar em um número entre 0 e 5.")
sleep(1)
print("Será que você consegue adivinhar qual foi?")
jogador = int(input("Qual é o seu palpite? ")) # Jogador tenta adivinhar
print("PROCESSANDO...")
sleep(2)
if jogador == computador:
  print("PARABÉNS! Você conseguiu me vencer!, o número era {}".format(computador))
elif jogador > computador:
  print("Número alto! Digite outro número: ")
elif jogador < computador:
  print("Número baixo! Digite outro número: ")
else:
 print("GANHEI! Eu pensei no número {} e não no {}!".format(computador, jogador))

                        

