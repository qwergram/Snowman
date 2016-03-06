from util import do, p, BetaScript, kill, usernames
import subprocess, time, os, os.path

from s_08 import s_08
from s_09 import pin_items, pin_cortana, resize_cio

p("Importing s_08!")

def s_31():
    if input("Would you like to configure the start menu again? (y/N)").lower().startswith('y'):
        s_08()
        pin_cortana()
        BetaScript('send {LWin}')
        time.sleep(.9)
        resize_cio()
    if input("Would you like to configure the taskbar again? (y/N)").lower().startswith('y'):
        pin_items()


if __name__ == "__main__":
    s_31()
