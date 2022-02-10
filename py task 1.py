def Input_move1():
    n = input("\nEnter  move for Player 1 -")
    return n


def Input_move2():
    n = input("\nEnter  move for Player 2 -")
    return n


def Input_combination_attack():
    n = input("\nEnter the move combination for attack: ")
    return n


def Input_combination_split():
    n = input("\nEnter the move combination for split: ")
    return n


def current_status(lhand_1, rhand_1, lhand_2, rhand_2):
    print("\nCurrent status :")
    print("Player1- %s %s" % (lhand_1, rhand_1))
    print("Player2- %s %s" % (lhand_2, rhand_2))


def working():
    lhand_1 = 1
    rhand_1 = 1
    lhand_2 = 1
    rhand_2 = 1

    current_status(lhand_1, rhand_1, lhand_2, rhand_2)

    num = 1
    while(True):
        if(num % 2 != 0):
            move_of_player = Input_move1().upper()
        if(num % 2 == 0):
            move_of_player = Input_move2().upper()

        if(move_of_player == "A"):
            attack_combination = Input_combination_attack().upper()

            flag = 1
            for i in range(len(attack_combination)):
                if(attack_combination[i] != " " and flag == 1):
                    left_move = attack_combination[i]
                    flag += 1

                if(attack_combination[i] != " " and flag == 2):
                    right_move = attack_combination[i]

            if(num % 2 != 0):
                if(left_move == "R" and right_move == "L"):
                    lhand_2 += rhand_1
                elif(left_move == "L" and right_move == "R"):
                    rhand_2 += lhand_1
                elif(left_move == "R" and right_move == "R"):
                    rhand_2 += rhand_1
                elif(left_move == "L" and right_move == "L"):
                    lhand_2 += lhand_1

            elif(num % 2 == 0):
                if(left_move == "R" and right_move == "L"):
                    lhand_1 += rhand_2
                elif(left_move == "L" and right_move == "R"):
                    rhand_1 += lhand_2
                elif(left_move == "R" and right_move == "R"):
                    rhand_1 += rhand_2
                elif(left_move == "L" and right_move == "L"):
                    lhand_1 += lhand_2

        elif(move_of_player == "S"):
            split_combination_of_player = Input_combination_split().upper()
            print(split_combination_of_player)
            slag = 1

            for i in range(len(split_combination_of_player)):
                if(split_combination_of_player[i] != " " and slag == 1):
                    split_move = split_combination_of_player[i]
                    slag += 1

                elif(split_combination_of_player[i] != " " and slag == 2):
                    fst_hand = ord(split_combination_of_player[i])-48
                    slag += 1

                elif(split_combination_of_player[i] != " " and slag == 3):
                    scnd_hand = ord(split_combination_of_player[i])-48
                else:
                    pass

            if(num % 2 != 0):
                lhand_1 = fst_hand
                rhand_1 = scnd_hand
            elif(num % 2 == 0):
                lhand_2 = fst_hand
                rhand_2 = scnd_hand

        if(lhand_1 >= 5):
            lhand_1 = 0
        if(rhand_1 >= 5):
            rhand_1 = 0
        if(lhand_2 >= 5):
            lhand_2 = 0
        if(rhand_2 >= 5):
            rhand_2 = 0

        if(lhand_1 == 0 and rhand_1 == 0):
            print("Player2 Winner")
            current_status(lhand_1, rhand_1, lhand_2, rhand_2)
            break

        elif(lhand_2 == 0 and rhand_2 == 0):
            print("Player1 Winner")
            current_status(lhand_1, rhand_1, lhand_2, rhand_2)
            break

        else:
            current_status(lhand_1, rhand_1, lhand_2, rhand_2)

        num += 1


def restart_game():

    restart = input(" Play again?(yes/no):\n>>").lower()
    if restart == "yes":
        main()

    else:
        exit()


def main():
    working()
    restart_game()


main()
