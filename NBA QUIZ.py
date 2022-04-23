from PIL import Image
image1 = image('wiltchamberlain.jpg')
print("This is my quiz. Let's play!")


playinggame = input("Would you like the play the game? ")

if playinggame != "yes":
    quit()
print("Okay! Let's start the game!")
score = 0
answer = input("Who scored 100 points in one NBA game? ")
if answer.lower() == "wilt chamberlain":
    im = Image.open("wiltchamberlain.webp")
    im.show("wiltchamberlain.webp")
    print('Correct!')
    score += 1
else:
    ("Incorrect!")
answer = input("Who won the NBA MVP in 1995? ")
if answer.lower() == "david robinson":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
answer = input("Who was the first Canadian NBA player drafted 1st overall? ")
if answer.lower() == "anthony bennett":
    print("Correct!")
    score += 1
else:
    ("Incorrect!")
answer = input("Who was the youngest NBA player to make his NBA debut in a NBA Game? ")
if answer.lower() == "andrew bynum":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
answer = input("Which coach holds the record for the most coaching wins in NBA history? ")
if answer.lower() == "don nelson":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
answer = input("How many points did Michael Jordan score in a NBA Playoff game. Hint: It is the record for most points in a game in playoff history. ")
if answer.lower == "63":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
answer = input("Who is the tallest NBA Player ever to play? ")
if answer.lower() == "gheorghe muresan":
    print('Correct!')
    score += 1
else: 
    print("Incorrect!")
answer = input("Who is the shortest NBA player to play a NBA game? ")
if answer.lower() == "muggsy bogues":
    im1= Image.open("muggsybogues.jpg")
    im.show("muggsybogues.jpg")
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
answer = input("Who is the most traded NBA player in history? ")
if answer.lower() == "trevor ariza":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
answer = input("Which NBA player has played the most seasons with one team? ")
if answer.lower() == "dirk nowitzki":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
("You got " + str(score) + "questions correct!")
("You got " + str((score/10)* 100) + " questions correct!")