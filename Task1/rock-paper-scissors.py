import random

ROCK = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''


PAPER = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''


SCISSORS = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


print("\n")
print("******************* ROCK PAPER SCISSORS GAME *******************")
print("\n")

PLAY=True

while(PLAY):

    choice=int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors: \n"))
    print("Your choice \n")

    if choice==0:
        print(ROCK)

    elif choice==1:
        print(PAPER)

    else :
        print(SCISSORS)

    comp_choice=random.randint(0,2)

    print("Computer's Choose :")

    if comp_choice ==0:
        print(ROCK)
    elif comp_choice==1:
        print(PAPER)
    else :
        print(SCISSORS)

    #0=rock 1=paper 2=scisscors

    if choice== comp_choice:
        print("Game Drawn\n")
    elif choice==0 and comp_choice==1:
        print("You lose. AI is taking over humans!!\n")
    elif choice==0 and comp_choice==2:
        print("YOu win. AI needs to work harder to attain human level!\n")
    elif choice==1 and comp_choice==0:
        print("You Win. AI needs to work harder to attain human level!\n")
    elif choice==1 and comp_choice==2:
        print("You lose. AI is taking over humans!!\n")
    elif choice==2 and comp_choice==0:
        print("You lose. AI is taking over humans!!\n")
    else :
        print("You win. AI needs to work harder to attain human level!\n")

    cont=input("Do you want to play more(Yes/No)\n")

    if(cont=="No"):
        PLAY=False

print(" ******************* THANK YOU FOR PLAYING! *******************\n")
