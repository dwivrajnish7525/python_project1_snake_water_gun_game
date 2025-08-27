#Snake Water Gun Game
import random
'''
Snake->1
Water->0
Gun->-1
''' 
print("************************************")
print("-------(Snake,Water,Gun Game)-------")
print('''            RULES
🐍 Snake drinks Water → Snake wins
💧 Water drowns Gun → Water wins
🔫 Gun kills Snake → Gun wins''')
print("------------------------------------")
total_rounds = int(input("Enter number of rounds you want to play: "))
user_score = 0
comp_score = 0
draws = 0
roundno = 1
for roundno in range(1, total_rounds + 1):
    print(f"                Round:{roundno}        ")
    roundno+=1
    print("                 START             ")
    print("S->Snake🐍\nW->Water💧\nG->Gun🔫\nE->Exit Game👋🚪")
    print("___________________________")
    computer=random.choice([-1,1,0])
    User_input=input("Enter your choice:")
    User_input=User_input.lower()
    if(User_input=="e"):
        break
    elif User_input not in ['s','w','g','e']:
        print("Invalid Choice ❌")
        continue
    else:
        User_input_dict={'s':1,'w':0,'g':-1}
        User_input_dict_reverse={1:'Snake🐍',0:'Water💧',-1:'Gun🔫'}
        you=User_input_dict[User_input]
        print(f"You chose:{User_input_dict_reverse[you]}\nComputer chose:{User_input_dict_reverse[computer]}")
        if(computer==you):
            print("Its a draw🤝😐")
            draws += 1
        elif(computer==-1 and you==1):
            print("You Lose!😞💔")
            comp_score += 1
        elif(computer==-1 and you==0):
            print("You Win!🏆🎉")
            user_score += 1
        elif(computer==1 and you==-1):
            print("You Win!🏆🎉")
            user_score += 1
        elif(computer==1 and you==0):
            print("You Lose!😞💔")
            comp_score += 1
        elif(computer==0 and you==1):
            print("You Win!🏆🎉")
            user_score += 1
        elif(computer==0 and you==-1):
            print("You Lose!😞💔")
            comp_score += 1
        else:
            print("Something went wrong!")
        print(f"📊 Current Score → You: {user_score} | Computer: {comp_score} | Draws: {draws}")
        print("_____________________________________________________")
print("Game Over 👋🚪")
print(f"Final Score → You: {user_score} | Computer: {comp_score} | Draws: {draws}")
if user_score > comp_score:
    print("Overall Winner: You 🎉🏆")
elif comp_score > user_score:
    print("Overall Winner: Computer 🤖💻")
else:
    print("Overall Result: Draw 🤝😐")

