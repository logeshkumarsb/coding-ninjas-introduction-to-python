ans=0
while ans!=6:
 op=int(input())
 if op==1:
     s1=int(input())
     s2=int(input())
     print(s1+s2)
 elif op==2:
     s1=int(input())
     s2=int(input())
     print(s1-s2)
 elif op==3:
     s1=int(input())
     s2=int(input())
     print(s1*s2)  
 elif op==4:
     s1=int(input())
     s2=int(input())
     print(int(s1/s2))
 elif op==5:
     s1=int(input())
     s2=int(input())
     print(int(s1%s2))
 elif op>=7:
     print("Invalid Operation")
 else:
    ans=6
    break
        
