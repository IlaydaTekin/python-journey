#personality test

Question_1=input(
"How do you usually make important decisions?\n"
"A) Based on logic and facts\n"
"B) Based on feelings and intuition\n"
"C) I ask others for advice\n"
"D) I delay until I’m sure\n" 
"Choose one: A/B/C/D\n"
).strip().upper()

Question_2=input(
"In a group project, what role do you naturally take?\n"
"A) Leader\n"
"B) Organizer/planner\n"
"C) Supporter/helper\n"
"D) Observer\n"
"Choose one: A/B/C/D\n"
).strip().upper()

Question_3=input(
"How do you react to unexpected changes?\n"
"A) I adapt quickly and enjoy it\n"
"B) I feel uncomfortable but adjustn\n"
"C) I try to avoid change\n"
"D) I get stressed and overwhelmed\n"
"Choose one: A/B/C/D\n"
).strip().upper()

Question_4=input(
"What matters most to you in relationships?\n"
"A) Trust\n"
"B) Fun and shared experiences\n"
"C) Loyalty\n"
"D) Communication\n"
"Choose one: A/B/C/D\n"
).strip().upper()

Question_5=input(
"What motivates you the most?\n"
"A) Achieving success and goals\n"
"B) Helping others\n" 
"C) Learning new things\n" 
"D) Having freedom and independence \n"
"Choose one: A/B/C/D\n"
).strip().upper()

answers = [Question_1, Question_2, Question_3, Question_4, Question_5]

if answers.count('A') >= 3:
    print('You are a logical person')
elif answers.count('B') >= 3:
    print('You are intuitive person')
elif answers.count('C') >= 3:
    print('You are seeking approval from other people')
elif answers.count('D') >= 3:
    print('You tend to procrastinate')
else:
    print('You have complex personality.')

print(f"\n Your answer: , {answers}")
