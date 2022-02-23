"""  Você administra uma fábrica de hovercraft. Sua fábrica faz dez hovercrafts em um mês. Dado o número de clientes que você obteve naquele mês, você teve lucro? Custa 2.000.000 para construir um hovercraft, e você os está vendendo por 3.000.000. Você também paga 1.000.000 por mês pelo seguro.

Tarefa:
Determine se você teve lucro ou não com base em quantos dos dez hovercrafts você conseguiu vender naquele mês.
 
Formato de entrada:
Um número inteiro que representa as vendas que você fez naquele mês.

Formato de saída:
Uma cadeia de caracteres que diz 'Lucro', 'Prejuízo' ou 'Ponto de Equilíbrio'.

Exemplo de entrada:
5

Exemplo de saída:
Prejuízo """

print("Quantos hovercrafts você vendeu? ")
sales=(int(input()))

if (sales*3000000000 > 21000000000):
 print("Lucro")
elif (sales * 3000000000 == 21000000000):
 print("Ponto de Equilíbrio")
else:
 print("Prejuízo")