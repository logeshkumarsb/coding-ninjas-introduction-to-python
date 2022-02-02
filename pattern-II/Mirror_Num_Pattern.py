n=int(input())
i=1
while i<=n:
    k=1
    j=1
    while k<n-i+1:
        print(" ",end='')
        k=k+1
    while j<=i:
        print(j,end='')
        j=j+1
    print()
    i=i+1
