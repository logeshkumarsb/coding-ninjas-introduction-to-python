
def checkMember(n):
#Implement Your Code Here
 f1=0
 f2=1
 f3=0
 count=3;
 while f3!=n:
    f3=f2+f1
    f1=f2
    f2=f3
    if(f3>n):
        break
 if(f3==n):
    return True
 else:
    return False

n=int(input())
if(checkMember(n)):
    print("true")
else:
    print("false")
