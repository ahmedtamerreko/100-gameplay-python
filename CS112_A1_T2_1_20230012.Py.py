# File: CS112_A1_T2_1_20230012
# Purpose: welcome to 100 Game ,
# this game is played between Two players the player who reaches 100 First win the game
# Author = Ahmed Tamer Shawky
# ID : 20230012


print("Welcome to 100 Game")
print("Please choose a Number Between 1 to 10")


# "is_num_valid" is a Function Check if The user Entered An Integer Number Or not and
# if he Entered An integer Number Check if This Number is Between 1 to 10 or not
def is_num_valid(checked_number):
    x = checked_number.isnumeric()
    if not x:
        return False
    else:
        n = int(checked_number)
    if 0 < n <= 10:
        return True
    else:
        return False


turn = True
Sum = 0
# Game Playing
while True:
    if turn:
        print("player1's turn")
    else:
        print("player2's turn")

    num = input()
    if not is_num_valid(num):  # Function Checking if The Number is Valid Or Not As Mentioned Above
        print("please choose valid number from 1 to 10")
        continue
    else:
        Sum += int(num)  # Adding number input to the Sum
    if Sum > 100:  # This Case will be in the End of the Game to Prevent Sum to be Greater than 100
        print("The Sum should not be greater than 100! , try again")
        Sum -= int(num)
        continue
    print("sum = ", Sum)  # Print Sum Each Time to see the New Value of it
    if Sum == 100 and turn:  # Check Who is the Winner
        print("player1 won the game")
        break
    elif Sum == 100 and not turn:
        print("player2 won the game")
        break
    if turn:  # If The Sum Did not reach 100 Yet, so it's time to Another Player to Play
        turn = False
    else:
        turn = True
# To Make Python File Display The last Message
python_file = input("Press Enter to Exit")
