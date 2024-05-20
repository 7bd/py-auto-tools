#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This script is used to automatically run a list of other scripts at specified intervals.
"""

import subprocess
import time

scripts = [
    {'path': 'ocean_autoclick.py', 'time': 40},
    {'path': 'yescoin_autoclick.py', 'time': 2*60*60 + 2*60},
]

while True:
    for script in scripts:
        process = subprocess.Popen(['python', script['path']])
        time.sleep(script['time'])
        if process.poll() is None:
            process.terminate()
        time.sleep(1)
