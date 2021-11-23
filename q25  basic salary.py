salary=int(input("please enter the salary:"))
HRA=salary*int(input("please enter persentage:"))/100
DA=salary*int(input("please enter persentage:"))/100
gross_salary=salary+HRA+DA
if salary<=10000: 
    # HRA=20%,DA=80%
    print(gross_salary)
elif salary<=20000:
    # HRA=25%,DA=90%
    print(gross_salary)
elif salary>20000:
    # HRA=30%,DA=95%
    print(gross_salary)
else:
    print("can't able to find gross_salary")