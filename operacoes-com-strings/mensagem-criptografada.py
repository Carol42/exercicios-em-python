""" Você é um agente secreto e recebe uma mensagem criptografada que precisa ser decodificada. O código que está sendo usado inverte a mensagem e insere caracteres não alfabéticos na mensagem para dificultar a decifração.

Tarefa:
Crie um programa que pegue a mensagem codificada, inverta-a, remova quaisquer caracteres que não sejam uma letra ou um espaço e produza a mensagem oculta. """

print("Insira a mensagem a ser descriptografada: ")
a=input()
list=[]
for i in range (len(a)):
 list.append(a[i])
list.reverse()
str=""
b=str.join(list)
for x in range(len(b)):
 if b[x].isalpha() == True:
  continue 
 elif b[x] == " ":
  continue
 else:
  b=b.replace(b[x], "5")
b=b.replace("5", "")
print(b)