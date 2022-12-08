"""
  John Schiltz.
  I wanted to do it both ways
"""

LB_KG_CONVERSION = 2.20462
WEIGHT_CLASS_M = {
    49: "Light flyweight",
    52: "Flyweight",
    56: "Bantomweight",
    60: "Lightweight",
    64: "Light welterweight",
    69: "Welterweight",
    75: "Middleweight",
    81: "Light heavyweight",
    91: "Heavyweight",
}
WEIGHT_CLASS_F = {
    48: "Light flyweight",
    51: "Flyweight",
    54: "Bantomweight",
    57: "Lightweight",
    60: "Light welterweight",
    64: "Welterweight",
    69: "Middleweight",
    75: "Light heavyweight",
    81: "Heavyweight",
}

MAX_WEIGHT_CLASS = {"man": "Super heavyweight", "woman": "Heavyweight"}

WEIGHT_CLASSES = {"man": WEIGHT_CLASS_M, "woman": WEIGHT_CLASS_F}


def get_weight_class(weight: int, gender: str) -> str:
    """return weight class name for correct weight and gender

    Args:
        weight (int): weight in kg
        gender (str): "male" or "female"

    Returns:
        str: weight class
    """
    if gender not in WEIGHT_CLASSES.keys():
        print("Please enter correct gender")
        return None

    for w, c in WEIGHT_CLASSES.get(gender).items():
        if weight < w:
            return c
    else:
        return MAX_WEIGHT_CLASS.get(gender)


def get_weight_class_if(weight: int, gender: str) -> str:
    """return weight class name for correct weight and gender

    Args:
        weight (int): weight in kg
        gender (str): "male" or "female"

    Returns:
        str: weight class
    """
    if gender == "man":
        if weight < 49:
            return "Light flyweight"
        elif weight < 52:
            return "Flyweight"
        elif weight < 56:
            return "Bantomweight"
        elif weight < 60:
            return "Lightweight"
        elif weight < 64:
            return "Light welterweight"
        elif weight < 69:
            return "Welterweight"
        elif weight < 75:
            return "Middleweight"
        elif weight < 81:
            return "Light heavyweight"
        elif weight < 91:
            return "Heavyweight"
        else:
            return "Super heavyweight"
    elif gender == "woman":
        if weight < 48:
            return "Light flyweight"
        elif weight < 51:
            return "Flyweight"
        elif weight < 54:
            return "Bantomweight"
        elif weight < 57:
            return "Featherweight"
        elif weight < 60:
            return "Lightweight"
        elif weight < 64:
            return "Welterweight"
        elif weight < 69:
            return "Light middleweight"
        elif weight < 75:
            return "Middleweight"
        elif weight < 81:
            return "Light heavyweight"
        else:
            return "Heavyweight"


if __name__ == "__main__":
    try:
        weight = int(input("Please enter your weight in lbs: "))
    except:
        print("Please enter a number")
        exit()

    gender = input('Please enter if you are a "man" or "woman": ')

    print(get_weight_class_if(weight / LB_KG_CONVERSION, gender))
    print(get_weight_class(weight / LB_KG_CONVERSION, gender))
