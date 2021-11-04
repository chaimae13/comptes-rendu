list1=[0,1,2,3,4,5]
list2=[6,7,8,9,10,11]
list3=[]
x=0
for i in list1:
    if  x%2 == 1:#on verifie si lindex des element du liste est impaire
     list3.append(i) #si lindex est impaire on l'ajoute a la liste3 on utulisant la fonction append
    x += 1
for i in list2:#on verifie si lindex des element du liste est paire
    if  x % 2 == 0:#si lindex est paire on l'ajoute a la liste3 on utulisant la fonction append
     list3.append(i) 
    x +=1    
print("liste ",list3)
