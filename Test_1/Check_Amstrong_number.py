n=int(input())
k=n
j=n
count=0;
while j!=0:
    count=count+1
    j=j//10
rev=0
while k!=0:
    a=k%10
    rev=rev+a**count
    k=k//10
if(rev==n):
    print("true")
else:
    print("false")
