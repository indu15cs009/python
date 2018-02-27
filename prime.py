r=int(input("enter the number"))
a=int(input("enter the limit"))

for num in range(r,a+1):
    if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
