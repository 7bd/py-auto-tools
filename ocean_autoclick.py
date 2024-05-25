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
    {'coords': (376, 560), 'wait_time': 2},
    {'coords': (280, 510), 'wait_time': 20},
    {'coords': (98, 165), 'wait_time': 2},
]


async def main():
    """ Main function. """
    try:
        telegram_window = gw.getActiveWindow()
    except IndexError:
        print("No window with title 'Telegram Web' found.")
        return

    for point in points:
        pyautogui.click(
            telegram_window.left + point['coords'][0],
            telegram_window.top + point['coords'][1]
        )
        await asyncio.sleep(point['wait_time'])

if __name__ == "__main__":
    asyncio.run(main())
