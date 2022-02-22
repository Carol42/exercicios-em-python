""" Você está torcendo pelo seu time favorito. Depois de cada jogada, se o seu time estiver mais de 10 jardas no campo, você se levanta e dá um high five ao seu amigo. Se eles não avançarem pelo menos um metro, você fica quieto e diz 'shh', e se eles avançam 10 metros ou menos, você diz 'Ra!' para cada jarda que eles avançaram naquela jogada.

Tarefa
Dado o número de jardas que seu time avançou, produza 'High Five' (para mais de 10), 'shh' (para <1) ou uma string que tenha um 'Ra!' para cada jarda que eles ganharam.

Formato de entrada
Um valor inteiro que representa o número de jardas ganhas ou perdidas por sua equipe.

Formato de saída
Uma sequência de gritos apropriados.

Exemplo de entrada
3

Exemplo de Saída
Rá!Rá!Rá! """

print("Insira a quantidade de jardas que a equipe avançou: ")
yards = (int(input()))
if (yards>10):
 print("High Five")
elif (yards<1):
 print("shh")
else:
  print("Ra!" * yards)