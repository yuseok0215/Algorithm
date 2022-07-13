import sys
from tkinter import N
sys.stdin=open("input.txt","rt")

check=[0]*10000
n=1
for i in range(10000):
    if check[i]==0:
        x=i+1
        while x<=10000:
            check[x-1]=1
            arr=list(str(x))
            for a in arr:
                x+=int(a)
for i in range(10000):
    if check[i]==0:
        print(i+1)