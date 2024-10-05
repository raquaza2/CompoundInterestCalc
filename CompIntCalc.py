principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principal amount: "))
    if principle <= 0:
        print("Please enter a positive number")
        
print(principle)