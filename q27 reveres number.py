num=int(input("please enter the number:"))
a=num%10
b=(num//10)%10
c=(num//100)%10
d=(num//1000)%10
if (a,b,c,d):
    print(a,b,c,d)
else:
    print("-")