
import random


def roll_dice(dice_code):
    """
    Simulates a dice roll based on the provided dice notation.

    :param str dice_code: Dice notation string, e.g., '3D6+2' for rolling a 6-sided dice three times and adding 2 to the result.

    :rtype: int, str
    :return: Computed dice roll result, or 'Wrong Input' if provided notation is invalid.
    """
    dice_type = ["D3", "D4", "D6", "D8", "D10", "D12", "D20", "D100"]
    for dice in dice_type:
        if dice in dice_code:
            try:
                multiply, modifier = dice_code.split(dice)
            except ValueError:
                return "Wrong input"
            dice_value = int(dice[1:])
            break
    else:
        return "Wrong input"

    try:
        multiply = int(multiply) if multiply else 1
    except ValueError:
        return "Wrong input"

    try:
        modifier = int(modifier) if modifier else 0
    except ValueError:
        return "Wrong input"

    return sum([random.randint(1, dice_value) for _ in range(multiply)]) + modifier


if __name__ == '__main__':
    print(roll_dice("2D10+10"))
    print(roll_dice("D6"))
    print(roll_dice("2D3"))
    print(roll_dice("D12-1"))
    print(roll_dice("DD34"))
    print(roll_dice("4-3D6"))