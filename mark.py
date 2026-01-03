a=int(input("Enter mark of maths:"))
b=int(input("Enter mark of ds:"))
c=int(input("Enter mark of web:"))
d=int(input("Enter mark of english:"))
t=a+b+c+d
avg=t/4
print("The total marks you obtained:",t)
print("The average is:",avg)
if avg > 75:
    print("You have achieved Distinction.")
elif avg >= 60 and avg < 75:
    print("You have secured First Class.")
elif avg >= 50 and avg < 60:
    print("You have secured Second Class.")
elif avg >= 40 and avg < 50:
    print("You have secured Third Class.")
else:
    print("You have Failed.")

