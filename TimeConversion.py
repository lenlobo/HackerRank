t = input()
k=[]
ans=''
k = t.split(":")
if k[2][2:]=='PM':
    k[0]=int(k[0])
    if k[0]==12:
        k[0]=str(k[0])
        ans=k[0]+":"+k[1]+":"+k[2][:2]
        
    else:
        k[0]=k[0]+12
    
    if k[0]==24:
        k[0]=00
    k[0]=str(k[0])
    ans=k[0]+":"+k[1]+":"+k[2][:2]
elif k[2][2:]=='AM':
    k[0]=int(k[0])
    if k[0]==12:
        k[0]=00
    k[0]='0'+str(k[0])

    ans=k[0]+":"+k[1]+":"+k[2][:2]
print(ans)
