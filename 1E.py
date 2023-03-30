import math
reader=open('input.txt','r')
f=reader.read().rstrip().split()
reader.close()

p,n=set(),set()
k1,m,k2,p2,n2=list(map(int,f))
totalm=(p2-1)*m+n2
ans=[]
for i in range(1,1000000):
    totali=math.ceil(k2/i)
    if totali==totalm:
        ans.append(i)
    if len(ans)>10: break


if ans==[] or n2>m:
    print('-1 -1')
elif len(ans)==1:
    p1=math.ceil(k1/ans[0]/m)
    n1=math.ceil(k1/ans[0]-m*(p1-1))
    print(p1,n1)
elif len(ans)>1:
    for i in ans:
        p1 = math.ceil(k1 / i / m)
        p.add(p1)
        n1 = math.ceil(k1 / i - m * (p1 - 1))
        n.add(n1)
    if len(p)>1:
        p1=0
    else:
        p1=list(p)[0]
    if len(n)>1:
        n1=0
    else:
        n1=list(n)[0]
    print(p1,n1)