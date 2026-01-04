try:
    num=int(input("Enter a number:"))
    if num>0:
        print("The number is positive.")
    elif num<0:
        print("The number is negative.")
    elif num==0:
        print("The number is zero.")
except valueError:
    print("Invalid input! please enter a number.")
