#Marksheet
a=input("Name:")
b=input("class:")
c=input("Age:")
m1=float(input("Mrkas in physics="))
m2=float(input("Mrkas in chemistry="))
m3=float(input("Mrkas in maths="))
avg=(m1+m2+m3)/3
print("average=",avg)
if(avg>=90):
    print("Grade=A")
elif(avg>=75):
    print("Grade=B")
elif(avg>=50):
    print("Grade=C")
else:
    print("FAIL")




