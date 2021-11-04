def factorriel(nb): 
    if nb < 0: #pour un nombre negative on peut pas obtenir le factorriel
        print(" entrer un nbr positive")

    elif nb == 0:
        return 1
        
    else: 
        fact = 1 
        while(nb > 1): #on commence avec 2 car on a deja affecter le "1" a "fact"
            fact *= nb #obtenir la multuplicaion successife des nombres pour avoir le factoriel
            nb -= 1
        return fact 
m=int(input("donner un nbr positive"))
sum=0
for i in range(1,m+1): 
    """on utulise la boucle for pour circuler tous les nombres qui precedent le nombre donner et on pose
    condition d'arret le nbr donne +1 car  range arret aux nbr-1 """
    sum += factorriel(i)/i
print("la somme du fact est ",sum)