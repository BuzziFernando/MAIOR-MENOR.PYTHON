temp = [0]*12
meses = [ "jan","fev","mar","abri","mai","jun","jul","ago","set","out","nov","des"]
mese = [0]*12

maiortemp = 0
mesmaiortemp = 0

menortemp = 0
mesmenortemp = 0

for i in range (12) :
    print( " digite a temperatura do mes ",meses [i])
    temp[i]= float(input())

for i in range ( 12) :
    if maiortemp < temp[i]:
        maiortemp = temp[i]
        mesmaiortemp = i

    if i == 0:
        menortemp = temp[i]
        mesmenortemp = i
    else:
        if menortemp > temp[i]:
            menortemp = temp[i]
            mesmenortemp = i

print(" a maior temp do ano foi ",maiortemp,"no mes",meses[mesmaiortemp])
print(" a menor temp do ano foi ", menortemp," no mes",meses[mesmenortemp])

    








