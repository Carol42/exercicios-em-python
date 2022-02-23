""" Você está se preparando para pintar uma obra de arte. A tela e os pincéis que você deseja usar custam 40,00. Cada cor de tinta que você compra é um adicional de 5,00. Determine quanto dinheiro você precisará com base no número de cores que deseja comprar se o imposto nesta loja for de 10%.

Tarefa
Dado o número total de cores de tinta que você precisa, calcule e imprima o custo total do seu projeto arredondado para o número inteiro mais próximo.

Formato de entrada
Um número inteiro que representa o número de cores que você deseja comprar para seu projeto.

Formato de saída
Um número que representa o custo de sua compra arredondado para o número inteiro mais próximo.

Exemplo de entrada
10

Exemplo de saída
99 """

print("Quantas cores de tinta você deseja comprar? ")
colors=(int(input()))
print(round((40+5*colors)*1.1))