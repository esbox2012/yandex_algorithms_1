a=int(input())
b=int(input())
c=int(input())
s=sorted([a,b,c],reverse=-1)
if s[0]<s[1]+s[2]:
	print('YES')
else:
	print('NO')