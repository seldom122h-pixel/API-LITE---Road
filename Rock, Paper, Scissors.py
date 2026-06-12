import random


def new_game():
    print("         - INFINITE Rounds - Classic Rules - ")

    player_score = 0
    ai_score = 0

    options = {1: "rock", 2: "paper", 3: "scissors"}
    emoji = {"rock": "✊", "paper": "✋", "scissors": "✌️"}

    while True:
        random_ai_choice = random.randint(1, 3)
        computer = options[random_ai_choice]

        print("\nRock✊(1) / Paper✋(2) / Scissors✌️(3) / Exit Game(4)")
        print(f'Player score: {player_score} | AI score: {ai_score}')

        choice_r = input("Enter your choice: ")

        if choice_r not in ["1", "2", "3", "4"]:
            print("Please enter a valid choice (1-4)")
            continue

        if choice_r == "4":
            print("Returning to menu...")
            break

        player_choice_num = int(choice_r)
        player = options[player_choice_num]

        print(f'\nYou chose: {player} {emoji[player]}')
        print(f'Computer chose: {computer} {emoji[computer]}')

        # Определяем победителя
        if player == computer:
            print("Draw! 🤝")
        elif (player == "rock" and computer == "scissors") or \
                (player == "scissors" and computer == "paper") or \
                (player == "paper" and computer == "rock"):
            print("You win! 🎉")
            player_score += 1
        else:
            print("You lose... 🤖")
            ai_score += 1

        print('------------------------')


if __name__ == '__main__':
    menu = """
  == ROCK-PAPER-SCISSORS ==
-----------------------------
1. New game
2. Exit
-----------------------------
    """
    print(menu)

    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                new_game()
            elif choice == 2:
                print("Thanks for playing! See you next time 👋")
                exit()
            else:
                print("Please enter a valid choice (1 or 2)")
        except ValueError:
            print("Please enter a number (1 or 2)")