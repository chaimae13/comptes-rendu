l=[11, 45, 8, 11, 23, 45, 23, 45, 89]
a={}
for i in l:
    if i in a:
       a[i]+=1
    else: 
        a[i]=1
print(a)
         