
def inverser(t):
  reverse = ""
  l = len(t) #trouver la longeur du chaine
  while l:
     l = l-1
     """acceder a la dernier valeur et le stocker dans "reverse" puis pour l'avant dernier jusqu'on  arrive a
     la premier lettre du chaine et la stocker comme la dernier element en reverse"""
     reverse = reverse + t[l]
  return reverse

def inverser2(t):
  return t[::-1]#methode 2 pour avoir l'inverse plus facilement
y=input("l'invers")

print(inverser(y))
print(inverser2(y))