from IPython.display import clear_output

#Choice display method
def disply_list(choicelist):
    print(choicelist)

choicelist = [n for n in range(10)]
disply_list(choicelist)


# User choice
def user_choice():
    choice = 'wrong'
    within_range = False

    while choice.isdigit() == False or within_range == False:
        choice = input("Please enter number (0-10) : ")
        if choice.isdigit() == False:
            print("Sorry that is not a digit!")
        if choice.isdigit() == True:
            if int(choice) in range(0,10):
                within_range = True
            else:
                print("Please enter the number in the range(0-10)")
                within_range = False

    return int(choice)

value = user_choice()
# print(value)
game_list = [0,1,2]
def display_game(game_lsit):
    print("Here is the game list")
    print(game_lsit)

display_game(game_list)

# Position choice
def position_choice():
    choice = 'wrong'
    while choice not in ['0','1','2']:
        clear_output()
        print("Sorry you did not choice valid input (0,1,2)")
    return int(choice)
# value = position_choice()
# print(value)

# Replacement choice
def replacemment_choice(game_list,position):
    user_placement = input("type a string to place at the posation : ")
    game_list[position] = user_placement
    return game_list

value = replacemment_choice(choicelist,2)
print(value)

# Board graphic
board_list = ['X','O','X','O','X','O','X','O','X']
def display_board(board):
    print(board[0],'|',board[1],'|',board[2])
    print('----------')
    print(board[3],'|', board[4],'|', board[5])
    print('----------')
    print(board[6],'|', board[7],'|', board[8])
display_board(board_list)