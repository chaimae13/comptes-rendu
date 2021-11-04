def trouver(mat):
 for i in mat:
     a=0
     for j in  i:
         if j==l:
               print("i=",mat.index(i),"j=",a)
         a=a+1
mat=[[1,2,3]
     [4,5,6]
     [7,8,9]]
l=int(input("donner la valeur a trouver"))
print("lindex est",trouver(mat))