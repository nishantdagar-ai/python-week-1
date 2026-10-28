#Take inputs from the user and tell weather the given number is odd or even.
try:
    a=int(input("Enter a Value:"))
    if(a%2==0):
        print("The number is Even")
    else:
        print("The Number is Odd")
except ValueError:
    print("Enter A Valid Integral Input")

