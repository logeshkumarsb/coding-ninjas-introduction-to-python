f1=0
f2=1
f3=0
n=int(input())
if n==0:
    print(0)
elif n==1:
    print(1)
elif n==2:
    print(1)
else:
 count=3;
 while count<=n+1:
    f3=f2+f1
    f1=f2
    f2=f3
    count=count+1
 print(f3)
