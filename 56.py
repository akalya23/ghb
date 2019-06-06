B=input()
c1=c2=0
for i in B:
  if i.isalpha():
    c2+=1
  elif i.isnumeric():
    c1+=1
if c1>=1 and c2>=1:
  print("Yes")
else:
  print("No")
