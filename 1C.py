num=''.join(i for i in input() if i.isdigit())
if len(num)==7:
	num='495'+num
else:
	num=num[1:]
for i in range(3):
	newnum=''.join(i for i in input() if i.isdigit())
	if len(newnum)==7:
		newnum='495'+newnum
	else:
		newnum=newnum[1:]
	if newnum==num:
		print('YES')
	else:
		print('NO')