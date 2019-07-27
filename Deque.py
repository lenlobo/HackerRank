# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
d = deque()
ans=[]
o = int(input())
for i in range(o):
    qn=input()
    qn=qn.split(' ')
    if len(qn)==1:
        q=qn[0]
    elif len(qn)==2:
        q=qn[0]
        n=qn[1]
    if q == 'append':
        d.append(n)
    elif q=='appendleft':
        d.appendleft(n)
    elif q=='pop':
        d.pop()
    elif q=='popleft':
        d.popleft()
for i in d:
    ans.append(int(i))
for i in ans:
    print(i,end=' ')
