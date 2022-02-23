# Algoritmo que imprime as tabuadas de 0 a 10.

print ("TABUADA 0 AO 10\n")
i=0
a=0
while a<=10:
    for i in range(11):
            c=a*i          
            print("%.0f X %.0f = %.0f" %(a,i,c))
    a+=1
    print()
