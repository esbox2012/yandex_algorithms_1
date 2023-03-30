a,b,c,d=map(int,input().split())
if a==c:
  print(a,b+d)
elif a==d:
  print(a,b+c)
elif b==c:
  print(b,a+d)
elif b==d:
  print(b,a+c)
else:
  s=sorted([[a+c,max(b,d),(a+c)*max(b,d)],[a+d,max(b,c),(a+d)*max(b,c)],[b+c,max(a,d),(b+c)*max(a,d)],[b+d,max(a,c),(b+d)*max(a,c)]],key=lambda x:x[2])
  print(s[0][0],s[0][1])
