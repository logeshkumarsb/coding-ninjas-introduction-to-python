
def printTable(start,end,step):
#Implement Your Code Here
 while start<=end:
     k=int((start-32)*(5/9))
     print(start,end="\t")
     print(k)
     start=start+step

	   
s = int(input())
e = int(input())
step = int(input())
printTable(s,e,step)

