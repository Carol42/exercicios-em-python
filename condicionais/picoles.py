""" Você tem uma caixa de picolés e quer dar todos para um grupo de irmãos e irmãs. Se você tiver o suficiente na caixa para dar a cada um uma quantia igual, você deve ir em frente! Se não, eles vão brigar por eles, e você deve comê-los mais tarde.

Tarefa
Dado o número de irmãos para quem você está dando picolés, determine se você pode dar a cada um uma quantia igual ou se você não deve mencionar os picolés.

Formato de entrada
Dois valores inteiros, o primeiro representa o número de irmãos e o segundo representa o número de picolés que você deixou na caixa. """

print("Para quantas crianças você quer dar os picolés?")
siblings = int(input())
print("Quantos picolés você ainda tem na caixa? ")
popsicles = int(input())

if (popsicles%siblings == 0):
 print("Pode dividir entre as crianças!")
else:
 print("Melhor guardar para você...")