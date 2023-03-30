reader=open('input.txt','r')
n,k,m=list(map(int,reader.read().rstrip().split()))
reader.close()
count=0
while n>=k:
  if k//m==0:
    break
  count+=k//m
  n-=k
  n+=k%m
print(count)