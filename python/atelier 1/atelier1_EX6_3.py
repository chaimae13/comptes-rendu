
def tri_insertion(tab):
    for i in range(len(tab)):
        tmp = tab[i]#circuler sur tous les elements du tableau et poser un variable temporel pour stocker la premier valeur du tableau
        j=i-1
        while j >=0 and tmp < tab[j]:
            """on verifier si un element on tableau a une valeur petit que tmp si oui on les changes la place et
            on repete ceete operaton avec tous les element du tableau"""
            tab[j],tab[j+1]=tab[j+1],  tab[j]
            j-=1
            return tab
T=[5,7,1,6,12,0]
print("le tableau trier par insertion:",tri_insertion(T))
