#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module provides functionality for arranging Telegram windows on the screen.
"""

import pyautogui
import pygetwindow as gw

pyautogui.FAILSAFE = False

window_sizes = [
    {'width': 544, 'height': 904},
    {'width': 544, 'height': 904},
    # {'width': 544, 'height': 904},
    # {'width': 544, 'height': 904},
]

START_X = 0
START_Y = 0


def main():
    """ Main function. """
    all_windows = gw.getAllWindows()
    telegram_windows = [window for window in all_windows if window.title.startswith("Telegram")]

    current_x = START_X
    for i, window in enumerate(telegram_windows):
        if i < len(window_sizes):
            window.resizeTo(window_sizes[i]['width'], window_sizes[i]['height'])
            window.moveTo(current_x, START_Y)
            current_x += window_sizes[i]['width']


if __name__ == "__main__":
    main()
