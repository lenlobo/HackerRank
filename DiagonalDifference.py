n=int(input())
mat=[]
pdg=[]
ndg=[]
for i in range(n):
    l=[]
    l1=[]
    inp=input()
    l=list(inp.split(" "))
    for i in l:
        l1.append(int(i))
    mat.append(l1)
for i in range(n):
    for j in range(n):
        if i==j:
            pdg.append(mat[i][j])
mat2=[]
for i in mat:
    i=i[::-1]
    mat2.append(i)

for i in range(n):
    for j in range(n):
        if i==j:
            ndg.append(mat2[i][j])

print(abs(sum(pdg)-sum(ndg)))
