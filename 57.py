number1,number2=list(map(int,input().split()))
n1=list(map(int,input().split()))
count=0
for i in n1:
  if(i==number2):
    count=count+1
print(count)
