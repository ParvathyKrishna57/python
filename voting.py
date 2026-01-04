try:
    age=int(input("Enter the age:"))
    if age >18:
        print("You are eligible for voting.")
    else:
        print("You are not eligible for voting.")
except ValueError:
    print("Invalid input! please enter a valid number.")
