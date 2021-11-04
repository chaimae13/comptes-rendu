list=[47, 64, 69, 37, 76, 83, 95, 97]
dict={'Yassine':47, 'Imane':69, 'Mohammed':76, 'Abir':97}
l=[]
for i in list:
    if i in dict.values():
        l.append(i)
print(l)