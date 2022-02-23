# Algoritmo para verificar se o CPF é válido

cpf=input('Insira o CPF: ')
cpf1=[10, 9, 8, 7, 6, 5, 4, 3, 2, 0, 0]
cpf2=[0, 10, 9, 8, 7, 6, 5, 4, 3, 2,0]
a=[]
for i in range (11):
    verif1=(int(cpf[i])*(cpf1[i]))
    a.append(verif1)
b=sum(a)
c=b%11
if c == 0:
    d1=0
elif c == 1:
    d1=0
elif c > 1:
    d1=11-c
else:
    print( "ERRO!")
# print(d1)

a2=[]
for i in range (11):
    verif2=(int(cpf[i])*(cpf2[i]))
    a2.append(verif2)
b2=sum(a2)
c2=b2%11
if c2 == 0:
    d2=0
elif c2 == 1:
    d2=0
elif c2 > 1:
    d2=11-c2
else:
    print( "CPF inválido!")
# print(d2)
if d1 == int(cpf[9]):
    if d2 == int(cpf[10]):
       print("Ok!")
    else:
       print("CPF inválido!")
else:
    print("CPF inválido!")
