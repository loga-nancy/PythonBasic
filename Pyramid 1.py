n=int(input("Enter a value:"))

for i in range(1,n+1):
    for j in range(1,i+1):
        print("*", end=" ")
    print("\r")