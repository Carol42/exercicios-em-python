""" Você vai pedir doces ou travessuras com um amigo e todas as casas que você visita, exceto três, estão distribuindo doces. Uma casa que você visita está distribuindo escovas de dentes e duas casas estão distribuindo notas de dólar.

Tarefa
Dada a entrada do número total de casas que você visitou, qual é a chance percentual de que um item aleatório retirado de sua bolsa seja uma nota de um dólar?

Formato de entrada
Um número inteiro (>=3) representando o número total de casas que você visitou.

Formato de saída
Um valor percentual arredondado para o número inteiro mais próximo.

Exemplo de entrada
4

Exemplo de saída
50 """

print("Insira a quantidade de casas que você visitou: ")
houses = int(input())
from math import ceil
result = ceil(200/houses)
print (str(result) + "%")