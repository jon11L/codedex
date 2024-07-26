ph = int(input("Select a ph level between 1 to 14: "))

if ph < 7:
    print("pH Acidic")
elif ph > 7:
    print("pH Basic")
else:
    print("pH Neutral")