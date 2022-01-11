n=int(input())
sum=0;
k=0;
count=1
while count <= n:
  k=k+1;
  if k%2==0:
     sum=sum+k;
  count=count+1;
print(sum)
