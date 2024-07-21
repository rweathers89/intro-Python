a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = input("Do you want to  + or - the two numbers?: ")

if c == "+":
    print (str(a) + "+" + str(b) + "=" + str(a + b))
elif c == "-":
     print (str(a) + "-" + str(b) + "=" + str(a - b))
else:
    print("You can only add or subtract the numbers")