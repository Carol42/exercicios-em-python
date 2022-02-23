""" Você não está prestando atenção e acidentalmente digita um monte de letras aleatórias no teclado. Você quer saber se já digitou a mesma letra duas vezes, ou se todas são letras únicas.

Tarefa:
Se você receber uma sequência de letras aleatórias, sua tarefa é avaliar se alguma letra é repetida na sequência ou se você apenas pressiona teclas exclusivas enquanto digita. """

text=input()
a=[]
for char in text:
 count = 0
 for c in text:
  if c == char:
   count += 1
   a.append(count)
if any([i>1 for i in a]):
 print("Deja Vu!")
else:
 print("Unico!")