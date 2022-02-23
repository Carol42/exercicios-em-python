# Algoritmo para expandir, de forma simples, um Binômio de Newton

import math
print("CALCULADORA BINÔMIO DE NEWTON")
a=float(input("Digite um valor para a (coeficiente de X): "))
b=float(input("Digite um valor para b (coeficiente de Y): "))
n=int(input("Digite um valor para n (expoente do binômio): "))
w=int(input("Digite um valor para w (expoente de X): "))
z=int(input("Digite um valor para z (expoente de Y): "))
p = 0
n1=n
n2=0
while p <= n:
   print("+ %.0f x^%.0f y^%.0f"%((math.factorial(n)/((math.factorial(p))*(math.factorial(n-p))))*((a**n1)*(b**n2)) , (n1*w), (n2*z)) , end="") 
   p+=1
   n1-=1
   n2+=1
