Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

print("1) Do you like Dawn or Dusk? \n    1- Dawn \n    2-Dusk \n")
q1 = int(input("Enter your answer (1-2):    "))

if q1 == 1:
    Gryffindor +=1
    Ravenclaw += 1
elif q1 == 2:
    Hufflepuff += 1
    Slytherin += 1
else:
    print("Wrong input.")

print("Q2) When I’m dead, I want people to remember me as: \n    1-The Good \n    2-The Great \n    3-The Wise \n    4-The Bold\n")
q2 = int(input("Enter your answer (1-4):    "))

if q2 == 1:
    Hufflepuff += 2
elif q2 == 2:
    Slytherin += 2
elif q2 == 3:
    Ravenclaw += 2
elif q2 == 4:
    Gryffindor += 2
else:
    print("Wrong input.")

print("Q3) Which kind of instrument most pleases your ear? \n    1-The violin \n    2-The trumpet\n    3-The piano\n    4-The drum    \n")
q3 = int(input("Enter your answer (1-4):    "))

if q3 == 1:
    Slytherin += 4
elif q3 == 2:
    Hufflepuff += 4
elif q3 == 3:
    Ravenclaw += 4
elif q3 == 4:
    Gryffindor += 4
else:
    print("Wrong input.")

print(f"\nHufflepuff got {Hufflepuff} , Gryffindor got {Gryffindor}, Ravenclaw got {Ravenclaw}, Slytherin got {Slytherin}")

if Hufflepuff > Gryffindor and Hufflepuff > Ravenclaw and Hufflepuff > Slytherin:
    print(f"Hufflepuff won with {Hufflepuff} points.")
elif Gryffindor > Hufflepuff and Gryffindor > Ravenclaw and Gryffindor > Slytherin:
    print(f"Gryffindor won with {Gryffindor} points.")
elif Ravenclaw > Gryffindor and Ravenclaw > Hufflepuff and Ravenclaw > Slytherin:
    print(f"Ravenclaw won with {Ravenclaw} points.")
elif Slytherin > Gryffindor and Slytherin > Ravenclaw and Slytherin > Hufflepuff:
    print(f"Slytherin won with {Slytherin} points.")
else:
    print("Something went wrong with the scores.")
