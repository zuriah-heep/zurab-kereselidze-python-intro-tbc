from random import randrange

def rps():
    my_list = ['R', 'P', 'S']
    return my_list[randrange(3)]

def play(user, comp):
    if user != comp:
        print(user, "vs", comp)
        if (user == 'R' and comp == 'S') or (user == 'S' and comp == 'P') or (user == 'P' and comp == 'R'):
            print("You win")
        else:
            print("You lose")

def main():
    user = input("Please input you choice: ").upper()
    if user not in "RPS":
        print("Wrong input")
        exit(1)

    comp = rps()

    if user != comp:
        play(user, comp)
    else:
        print(user, "vs", comp)
        user = input("You tie. Try one more time: ").upper()
        comp = rps()

        if user != comp:
            play(user, comp)
        else:
            print(user, "vs", comp)
            print("You tie again")

if __name__ == "__main__":
    main()