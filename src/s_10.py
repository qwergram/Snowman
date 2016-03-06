from util import do, p, BetaScript, kill, usernames
import subprocess, time, os, os.path

p("Importing s_10!")

def s_10():
    setup_onenote()
    accept_onenote_terms()
    winup()
    p("Ran 2 checks 2 operations 5 iterations 0 tests")


def setup_onenote():
    BetaScript("Run C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\ONENOTE.EXE")

    kill()
    time.sleep(2)
    BetaScript("send {right}\nsleep 200\nsend {enter}")
    time.sleep(1)
    BetaScript("send a")
    time.sleep(1)
    kill("onenote.exe")
    BetaScript("send {enter}")



def accept_onenote_terms():
    full = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\ONENOTE.EXE"
    BetaScript("""
    send {LWin}
    sleep 900
    send onenote 2016
    sleep 500
    send {enter}
    """)
    p("Don't touch anything!")
    time.sleep(4.5)
    kill()



def winup():
    update = """
    send {LWin}
    sleep 900
    send winup
    sleep 500
    send {enter}
    """
    BetaScript(update)


if __name__ == "__main__":
    s_10()
