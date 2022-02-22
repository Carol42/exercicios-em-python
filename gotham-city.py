""" Você é um policial e recebe um relatório de atividade criminosa! Você deve ir por conta própria ou deve chamar um super-herói para ajudá-lo a combater o crime? Se houver menos de 5, você pode lidar com isso sozinho, se houver 5-10, você vai querer ir com o Batman, e se houver mais de 10, você deve ficar onde é seguro e deixar o Batman lidar com isso por conta própria!

Tarefa:
Determine se você precisa ligar para ele com base no número total de criminosos relatados.

Formato de entrada:
Um número inteiro que representa o número total de criminosos presentes na cena.

Formato de saída:
Uma string que diz 'Eu cuido disso!', 'Ajude-me Batman', ou 'Boa sorte aí!' dependendo do cenário.

Exemplo de entrada:
7

Exemplo de saída:
'Ajude-me Batman' """

print("Quantos criminosos na cena do crime? ")
criminals=(int(input()))
if (criminals < 5):
 print("Eu cuido disso!")
elif (criminals > 10):
 print("Boa sorte aí!")
else:
 print("Ajude-me Batman")