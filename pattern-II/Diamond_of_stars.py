n=int(input())

u = n//2+1
l = n - u
i=1
while i<=u:
    space=1
    while space<=u-i:
        print(' ',end='')
        space=space+1
    j=1
    while j<=2*i-1:
        print('*',end='')
        j=j+1
        
    print()
    i=i+1
    

i = l
while i>=1:
    space=1
    while space<=u-i:
        print(' ',end='')
        space=space+1
    j=1
    while j<=2*i-1:
        print('*',end='')
        j=j+1
        
    print()
    i=i-1
