principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principal amount: "))
    if principle <= 0:
        print("Please enter a positive number")
    else:
        break

while True:
    rate = float(input("Enter the rate amount: "))
    if rate <= 0:
        print("Please enter a positive number")    
    else:
        break

while True:
    time = int(input("Enter the number of years: "))
    if time <= 0:
        print("Please enter a positive number")
    else:
        break
    
total = principle * pow((1 + rate/100), time)
print(f"The total amount after{time} years is: {total:.2f}")