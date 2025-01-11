principle = 0
rate = 0
time = 0

while principle <=0:
    principle = float(input("Enter the principle amount: "))
    if principle <=0:
        print("The principle is not less than ZERO")

while rate <=0:
    rate = float(input("Enter the rate of interest: "))
    if rate <= 0:
        print("The interest should not be less than ZERO")

while time <=0:
    time = int(input("Enter the duration / time: "))
    if time <= 0:
        print("The time is not less than ZERO")

print(f"The principle is {principle}")
print(f"The rate of interest is {rate}")
print(f"The time is {time}")

total = principle * pow((1 + rate / 100), time)

print(f"Balance after {time} year/s: {total:.2f}")