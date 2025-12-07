#Rollercoaster Project Extendet

print("Welcome to our Rollercoaster!")
user_height = int(input("What is your height in cm? "))
bill = 0
if user_height >= 120:
    print("Great! You can ride")
    age = int(input("What is your age? "))
    if age < 12:
        print("The ticket costs only 5$")
        bill += 5
    elif age <= 18:
        print("The ticket costs 7$")
        bill += 7
    else:
        print("The ticket costs 12$")
        bill += 12
    want_photo = input("Would you like to a photo to be taken? (Y/N) ").lower()
    if want_photo == "y":
        print("The Photo costs extra 3$!")
        bill += 3
        print(f"Your total bill is {bill}$ and have a nice time")

else:
    print("I'm sorry.You cannot ride")