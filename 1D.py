reader=open('input.txt','r')
a,b,c=list(map(int,reader.read().rstrip().split('\n')))
if c<0:
  print('NO SOLUTION')
elif a==0:
  if b!=c**2:
    print('NO SOLUTION')
  else:
    print('MANY SOLUTIONS')
elif ((c**2-b)/a)%1>0:
  print('NO SOLUTION')
else:
  print((c**2-b)//a)