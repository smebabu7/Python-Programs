fruits = []
prices = []
total = 0

while True:
    fruit = input("Enter a fruit to buy (q to quit) : ")
    if fruit.lower() == "q":
        break
    else:
        while True:
            user_input = input(f"Enter the price of the fruit: Rs ")
            try:
                price = float(user_input)
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        fruits.append(fruit)
        prices.append(price)

print(" ************************* Your  Shopping Cart **********************")
for fruit in fruits:
    print((fruits.index(fruit) + 1), fruit)

for price in prices:
    total += price

ct = len(fruits)
print(f"\nThe total fruits that you have bought are {ct} and the total is Rs {total:.2f}")

while True:
    status =(input("\nPlease confirm the payment status (Yes/No) "))
    if status == "Yes":
        receipt = input("Confirm the total cash received Rs: ")
        if float(receipt) == float(total):
            print("Thank you for the payment!")
            break
        else:
            print("Payment is incomplete! Kindly make the payment!")
    else:
        print("Kindly make the payment")
        continue