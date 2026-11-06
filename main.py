import random

if __name__ == '__main__':
    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

    Scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''

    game_images = [rock, paper, Scissors]

    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    invalid_choice = False
    if 0 <= user_choice <= 2:
        print(game_images[user_choice])
    else:
        print("You typed an invalid number, you lose!")
        invalid_choice = True

    if not invalid_choice:
        computer_choice = random.randint(0,2)
        print(f"Computer chose: ")
        print(game_images[computer_choice])

        if user_choice == 0 and computer_choice == 2:
            print("You win!")
        elif computer_choice == 0 and user_choice == 2:
            print("You lose!")
        elif computer_choice > user_choice:
            print("You lose!")
        elif user_choice > computer_choice:
            print("You win!")
        elif computer_choice == user_choice:
            print("It's a draw!")