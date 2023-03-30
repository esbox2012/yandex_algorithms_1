reader=open('input.txt','r')
f=reader.read().rstrip().split('\n')
reader.close()
a,b,c,d,e,f=list(map(float,f))


# 1 - бесконечно много решений:
if c!=0 and d!=0 and a/c==b/d:
    if f!=0 and b/d==e/f:
        print(1,-c/d,f/d)
    if f==0 and e==0:
        print(1,1,0)
    elif b/d!=e/f:
        print(0)
elif c==d==f==0 and a!=0 and b!=0 and e!=0:
    print(1,-a/b,e/b)
# 0 - нет решений
elif (a==b==c==d==0 and (e!=0 or f!=0)) or (c!=0 and d!=0 and f!=0 and a/c==b/d and b/d!=e/f):
    print(0)
# 5 - любая пара чисел является ответом
elif a==b==c==d==e==f==0:
    print(5)

# 3 - если y любое число
elif b==0 and d==0:
    if c!=0 and f!=0 and a/c!=e/f:
        print(0)
    else:
        if a==0 and e==0:
            print(3,f/c)
        else:
            print(3,e/a)
# 4 - если x любое число
elif a==0 and c==0:
    if (e==0 and f!=0 and b!=0) or (e!=0 and f==0 and d!=0):
        print(0)
    elif b==0:
        print(4,f/d)
    else:
        print(4,e/b)
# 2 - одно решение
elif a==d==0 and c!=0 and b!=0:
    x0=f/c
    y0=e/b
    print(2,x0,y0)
elif b==c==0 and a!=0 and d!=0:
    x0=e/a
    y0=f/d
    print(2,x0,y0)
else:
    y0=(a*f-c*e)/(a*d-c*b)
    x0=(e-b*y0)/a
    print(2,x0,y0)
