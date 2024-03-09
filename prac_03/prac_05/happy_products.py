"""
Happy Products Solution

Enter the number of products you want to buy and your chosen price.
If you buy 0-5 items, they're full price, over 5 items and each one is 10% off!

"""
# Input, Processing, Output:
DISCOUNT_THRESHOLD = 5
MENU = "Menu:\n(I)nstructions\n(C)alculate\n(Q)uit"

print(MENU)
choice_value = input("Choice: ").lower()
while choice_value != "q":
    if choice_value == 'i':
        print("Enter the number of products you want to buy and your chosen price.")
        print(f"If you buy 0-{DISCOUNT_THRESHOLD} items, they're full price, over {DISCOUNT_THRESHOLD} items and each one is 10% off!")
    elif choice_value == 'c':
        number_of_products = int(input("Number of products: "))
        while number_of_products < 0:
            print("Invalid input")
            number_of_products = int(input("Number of products: "))
        price = float(input("Price: "))
        while price <= 0:
            print("Invalid input")
            price = float(input("Price: "))
        total = number_of_products * price
        if number_of_products > DISCOUNT_THRESHOLD:
            total = total * 0.9
        print(f"{number_of_products} x ${price:.2f} products = ${total:.2f}")
    else:
        print("Invalid choice")
    print(MENU)
    choice_value = input("Choice: ").lower()
print("Farewell")