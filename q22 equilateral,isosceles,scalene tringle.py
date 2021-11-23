a=int(input("please enter value:"))
b=int(input("please enter value:"))
c=int(input("please enter value:"))
if a==b and b==c:
    print("equilateral triangle")
elif a==b or b!=c:
    print("isosceles angle")
else:
    print("scalene angle")