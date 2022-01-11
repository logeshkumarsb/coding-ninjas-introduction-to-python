n=int(input())
s=n;
rev=0;
while s!=0:
    rev=rev*10+s%10;
    s=s//10
print(rev)
