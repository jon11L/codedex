height = float(input("what is your height? (write in cm ex: 177)  "))
credit = int(input("How many credits do you have?  "))

if height >= 150 and credit >= 4:
    print("Enjoy the ride!")
elif height < 150 and credit > 4:
    print("You are not tall enough to ride.")
elif height > 150 and credit < 4:
    print("You don't have enough credits. ")
else:
    print("You have not met either requirement.")
