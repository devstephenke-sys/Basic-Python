import json
import os

# Save/load file
SAVE_FILE = "game_save.json"

# Player state
player = {
    "name": "",
    "inventory": [],
    "location": "start"
}

# Game locations and options
story = {
    "start": {
        "text": "You are in a dark forest. Two paths lie ahead.",
        "options": {
            "1": {"desc": "Take the left path", "next": "river"},
            "2": {"desc": "Take the right path", "next": "cave"}
        }
    },
    "river": {
        "text": "You reach a river. There is a shiny sword by the bank.",
        "options": {
            "1": {"desc": "Pick up the sword", "next": "bridge", "item": "Sword"},
            "2": {"desc": "Ignore it and cross the bridge", "next": "bridge"}
        }
    },
    "cave": {
        "text": "You enter a cave and encounter a sleeping dragon.",
        "options": {
            "1": {"desc": "Sneak past the dragon", "next": "treasure"},
            "2": {"desc": "Attack the dragon", "next": "death"}
        }
    },
    "bridge": {
        "text": "You safely cross the bridge and find a small village.",
        "options": {
            "1": {"desc": "Enter the village", "next": "village"},
            "2": {"desc": "Rest outside", "next": "death"}
        }
    },
    "village": {
        "text": "The villagers welcome you. You are safe. YOU WIN!",
        "options": {}
    },
    "treasure": {
        "text": "You find a treasure chest full of gold. YOU WIN!",
        "options": {}
    },
    "death": {
        "text": "Oh no! You met a tragic end. GAME OVER.",
        "options": {}
    }
}

# Save game state
def save_game():
    with open(SAVE_FILE, "w") as f:
        json.dump(player, f)
    print("Game saved!\n")

# Load game state
def load_game():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            data = json.load(f)
            player.update(data)
        print("Game loaded!\n")
    else:
        print("No saved game found.\n")

# Play the game
def play():
    if player["name"] == "":
        player["name"] = input("Enter your name: ")

    while True:
        location = player["location"]
        scene = story[location]

        print("\n" + scene["text"])

        # Check if game ended
        if not scene["options"]:
            break

        for key, option in scene["options"].items():
            print(f"{key}. {option['desc']}")

        choice = input("Choose an option: ")
        if choice in scene["options"]:
            selected = scene["options"][choice]

            # Add item to inventory if exists
            if "item" in selected:
                player["inventory"].append(selected["item"])
                print(f"You got: {selected['item']}")

            player["location"] = selected["next"]

            # Ask to save
            save = input("Do you want to save? (y/n): ").lower()
            if save == "y":
                save_game()
        else:
            print("Invalid choice. Try again.")

    print("\nYour inventory:", player["inventory"])
    print("Thanks for playing!")

# Main menu
def main():
    while True:
        print("\n=== TEXT ADVENTURE GAME ===")
        print("1. New Game")
        print("2. Load Game")
        print("3. Quit")
        choice = input("Choose: ")

        if choice == "1":
            player["name"] = ""
            player["inventory"] = []
            player["location"] = "start"
            play()
        elif choice == "2":
            load_game()
            play()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
