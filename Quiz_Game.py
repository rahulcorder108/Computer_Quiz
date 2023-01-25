print("Welcome to computer quiz!")
playing = input("Do you want to play the game? ")

if playing.lower() == "yes":
    print(playing)
else:
    quit()
print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stands for? ")
if answer.lower()  == "central processing unit":
    print("your answer is correct")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stands for? ")
if answer.lower()  == "graphics processing unit":
    print("your answer is correct")
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stands for? ")
if answer.lower()  == "power supply unit":
    print("your answer is correct")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stands for? ")
if answer.lower()  == "random access memory":
    print("your answer is correct")
    score += 1
else:
    print("Incorrect!")

print("you got " + str(score) + " question correct!")
print("you got " + str((score/4) * 100) + " %.")