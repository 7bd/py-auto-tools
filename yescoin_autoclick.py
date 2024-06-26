#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module provides functionality for automatically moving the mouse cursor
across the screen and clicking at specific points after a certain amount of time.
"""

import asyncio
import random
import time

import pyautogui
import pygetwindow as gw

pyautogui.FAILSAFE = False


WIDTH = 201
HEIGHT = 213
STEPS_X = 3
STEPS_Y = 3
STEP_SIZE_X = WIDTH // STEPS_X
STEP_SIZE_Y = HEIGHT // STEPS_Y
CLICK_POINTS_BOOST_CHEST = [(395, 750), (180, 510), (98, 165)]
CLICK_POINTS_BOOST_RECOVERY = [(395, 750), (360, 510), (98, 165)]
SCAN_TIME = 60
HORIZONTAL_SCANS = 10


async def move_to_point(x, y, duration):
    ''' Move the mouse to the specified point on the screen. '''
    pyautogui.moveTo(x, y, duration=duration)


async def click_at_points(window):
    ''' Click the mouse at the specified points on the screen. '''
    click_points = random.choice([CLICK_POINTS_BOOST_CHEST, CLICK_POINTS_BOOST_RECOVERY])
    for point in click_points:
        x = window.left + point[0]
        y = window.top + point[1]
        pyautogui.click(x, y)
        await asyncio.sleep(2)


async def move_to_all_points():
    ''' Move the mouse to every point on the screen. '''
    try:
        telegram_window = gw.getActiveWindow()
    except IndexError:
        print("No window with title 'Telegram Web' found.")
        return

    start_x = telegram_window.left + (telegram_window.width - WIDTH) // 2
    start_y = telegram_window.top + (telegram_window.height - HEIGHT) // 2 + 30
    end_x = start_x + WIDTH
    end_y = start_y + HEIGHT

    start_time = time.time() + SCAN_TIME // 2

    last_x = start_x
    direction = 1  # 1 for right, -1 for left

    while True:
        tasks = []
        for y in range(end_y, start_y - STEP_SIZE_Y, -STEP_SIZE_Y):
            for _ in range(HORIZONTAL_SCANS):
                if direction == 1:
                    for x in range(last_x, end_x + STEP_SIZE_X, STEP_SIZE_X):
                        tasks.append(move_to_point(x, y, 0.1 if x != last_x else 0))
                    last_x = end_x
                else:
                    for x in range(last_x, start_x - STEP_SIZE_X, -STEP_SIZE_X):
                        tasks.append(move_to_point(x, y, 0.1 if x != last_x else 0))
                    last_x = start_x
                direction *= -1
        await asyncio.gather(*tasks)

        if time.time() - start_time >= SCAN_TIME:
            await click_at_points(telegram_window)
            start_time = time.time()


def main():
    ''' Main function. '''
    asyncio.run(move_to_all_points())


if __name__ == "__main__":
    main()
