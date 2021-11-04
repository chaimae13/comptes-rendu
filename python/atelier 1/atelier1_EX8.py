def nbr_apparence(l,m):
 cnt=0
 for i in l:
  if i == m:
    """si l'indice i egale a la valeur qu'on cherche alors le compteur s'incremente et on 
    continue sur le reste du liste jusqu'on arrive ala fin"""
    cnt +=1
 return cnt
y=input("chaine :")
z=input("caractere a recupere : ")
print("nbr d'apparence :  ",nbr_apparence(y,z))