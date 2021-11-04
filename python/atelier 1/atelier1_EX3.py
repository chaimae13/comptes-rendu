def somme(n):
    if n==1:
      return 1
    elif n==0:
      return 0#on a commence avec 1 alors on a pas d'un nombre a ajouter
    else:
     return (n + somme(n - 1))
     """on rappel la fonction somme mais on l'affect le nombre precedent du nombre pour avoir
      la somme des chiffre precedent du nombre"""
num=int(input("entrer un nombre "))
print("la somme est : ",somme(num))        



