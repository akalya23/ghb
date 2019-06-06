    
num1,num2=list(map(int,input().split()))
a1=list(map(int,input().split()))
count=0
for i in a1:
  if(i==num2):
    count=count+1
if(count>0):
  print("yes")
else:
  print("no")
