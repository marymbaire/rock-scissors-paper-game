import random


def game():
    mylist = ["R", "S", "P"]
    while mylist:
        import re
        player = input("What's your choice? 'R' for rock, 'P' for paper, 's' for scissors:")
        if not re.match("^[R,,S, P]*$", player):
            print("Error! Only letters R,S or P allowed!")
        print(random.choice(mylist))
        CPU = random.choice(mylist)
        print("Player:", player, "CPU:", CPU)
        if (player == 'R' and CPU == 'R') or (player == 'S' and CPU == 'S') or (player == 'P' and CPU == 'P'):
            print("its a tie")
        elif (player == 'R' and CPU == 'S') or (player == 'S' and CPU == 'P') or (player == 'P' and CPU == 'R'):
            print("YAAY!! you has won")
        elif (player == 'S' and CPU == 'R') or (player == 'P' and CPU == 'S') or (player == 'R' and CPU == 'P'):
            print("OOPS!! computer has won")


game()






