import random, art
def display_result():
    print(f"Your cards: {mylist}， current score: {sum(mylist)}")
    print(f"Computer's first card: {computer_list[0]}")
    continu = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    play_game = True
    if continu == 'n':
        while sum(computer_list) < 16:
            computer_list.append(random.choice(cards))
            if sum(computer_list) > 21 and 11 in computer_list:
                computer_list[computer_list.index(11)] = 1

        play_game = result()

    return continu, play_game

def result():
    print(f"Your final cards: {mylist}, final score: {sum(mylist)}")
    print(f"Computer's final cards: {computer_list}, final score: {sum(computer_list)} ")

    if sum(mylist) >21:
        print("You lose.😔/(ㄒoㄒ)/~~")
    elif sum(mylist) > sum(computer_list) or sum(computer_list) > 21:
        print("You win！ 😃")
    elif sum(mylist) == sum(computer_list):
        print("Draw. ")
    else:
        print("You lose.😔/(ㄒoㄒ)/~~")

    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y"

    return play_game

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
play_game = True
while play_game:
    print("\n"*20)
    print(art.logo)

    mylist = random.choices(cards, k = 2)
    computer_list = random.choices(cards, k = 2)

    continu, play_game = display_result()

    while continu == 'y':
        mylist.append(random.choice(cards))
        if sum(mylist) > 21 and 11 in mylist:
            mylist[mylist.index(11)] = 1
        elif sum(mylist) > 21:
            play_game = result()
            break
        continu, play_game = display_result()

