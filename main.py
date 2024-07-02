import random
'''
1 is for Snake
-1 is for water
0 is for gun
'''

computer = random.choice([-1,0,1])
you = input("Enter your choice: ")
youDict = {"snake":1,"water":-1,"gun":0}
reverseDict = {1:"snake",-1:"water",0:"gun"}
younum = youDict[you]

print(f"You Choose {reverseDict[you]}\nComputer choose {reverseDict[computer]}")

if(computer == you):
    print("Match Draw")

if(computer == -1 and you == 1):
    print("You Win")

elif(computer == -1 and you == 0):
    print("You Loose")

elif(computer == 1 and you == -1):
    print("You Loose")

elif(computer == 1 and you == 0):
    print("You Win")

elif(computer == 0 and you == 1):
    print("You Loose")

elif(computer == 0 and you == -1):
    print("You Loose")

else:
    print("Something went wrong")