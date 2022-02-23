""" Você conhece um grupo de alienígenas, e seu idioma é como o português, exceto que eles dizem cada palavra de trás para frente.
Como você vai aprender a se comunicar com eles?

Tarefa:
Pegue uma frase em português que você gostaria de dizer e transforme-a em uma linguagem que esses alienígenas entendam. """

print("Insira a frase que gostaria de traduzir: ")
a=input()
list=[]
for i in range (len(a)):
 list.append(a[i])
list.reverse()
str=""
b=str.join(list)
print(b)