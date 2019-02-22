import random
user1 = input("Hi,my name is :")
user2 = input("hi %s,you are playing with computer"%user1)
def compare(u1,u2):
            if u1 == u2:
                print("Tie")
            elif u1 == "rock":
                if u2 == "scissor":
                    print("winner is",user1)
                else:
                    print("winner is computer")
            elif u1 =="paper":
                if u2 == "rock":
                    print("winner is",user1)
                else:
                    print("winner is computer")
            elif u1 =="scissor":
                if u2 == "paper":
                    print("winner is",user1)
                else:
                    print("winner is computer")
            else:
                print("you enter a wrong choice")
for i in range(10):
    user1_choice = input("%s,do you pick any one in between rock,paper and scissor"%user1)
    user2_choice = random.choice(["rock","paper","scissor"])
    if user1_choice == "exit":
        break
    else:
        compare(user1_choice,user2_choice)
