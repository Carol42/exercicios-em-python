# Algoritmo para cadastrar os dados de um cliente em um arquivo .txt com verificação da validade do CPF:

print('INSIRA OS SEUS DADOS PESSOAIS: ')
nome=input('Nome completo: ')
nascimento=input('Data de nascimento: ')
v=0
while v==0:
    cpf=input('CPF: ')
    
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
    if d1 == int(cpf[9]):
        if d2 == int(cpf[10]):
            print("OK")
            v=1
        else:
           print("CPF inválido!")
           v=0
    else:
        print("CPF inválido!")
        v=0
    
rg=input('RG: ')
endereço=input('Endereço: ')
bairro=input('Bairro: ')
numero=input('Número: ')
telefone=input('Telefone para contato: ')
email=input('E-mail: ')

arq=open('Cadastro Clientes.txt', 'a')
arq.write('\n')
arq.write("Nome: " + nome + "\n")
arq.write("Data de nascimento: " + nascimento + "\n")
arq.write("CPF: " + cpf + "\n")
arq.write("RG: " + rg + "\n")
arq.write("Endereço: " + endereço + "\n")
arq.write("Bairro: " + bairro + "\n")
arq.write("Número: " + numero + "\n")
arq.write("Telefone para contato: " + telefone + "\n")
arq.write("E-mail: " + email + "\n")
arq.close()
