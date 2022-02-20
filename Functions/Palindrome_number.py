def checkPalindrome(num):
#Implement Your Code Here
 b=num;
 rev=0
 while b!=0:
     rev=rev*10+b%10
     b=b//10
 if rev==num:
     return True
 else:
     return False
		
num = int(input())
isPalindrome = checkPalindrome(num)
if(isPalindrome):
	print('true')
else:
	print('false')
