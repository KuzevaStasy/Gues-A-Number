import random

print("Choose difficulty level:")
print("1 - Easy (1 to 50, unlimited attempts)")
print("2 - Medium (1 to 100, 10 attempts)")
print("3 - Hard (1 to 200, 7 attempts)")

difficulty = input("Enter 1, 2, or 3: ")

if difficulty == "1":
    max_num = 50
    attempts = None  # unlimited
elif difficulty == "2":
    max_num = 100
    attempts = 10
elif difficulty == "3":
    max_num = 200
    attempts = 7
else:
    print("Invalid choice, defaulting to Medium.")
    max_num = 100
    attempts = 10

computer_number = random.randint(1, max_num)
tries = 0

while True:
    player_input = input(f"Guess a number between 1 and {max_num}: ")

    # prevent crashing if input is not a number
    if not player_input.isdigit():
        print("Please enter a valid number!")
        continue

    player_number = int(player_input)
    tries += 1

    if player_number == computer_number:
        print(f"You guessed it in {tries} tries!")
        break
    elif player_number < computer_number:
        print("Too Low!")
    else:
        print("Too High!")

    # check attempts only if there is a limit
    if attempts and tries >= attempts:
        print(f"Out of attempts! The number was {computer_number}.")
        break
