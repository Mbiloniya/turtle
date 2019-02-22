import random
import simplegui

computer_score = 0
human_score = 0
computer_choice = ""
human_choice = ""

def choice_to_number(choice):
    return {"rock":1,"paper":2,"scissor":3}[choice]

def number_on_choice(number):
    return {1:"rock",2:"paper",3:"scissor"}[number]

def random_computer_choice():
    return random.choice(["rock","paper","scissor"])

def choice_result(human_choice,computer_choice):
    global human_score
    global computer_score

    human_choice_number = choice_to_number(human_choice)
    computer_choice_number = choice_to_number(computer_choice)

    if human_choice_number == computer_choice_number:
        print("tie")
    elif (human_choice_number - computer_choice_number) %3 == 1:
        print("Computer wins")
        computer_score+=1
    else:
        print("human wins")
        human_score+=1

def rock():
    global human_choice,computer_choice
    global human_score,computer_score

    human_choice = 'rock'
    computer_choice=random_computer_choice()
    choice_result(human_choice,computer_choice)

def paper():
    global human_choice,computer_choice
    global human_score,computer_score
    human_choice = 'paper'
    computer_choice=random_computer_choice()
    choice_result(human_choice,computer_choice)

def scisscor():
    global human_choice,computer_choice
    global human_score,computer_score
    human_choice = 'scissor'
    computer_choice=random_computer_choice()
    choice_result(human_choice,computer_choice)

def draw(canvas):
    try:
        # Draw choices
        canvas.draw_text("You: " + human_choice, [10,40], 48, "Green")
        canvas.draw_text("Comp: " + computer_choice, [10,80], 48, "Red")

        # Draw scores
        canvas.draw_text("Human Score: " + str(human_score), [10,150], 30, "Green")
        canvas.draw_text("Comp Score: " + str(computer_score), [10,190], 30, "Red")

    except TypeError:
        pass

def play_rps():
    frame = simplegui.create_frame("Home", 300, 200)
    frame.add_button("Rock", rock)
    frame.add_button("Paper", paper)
    frame.add_button("Scissors", scissors)
    frame.set_draw_handler(draw)

    # Start the frame animation
    frame.start()

play_rps()

