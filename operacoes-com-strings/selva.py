""" Você está acampando sozinho na selva e ouve alguns animais no escuro nas proximidades. Com base no barulho que eles fazem, determine quais animais eles são.

Tarefa:
Você recebe os ruídos feitos por diferentes animais que você pode ouvir no escuro, avalie cada ruído para determinar a qual animal ele pertence. Os leões dizem 'Grr', os tigres dizem 'Rawr', as cobras dizem 'Ssss' e os pássaros dizem 'Chirp'.

Formato de entrada:
Uma string que representa os ruídos que você ouve com um espaço entre eles.

Formato de saída:
Uma string que inclui cada animal que você ouve com um espaço após cada um. (os animais podem repetir) """

print("Insira os sons que ouviu: ")
a=input()
a=a.replace("Grr", "Lion")
a=a.replace("Rawr", "Tiger")
a=a.replace("Ssss", "Snake")
a=a.replace("Chirp", "Bird")
print(a)