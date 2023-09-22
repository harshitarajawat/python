print("wlcm to my computer quiz" )

playing = input("do u want to play?")

if playing != "yes":
    quit()

print("oka! let's play :)")
score = 0

answer = input("what does gpu stands for? ")
if answer.lower()== "graphic processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect!")


answer = input("what does ram stands for? ")
if answer.lower() == "random access memory":
    print("correct!")
    score += 1
else:
    print("incorrect!")


answer = input("what does psu  stands for? ")
if answer.lower() == "power supply":
    print("correct!")
    score += 1
else:
    print("incorrect!")

print("you got " + str(score) + "questions correct!")
print("you got " + str((score / 3) * 100) + "%.")


    