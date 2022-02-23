""" Há um problema com o seu teclado: ele escreve símbolos aleatoriamente quando você digita um texto. Você precisa limpar o texto removendo todos os símbolos.

Tarefa:
Pegue um texto que inclua alguns símbolos aleatórios e traduza-o em um texto que não tenha nenhum deles. O texto resultante deve incluir apenas letras e números.  """

print("Insira o texto a ser traduzido: ")
a=input()
for i in range(len(a)):
 if a[i].isalpha():
  continue
 elif a[i].isdigit():
  continue
 elif a[i] == " ":
  continue
 else:
  a=a.replace(a[i], "¿")
a=a.replace("¿", "")
print(a)