n=int(input())
sumOdd=0
sumEven=0
while n!=0:
    a=n%10;
    if a%2==0:
        sumEven=sumEven+a
    else:
        sumOdd=sumOdd+a
    n=n//10
print(sumEven,sumOdd)
