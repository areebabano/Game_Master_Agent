# from agents import function_tool
# import random

# @function_tool
# def roll_dice(sides: int = 6, count: int = 1) -> str:
#     """Roll dice with given sides and count and return the results."""
#     rolls = [random.randint(1, sides) for _ in range(count)]
#     return f"Rolled {count}d{sides}: {rolls} (Total: {sum(rolls)})"


# from agents import function_tool
# import random

# @function_tool
# def roll_dice(sides: int = 6, count: int = 1) -> str:
#     """
#     Roll a specified number of dice with a given number of sides.
    
#     Parameters:
#     - sides: Number of sides per die (default 6).
#     - count: Number of dice to roll (default 1).
    
#     Returns:
#     A string showing the individual rolls and their total sum.
#     """
#     rolls = [random.randint(1, sides) for _ in range(count)]
#     return f"Rolled {count}d{sides}: {rolls} (Total: {sum(rolls)})"


from agents import function_tool
import random

@function_tool
def roll_dice(sides: int = 6, count: int = 1) -> str:
    """
    Roll a specified number of dice with a given number of sides.
    
    Parameters:
    - sides: Number of sides per die (default 6).
    - count: Number of dice to roll (default 1).
    
    Returns:
    A string showing the individual rolls and their total sum.
    """
    # Roll 'count' dice, each with 'sides' number of sides, generating random values between 1 and 'sides'
    rolls = [random.randint(1, sides) for _ in range(count)]
    
    # Format the result string to show the individual dice rolls and their total
    return f"Rolled {count}d{sides}: {rolls} (Total: {sum(rolls)})"
