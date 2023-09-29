import random


def roll_dice(dice_code):
    """Rolls a dice based on the given dice code."""

    # Split the dice code by 'D' (e.g., 2D10 -> ['2', '10'])
    parts = dice_code.split('D')

    # Number of rolls; default is 1 if not specified
    num_rolls = 1 if parts[0] == '' else int(parts[0])

    # If there's a modifier (e.g., +10 or -5), separate it
    if '+' in parts[1]:
        dice, modifier = parts[1].split('+')
        modifier = int(modifier)
    elif '-' in parts[1]:
        dice, modifier = parts[1].split('-')
        modifier = -int(modifier)
    else:
        dice = parts[1]
        modifier = 0

    # Roll the dice and sum the results with the modifier
    total = sum([random.randint(1, int(dice)) for _ in range(num_rolls)]) + modifier
    return total


def main():
    """Main function to execute the dice rolling simulator."""

    # Valid dice types
    valid_dice = ['D3', 'D4', 'D6', 'D8', 'D10', 'D12', 'D20', 'D100']

    while True:
        try:
            # Get the user's dice code
            dice_code = input("Enter your dice code (e.g., 2D10+20 or D6 or q to quit): ").upper()

            # Exit the program if the user types 'q'
            if dice_code == 'Q':
                break

            # Check if the dice part (without number of rolls and modifier) is valid
            if any(d in dice_code for d in valid_dice):
                result = roll_dice(dice_code)
                print(f"Result of {dice_code} is: {result}")
            else:
                print(
                    "Invalid dice code! Make sure you're using a valid dice type (D3, D4, D6, D8, D10, D12, D20, D100).")

        except ValueError:
            print("Error in your input! Make sure you're following the correct format.")
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()