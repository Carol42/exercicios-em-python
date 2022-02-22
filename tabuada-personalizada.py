# Algoritmo que pergunta ao usuário qual tabuada ele quer calcular e a exibe na tela.

print("TABUADA\n")
a=float(input("Digite o número que deseja calcular a tabuada: "))
b=float(input("Digite até qual número você deseja calcular a tabuada: "))
i=0
c=0
while i<=b:
    print("%.0f X %.0f = %.0f" %( a,i,c))
    i+=1
    c=a*i
