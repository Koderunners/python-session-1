a = int(input("Enter a number:"))

while True:
    opr = input("Enter Operator: ")
    if (opr == '='):
        break

    b = int(input("Enter another number:"))
    
    if opr ==  "+":
        a = a + b
    elif opr == "-":
        a = a- b 
    elif opr == "*":
        a = a * b 
    elif opr == "/":
        a = a / b
    elif opr == "//":
        a = a // b 
    elif opr == "**":
        a = a ** b 
    else:
        print ("Operation not supported!")
        break

print ("Result: ", a)