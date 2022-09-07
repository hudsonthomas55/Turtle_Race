import turtle
import random

    # Sheldon is player 1
sheldon = turtle.Turtle()
sheldon.color("blue")
sheldon.shape("turtle")
sheldon.penup()
sheldon.goto(-200,100)

    # Thomasina is player 2
thomasina = sheldon.clone()
thomasina.color("purple")
thomasina.penup()
thomasina.goto(-200,-100)

    # Build Sheldon's home
sheldon.goto(200,60)
sheldon.pendown()
sheldon.circle(40)
sheldon.penup()
sheldon.goto(-200,100)

    # Build Thomasina's home
thomasina.goto(200,-140)
thomasina.pendown()
thomasina.circle(40)
thomasina.penup()
thomasina.goto(-200,-100)


    # Print Sheldon's name
sheldon.up()
sheldon.setpos(0, 0)
sheldon.down()
sheldon.color("blue")
sheldon.write("Sheldon", font=("Verdana", 12, "bold"))
sheldon.up()
sheldon.goto(-200,100)

    # Print Thomasina's name
thomasina.up()
thomasina.setpos(0, -200)
thomasina.down()
thomasina.color("purple")
thomasina.write("Thomasina", font=("Verdana", 12, "bold"))
thomasina.up()
thomasina.goto(-200,-100)


    # Start game
die = [1,2,3,4,5,6]
for i in range(20):
    if sheldon.pos() >= (200,100):
        sheldon.goto(200,100)
        print("Sheldon Wins!")
        break
    elif thomasina.pos() >= (200,-100):
        thomasina.goto(200,-100)
        print("Thomasina Wins!")
        break
    elif sheldon.pos() > (200,100):
        sheldon.goto(200,100)
        thomasina.goto(200,-60)
    elif thomasina.pos() > (200, -100):
        thomasina.goto( 200,-100)
        sheldon.goto(200,60)
    else:
            # Sheldon's Turn
        sheldon_turn = input("Player 1 press 'Enter' to roll the die ")
        die_outcome = random.choice(die)
        print("Result of the die roll is: ", die_outcome)
        print("Number of steps will be: ", (20*die_outcome))
        sheldon.fd(20*die_outcome)
            # Thomasina's Turn
        thomasina_turn = input("Player 2 press 'Enter' to roll the die ")
        die_outcome = random.choice(die)
        print("Result of the die roll is: ", die_outcome)
        print("Number of steps will be: ", (20*die_outcome))
        thomasina.fd(20*die_outcome)
        
        





