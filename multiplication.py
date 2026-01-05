#take inputs from the user
num=int(input("Enter the digit:"))
l=int(input("Enter the limit:"))
#print multiplication table up to the limit
for i in range(1,l+1):
    print(f"{num}*{i}={num*i}")
