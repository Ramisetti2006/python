#program-1:

number=float(input("Enter a Number : "))
if number>0:
    print("Positive Number")
elif number<0:
    print("Negative Number")
else:
    print("Zero")


#Program-2:
    
a=int(input("Enter First Number : "))
b=int(input("Enter Second Number : "))
c=int(input("Enter Third Number : "))
if a>b and a>c:
    print("Largest =",a)
elif b>c:
    print("Largest =",b)
else:
    print("Largest =",c)


#Program-3:
year=int(input("Enter Year : "))
if(year%400==0):
    print("Leap Year")
else:
    print("Not Leap Year")

#Program-4:
    
marks=float(input("Enter Marks : "))
if marks>=90:
    grade='A+'
elif marks>=80:
    grade='A'
elif marks>=70:
    grade='B'
elif marks>=60:
    grade='C'
elif marks>=50:
    grade='D'
else:
    grade='F'
print("Grade =",grade)

#Program-5

print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
choice=int(input("Enter Choice : "))
a=float(input("Enter First Number : "))
b=float(input("Enter Second Number : "))
if choice==1:
    print("Addition =",a+b)
elif choice==2:
    print("Subtraction =",a-b)
elif choice==3:
    print("Multiplication =",a*b)
elif choice==4:
    if b!=0:
        print("Division =",a/b)
    else:
        print("Division by Zero Not Possible")
else:
    print("Invalid Choice")


