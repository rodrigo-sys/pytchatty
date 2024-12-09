#!/bin/python

import sys
import pytchat
import shutil
import random
import signal
from colorama import Fore, init
# from colorama import Fore, Style, init

init(autoreset=True)
terminal_size = shutil.get_terminal_size()
video_id = sys.argv[1]

assigned_colors = {}
def getRandomColor():
    fore = list(vars(Fore))
    # fore.remove('__doc__')
    color_name = random.choice(fore)
    return getattr(Fore, color_name)

def assignColor(author_name):
    if author_name not in assigned_colors:
        color = getRandomColor()
        assigned_colors[author_name] = color
    else:
        color = assigned_colors[author_name]

    return color

def updateTerminalSize(_, __):
    global terminal_size
    terminal_size = shutil.get_terminal_size()

def printChat():
    chat = pytchat.create(video_id=video_id)
    # chat = pytchat.create(video_id=video_id, seektime=2800)
    while chat.is_alive():
        for c in chat.get().sync_items():
            signal.signal(signal.SIGWINCH, updateTerminalSize)

            print(f"{assignColor(c.author.name) + '『' + c.author.name + '』'}")
            # print(f"{assignColor(c.author.name) + '[' + c.author.name + ']'}")

            if c.type == "superChat":
                print(Fore.LIGHTYELLOW_EX + f'{c.message}')
            else:
                print(f'{c.message}')

            print('-' * terminal_size.columns)
            # print('- ' * (terminal_size.columns // 2))

def main():
    printChat()

if __name__ == "__main__":
    main()
