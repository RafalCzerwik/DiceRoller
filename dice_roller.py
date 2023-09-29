import random
import re


def roll_the_dice(dice_code):
    """Simulates a dice roll based on the provided dice code."""

    # Checking if the dice code matches the pattern
    match = re.match(r'(\d*)D(\d+)([+-]\d+)?', dice_code)
    if not match:
        raise ValueError("Wrong input.")

    # Extracting values from the matched pattern
    num_rolls = int(match.group(1)) if match.group(1) else 1
    dice_type = int(match.group(2))
    modifier = int(match.group(3)) if match.group(3) else 0

    # Checking if the dice type is valid
    if dice_type not in [3, 4, 6, 8, 10, 12, 20, 100]:
        raise ValueError("Unknown dice type.")

    # Simulating the rolls
    result = sum(random.randint(1, dice_type) for _ in range(num_rolls)) + modifier

    return result


if __name__ == '__main__':
    # List of sample dice codes
    sample_dice_codes = ["2D10+10", "D6", "2D3", "D12-1", "DD34", "4-3D6"]

    for dice_code in sample_dice_codes:
        try:
            print(f"Result for {dice_code}: {roll_the_dice(dice_code)}")
        except ValueError as e:
            print(f"Error for {dice_code}: {e}")
