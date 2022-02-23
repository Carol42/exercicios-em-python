""" Você tem uma tigela em seu balcão com um número par de pedaços de frutas. Metade deles são bananas e a outra metade são maçãs. Você precisa de 3 maçãs para fazer uma torta.

Tarefa
Sua tarefa é avaliar o número total de tortas que você pode fazer com as maçãs que estão em sua tigela dada a quantidade total de frutas na tigela.

Formato de entrada
Um número inteiro que representa a quantidade total de frutas na tigela.

Formato de saída
Um número inteiro que representa o número total de tortas de maçã inteiras que você pode fazer.

Exemplo de entrada
26

Exemplo de saída
4 """

print("Qual a quantidade total de frutas na tigela? ")
fruit = int(input())

print((fruit//2)//3)