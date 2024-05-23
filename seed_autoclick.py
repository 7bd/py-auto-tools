#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script is used to automatically click on a list of predefined points on the screen.
"""

import asyncio

import pyautogui
import pygetwindow as gw

pyautogui.FAILSAFE = False

TELEGRAM_WINDOW_WIDTH = 502
TELEGRAM_WINDOW_HEIGHT = 902

points = [
    {'coords': (280, 660), 'wait_time': 2},
    {'coords': (380, 660), 'wait_time': 2},
    {'coords': (260, 510), 'wait_time': 10},
]


async def main():
    """ Main function. """
    try:
        telegram_window = gw.getWindowsWithTitle("Telegram Web")[0]
        telegram_window.activate()
        telegram_window.resizeTo(TELEGRAM_WINDOW_WIDTH, TELEGRAM_WINDOW_HEIGHT)
    except IndexError:
        print("No window with title 'Telegram Web' found.")
        return

    pyautogui.click(telegram_window.left + 260, telegram_window.top + 25)
    await asyncio.sleep(2)

    for point in points:
        pyautogui.click(
            telegram_window.left + point['coords'][0],
            telegram_window.top + point['coords'][1]
        )
        await asyncio.sleep(point['wait_time'])

if __name__ == "__main__":
    asyncio.run(main())
