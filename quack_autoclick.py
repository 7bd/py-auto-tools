#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script is used to automatically click on a list of predefined points on the screen.
"""

import asyncio

import pyautogui
import pygetwindow as gw

pyautogui.FAILSAFE = False


points = [
    {'coords': (198, 418), 'wait_time': 1}, # Egg 1
    {'coords': (262, 772), 'wait_time': 1}, # Harvest Egg
    {'coords': (342, 414), 'wait_time': 1}, # Egg 2
    {'coords': (262, 772), 'wait_time': 1}, # Harvest Egg
    {'coords': (268, 492), 'wait_time': 1}, # Egg 3
    {'coords': (262, 772), 'wait_time': 1}, # Harvest Egg
    {'coords': (320, 550), 'wait_time': 1}, # Dismiss
    {'coords': (407, 517), 'wait_time': 1}, # Dismiss
    {'coords': (270, 720), 'wait_time': 0.5}, # Boss Duck
    {'coords': (270, 720), 'wait_time': 0.5}, # Boss Duck
    {'coords': (270, 720), 'wait_time': 0.5}, # Boss Duck
    {'coords': (205, 625), 'wait_time': 1}, # Claim
]


async def main():
    """ Main function. """
    try:
        telegram_window = gw.getActiveWindow()
    except IndexError:
        print("No window with title 'Telegram Web' found.")
        return

    while True:
        for point in points:
            pyautogui.click(
                telegram_window.left + point['coords'][0],
                telegram_window.top + point['coords'][1]
            )
            await asyncio.sleep(point['wait_time'])
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())
