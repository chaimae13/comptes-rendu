#tri a bulle
def tri_bull(tab):
      n = len(tab)#affecter a n la taille du tableau
      for i in range(n-1):#circuler sur les cases du tableau et arreter sur la case avant dernier
          for j in range(n-i-1):
              if tab[j] > tab[j+1]:#verifier si la valeur est plus grand dans l'indice suivant alors on les changes les places
                   tab[j],tab[j+1]=tab[j+1], tab[j]
                   return tab
T=[5,7,1,6,12,0]
print("le tableau trier a bulle :",tri_bull(T))

