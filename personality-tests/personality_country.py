#Which country are you?
#Personality test

Question_1=input(
    "What is your ideal vacation?\n"
    "A) Tropical beaches, sun, and sea\n"
    "B) Historical cities and museums\n"
    "C) Nature, mountains, and adventure\n"
    "D) Modern cities and shopping\n" 
    "Choose one A/B/C/D "
).strip().upper()

Question_2=input(
    "What kind of food do you prefer?\n"
    "A) Seafood\n"
    "B) Pastries and desserts\n"
    "C) Meat-based dishes\n"
    "D) Street food\n"
    "Choose one A/B/C/D "
).strip().upper()

Question_3=input(
    "Where would you like to live?\n"
    "A) A calm and peaceful island\n"
    "B) A cultural and historical city\n"
    "C) A place close to nature\n"
    "D) A busy and modern metropolis\n" 
    "Choose one A/B/C/D"
).strip().upper()

Question_4=input(
    "Which trait describes you best?\n"
    "A) Relaxed and easygoing\n"
    "B) Artistic and cultured\n"
    "C) Adventurous and energetic\n"
    "D) Fast-paced and hardworking\n"
    "Choose one A/B/C/D"
).strip().upper()

Question_5=input(
    "What kind of weather do you enjoy most?\n"
    "A) Warm and sunny\n"
    "B) Mild and cool\n"
    "C) Cold and snowy\n"
    "D) Changeable but lively\n" 
    "Choose one A/B/C/D"
).strip().upper()


answers=[Question_1,Question_2,Question_3,Question_4,Question_5]

if answers.count('A') >= 3:
    print("You are fun, relaxed, and energetic.You loves sun, sea, and music and you have social and warm personality. So your place is BRAZIL.")
elif answers.count('B') >= 3:
    print('You are artistic and cultured person.You appreciate history and beauty. Also you enjoy life and good food. So your place is ITALY')
elif answers.count('C') >= 3:
    print('You are nature lover and calm person. Also you are adventurous but balanced at the same time.You enjoy peace and quiet. So your place is CANADA.')
elif answers.count('D') >= 3:
    print('You are fast-paced, disciplined, and hardworking person.You love technology and modern life.Also you are organized and focused. So your place is JAPAN')
else:
    print('You are world citizen. You don\'t have one specific place.')

print(f"\n Your answers: , {answers } ")