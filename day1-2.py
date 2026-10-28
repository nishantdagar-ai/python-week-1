#Take A number and tells either the number is negative,positive or zero.
try:
    a=float(input("Enter a Number:"))
    if (a<0):
        print("Number is Negative")
    elif(a>0):
        print("Number is Positive")
    else:
        print("Number is Zero")
except ValueError:
    print("Enter only numbers")