""" Você tem dois amigos que estão falando Pig Latin um com o outro! Pig Latin são as mesmas palavras na mesma ordem, exceto que você pega a primeira letra de cada palavra e a coloca no final, depois adiciona 'ay' ao final disso. ("estrada" = "stradaeay")

Tarefa
Sua tarefa é pegar uma frase em português e transformá-la na mesma frase em Pig Latin!

Formato de entrada
Uma string da frase em português que você precisa traduzir para o Pig Latin. (sem pontuação ou letras maiúsculas)

Formato de saída
Uma sequência da mesma frase em Pig Latin. """

print("Insira a frase a ser traduzida: ")
a=input()
b=a.split()
d=""
for i in range(len(b)):
 c="{0}{1}ay".format(b[i],b[i][0])
 c=c.replace(c[0], "",1)
 d=(d + c + " ")
print(d)