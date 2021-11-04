
def fibonacci (n):
    if(n<=1):
        return n#avnt le 1 ona que le 0 alors el ne return le meme nombre
    else :
        return (fibonacci(n-1)+fibonacci(n-2))#le nombre en fibonnacci est la somment du nombre precedent et l'avant precedant 
n=int(input("entrer le nombre de termes:"))
print("la series est ")
for i in range(n) : #on utulise la boucle for et aussi range pour circuler tout la series de fibonacci
 print(fibonacci(i), end = ' ')