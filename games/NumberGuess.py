import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("Select Difficulty Level:")
    print("1. Easy (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard (1-1000)")

    while True:
        choice = input("Enter choice (1/2/3) or 'q' to quit: ")

        if choice.lower() == 'q':
            print("Thanks for playing! Goodbye.")
            break

        if choice == '1':
            upper_limit = 50
        elif choice == '2':
            upper_limit = 100
        elif choice == '3':
            upper_limit = 1000
        else:
            print("Invalid choice. Defaulting to Medium (1-100).")
            upper_limit = 100

        secret_number = random.randint(1, upper_limit)
        attempts = 0
        guessed_correctly = False

        print(f"\nI'm thinking of a number between 1 and {upper_limit}.")

        while not guessed_correctly:
            try:
                guess = int(input("Enter your guess: "))
                attempts += 1

                if guess < secret_number:
                    print("Too low! Try again.")
                elif guess > secret_number:
                    print("Too high! Try again.")
                else:
                    print(f"Congratulations! You guessed the number in {attempts} attempts.")
                    guessed_correctly = True
            except ValueError:
                print("Invalid input. Please enter a whole number.")

        print("-" * 30)

if __name__ == "__main__":
    number_guessing_game()
