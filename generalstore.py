print ("Welcome to Adanna's General Store!")
print ("I will help you to print your bill.")

name = input ("Enter your name : ")

print ("Hello,{}. Let's start the process.".format(name))
total = 0
while True :
    print ("1. Clothes")
    print ("2. Grocery")
    print ("3. Toys")
    user_choice = int(input("Enter your choice : "))

    if user_choice == 1:
        num = int(input("How many clothes are you buying ? "))
        price_cloth = 6
        print ("Cost of each cloth = £", price_cloth)
        price_each = num * price_cloth

    elif user_choice == 2:
        num + int(input("How many grocery items are you buying ?"))
        price_grocery = 3.5
        print ("Cost of  each grocery item = £",price_grocery)
        price_each = num * price_grocery

    elif user_choice == 3:
        num = int(input("How many toys items are you buying ? "))
        price_toys = 4
