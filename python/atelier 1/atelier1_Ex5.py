def compte(n):
 if n < 10:
  return 1
 else:
  return 1 + compte(n/10) 
 """quand on a nombre plus grand que 10 alors il a 2 chiffre ou plus alors on r'applique la fonction 
       compte et on ajoute 1 juusqu'a ls nombre sera plus petit que 10"""
num=int(input("entrer un nombre "))
print("nbr de chiffre est ",compte(num))
