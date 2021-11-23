a=int(input("please enter physics marks:"))
b=int(input("please enter chemistry marks:"))
c=int(input("please enter biology marks:"))
d=int(input("please enter mathematics marks:"))
e=int(input("please enter computer marks:"))
total_value=(a+b+c+d+e)*100/500
if total_value>=90:
    print(total_value,"Grade A+")
elif total_value>=80:
    print(total_value,"Grade A")
elif total_value>=70:
    print(total_value,"Grade B+")
elif total_value>=60:
    print(total_value,"Grade B")
elif total_value>40:
    print(total_value,"Grade C")
elif total_value<40:
    print(total_value,"Grade D")
else:
    print("fail")
