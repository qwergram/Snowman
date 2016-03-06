from util import do, p, BetaScript, kill, usernames
import subprocess, time, os, os.path

from s_06 import set_pen_settings

def s_20():
    secondary__pen_settings()
    launch_onenote()


def secondary__pen_settings():
    BetaScript("send {Lwin}")
    time.sleep(.9)
    BetaScript("send surface")
    time.sleep(.5)
    BetaScript("send {enter}")
    time.sleep(.9)
    set_pen_settings()


def launch_onenote():
    BetaScript("Run C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\ONENOTE.EXE")
    time.sleep(1.5)
    BetaScript("send {enter}")
    time.sleep(1)
    kill("onenote.exe")

if __name__ == "__main__":
    s_20()
