def checkPalindrome(num):
#Implement Your Code Here
 s=num
 rev=0
 while s!=0:
     rev=rev*10+s%10;
     s=s//10
 if rev==num:
	 return True;
 else:
     return False;
		
num = int(input())
isPalindrome = checkPalindrome(num)
if(isPalindrome):
	print('true')
else:
	print('false')
