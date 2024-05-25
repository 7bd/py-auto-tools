#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This script is used to automatically run a list of other scripts at specified intervals.
"""

import subprocess
import time
from datetime import datetime

import pyautogui

# 225, 775, 1335, 2195
scripts = [
    # {'path': 'ocean_autoclick.py', 'time': 30, 'click': (1335, 25)},
    # {'path': 'seed_autoclick.py', 'time': 20, 'click': (1845, 25)},
    {'path': 'yescoin_autoclick.py', 'time': 5*60, 'click': (225, 25)},
    {'path': 'quack_autoclick.py', 'time': 25*60, 'click': (775, 25)},
]

while True:
    for script in scripts:
        print(f"Running {script['path']} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        pyautogui.click(*script['click'])
        time.sleep(1)

        process = subprocess.Popen(['python', script['path']])
        time.sleep(script['time'])
        if process.poll() is None:
            process.terminate()
        time.sleep(1)
