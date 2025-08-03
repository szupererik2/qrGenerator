import json
from colorGen import generateColors

def choose_color(filename):
    with open(filename, 'r') as file:
        color_pairs = json.load(file)

    print("Available colors:")
    for idx, pair in enumerate(color_pairs):
        print(f"{idx}: {pair['name']}")
    print("r: Random color")
    
    while True:
        choice = input("Enter the color ID you want to select (or 'r' for random): ").strip().lower()

        if choice == 'r':
            primary, complement = generateColors()
            print(f"Randomly generated colors: Primary {primary}, Complement {complement}")
            return primary, complement

        try:
            choice_id = int(choice)
            if 0 <= choice_id < len(color_pairs):
                selected = color_pairs[choice_id]
                print(f"You selected {selected['name']}")
                return selected['primary'], selected['complement']
            else:
                print("Invalid ID, try again.")
        except ValueError:
            print("Please enter a valid integer ID or 'r' for random.")