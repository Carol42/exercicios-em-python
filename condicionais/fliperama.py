""" Você está jogando um jogo no fliperama local e recebe 1 bilhete da máquina para cada 12 pontos que marcar. Você quer comprar uma pistola de água com seus ingressos. Dada a sua pontuação e o preço da pistola de água (em ingressos), você consegue comprá-la?

Tarefa
Avalie se você marcou ou não pontos altos o suficiente para ganhar ingressos suficientes para comprar a pistola de água no fliperama.

Formato de entrada
A primeira entrada é um valor inteiro que representa os pontos que você marcou jogando, e a segunda entrada é um valor inteiro que representa o custo da pistola de água (em ingressos).

Formato de saída
Uma string que diz 'Compre!' se você tiver ingressos suficientes, ou uma string que diz 'Tente novamente' se você não tiver.

Exemplo de entrada
500
40

Exemplo de saída
Compre! """

print("Quantos pontos você marcou? ")
score=(int(input()))
print("Qual o valor da pistola de agua (em ingressos)? ")
price=(int(input()))

if (score//12 >= price):
 print("Compre!")
else:
 print("Tente novamente")