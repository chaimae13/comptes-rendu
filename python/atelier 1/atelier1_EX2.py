def convertir(nb):
    if nb > 1:
        convertir(nb // 2)#on r'appelle la fonction convertir jusqu'au le nbr seria inferieur ou egals 1 
    print(nb % 2, end='')#on obient le reste pour former le nombre on binaire
num=int(input("entrer un nombre "))
print("votre numero converti est") 
convertir(num)
