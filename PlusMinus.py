n=int(input())
inp=input()
zero_count=0
p_count=0
n_count=0
arr=inp.split(" ")
for i in range(len(arr)):
    arr[i]=int(arr[i])
for i in range(len(arr)):
    if arr[i]==0:
        zero_count+=1
    elif arr[i]>0:
        p_count+=1
    elif arr[i]<0:
        n_count+=1
print(str.format('{0:.6f}', (p_count/n)))
print(str.format('{0:.6f}', (n_count/n)))
print(str.format('{0:.6f}', (zero_count/n)))
n=int(input())
inp=input()
zero_count=0
p_count=0
n_count=0
arr=inp.split(" ")
for i in range(len(arr)):
    arr[i]=int(arr[i])
for i in range(len(arr)):
    if arr[i]==0:
        zero_count+=1
    elif arr[i]>0:
        p_count+=1
    elif arr[i]<0:
        n_count+=1
print(str.format('{0:.6f}', (p_count/n)))
print(str.format('{0:.6f}', (n_count/n)))
print(str.format('{0:.6f}', (zero_count/n)))
