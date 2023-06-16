#!/usr/bin/python3

"""How many square units of water will be retained after it rains."""


def rain(walls):
    """Function that calculates the rainwater retained."""

    if len(walls) == 0:
        return 0    
    bar_left, bar_right = 0, len(walls) - 1
    bar_left_max, bar_right_max = walls[bar_left], walls[bar_right]
    amount_water = 0

    while bar_left < bar_right:
        if bar_left_max < bar_right_max:
            bar_left += 1
            bar_left_max = max(bar_left_max, walls[bar_left])
            amount_water += bar_left_max - walls[bar_left]
        else:
            bar_right -= 1
            bar_right_max = max(bar_right_max, walls[bar_right])
            amount_water += bar_right_max - walls[bar_right]
    return amount_water
    