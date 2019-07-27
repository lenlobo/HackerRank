from statistics import  median,pstdev
import numpy as np
import scipy.stats
from scipy.stats import sem, t
from scipy import mean
def mo(x):
    d={}
    for i in x:
        
        ic=x.count(i)
        d.update({i:ic})
    return d
def getKeysByValue(dictOfElements, valueToFind):
    listOfKeys = list()
    listOfItems = dictOfElements.items()
    for item  in listOfItems:
        if item[1] == valueToFind:
            listOfKeys.append(item[0])
    return  listOfKeys
        
    
l2=[]   
n=int(input())
inp=input()
l1=inp.split(" ")
for i in range(len(l1)):
    l1[i]=int(l1[i])
print("{0:.1f}".format(mean(l1)))
print("{0:.1f}".format(median(l1)))
a=mo(l1)
sorted(a.values(),reverse=True)
print(min(getKeysByValue(a,max(a.values()))))
print("{0:.1f}".format(pstdev(l1)))
h= 1.96 * (pstdev(l1)/(n)**0.5)
h="{0:.1f}".format(h)
m= "{0:.1f}".format(mean(l1))
m=float(m)
h=float(h)

print(m-h,m+h)