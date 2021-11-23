quantity=int(input("pleawe enter total quantity:"))
per_unit=int(input("please enter per unit:"))
total_cost=quantity*per_unit
discount=total_cost*10/100
if total_cost>=1000:
    print("you got discount","rs",discount,"thank you came again")    
else:
    print("you can't get discount")