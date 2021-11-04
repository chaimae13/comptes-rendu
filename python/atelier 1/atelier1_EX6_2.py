#tri par selection

def tri_selection(tab):
    for i in range(0, len(tab)-1):
        MIN=tab[i]
        min = i#circuler sur tous les element et precisant le min sur le debut du tableau 
        for j in range (i+1,len(tab)):
           if  tab [j] < MIN:#verifier si la case suivant est plus petit si oui on modifie le min et on repete cete operatin jusqu'a la fin du tableau
               MIN=tab[j]
               min = j
        x = tab[i]
        tab[i]= tab [min]
        tab [min] = x
        return tab
T=[5,7,1,6,12,0]
print("le tableau trier par selection :",tri_selection(T))
