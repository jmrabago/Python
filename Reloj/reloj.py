#! /usr/bin/env python3
"""
Clock program
"""

import time

def reloj():
    while True:
        actual_time = time.strftime('%H:%M:%S')
        print(actual_time, end='\r')
        time.sleep(1)

reloj()
