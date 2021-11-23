character=input("please input character:")
if character>="a" and character<="z":
    print(character,"is alphabet")
elif character>="1" and character<="9":
    print(character,"is number")
elif character=="#" or character=="@" or character=="$":
    print(character,"is a special character")
else:
    print("no")
