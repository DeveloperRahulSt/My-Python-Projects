print("Welcome to my math quiz!")

ifPlaying = input("Do you want to play? ")

if ifPlaying.lower() != "yes":
    quit()

print("Let's begin!")

score = 0

quiz = input("How much is 12-5? ")
if quiz == "7":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

quiz = input("How much is 5*8? ")
if quiz == "40":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " answers correct.")





