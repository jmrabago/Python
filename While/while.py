#!/usr/bin/env python3

"""
WHILE
"""

from datetime import datetime

datetime.now().second
wait_until = datetime.now().second + 2

while datetime.now().second != wait_until:
    print('Still waiting!')

print(f'We are at {wait_until} seconds!')

# Pass
while datetime.now().second != wait_until:
    pass

print(f'We are at {wait_until} seconds!')

# Break
while datetime.now().second != wait_until:
    print(f'We are at {wait_until} seconds!')
    break

# Continue
while datetime.now().second != wait_until:
    if datetime.now().second < wait_until:
        continue
    break
