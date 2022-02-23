""" Você está em uma loja de chapéus na Argentina! Os preços estão listados em dólares americanos e pesos argentinos. Você tem os dois, mas quer ter certeza de que pagará o preço mais baixo! Você paga em dólares ou pesos? A taxa de câmbio é de 2 centavos para cada Peso.

Tarefa
Crie um programa que leia dois preços e diga qual deles é mais baixo após a conversão.

Formato de entrada
Dois valores inteiros, o primeiro é o preço em Pesos e o segundo é o preço em Dólares.

Formato de saída
Uma string que diz em qual moeda você deve fazer a compra ('Dólares' ou 'Pesos').

Exemplo de entrada
4000
100

Exemplo de saída
Pesos """

print("Digite o valor em pesos: ")
pesos=(int(input()))
print("Digite o valor em dolares: ")
dollars=(int(input()))

pd=(pesos * 0.02)
dp=(dollars / 0.02)

if (pd > dollars):
 print("Dolares")
else:
 print("Pesos")