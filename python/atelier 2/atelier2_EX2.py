list=[1,2,3,4,5,6]
l=len(list)#obtenir le long du liste
x=l//3#diviser liste par trois
y=2*x#acceder a la deuxième partie du liste
l1=list[:x] #premier partie
l2=list[x:y]#deuxième partie
l3=list[y:]#troisième partie
print("la première  partie du liste inverse",l1[::-1])#afficher l'inverse du première  partie
print("la deuxième partie du liste inverse",l2[::-1])#afficher l'inverse du deuxième partie
print("la troisième partie du liste inversel3", l3[::-1] )#afficher l'inverse du troisième partie

 
    

