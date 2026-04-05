name=input("Enter your name: ")
print(f"\n Hello {name}. Now we will play a game. I want you to guess a number between 1 to 100. While we are playing clues will guide to you in order to guess the number. Don\'t worry.So let\'s start.")

secret=52
count=0

while True:
   guess=int(input("Enter a number: "))
   count+=1

   if guess==secret:
        print("Congratulations. You have guessed it.")
        print(f"\n You guessed the number on {count} times. ")
        break
   elif guess<secret:
       print("You need to guess a higher number.")
   else:
       print("You need to guess a smaller number.")