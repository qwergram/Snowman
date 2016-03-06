from util import do, p, BetaScript, kill, usernames
import subprocess, time, os, os.path

p("Importing s_09!")

def s_09():
    pin_items()
    pin_cortana()
    BetaScript("send {Lwin}")
    time.sleep(.9)
    resize_cio()
    p("Ran 2 checks 2 operations 5 iterations 0 tests")


def resize_cio():
    script = """
    send {LWin}
    sleep 900
    click 723, 303
    sleep 900
    send #{up}
    """

    BetaScript(script)
    time.sleep(1)
    kill()


def pin_cortana():
    script = """
    send {LWin}
    sleep 900
    click 84, 1111
    sleep 500
    click 443 50
    sleep 200
    send {LWin}
    sleep 800
    send {LWin}
    sleep 900
    click 84, 1111
    sleep 500
    click 443 50
    sleep 500
    click 195, 293
    sleep 500
    click down 60 371
    sleep 500
    click up 1004 915
    """
    BetaScript(script)


def pin_items():
    script = """
    send {Lwin}
    sleep 900
    send %s
    sleep 500
    send {AppsKey}
    sleep 300
    send {down %s}
    sleep 200
    send {enter}
    sleep 200
    send {esc}
    """
    order = [
        ["outlook 2016", 4],
        ["skype for business 2016", 4],
        ["onenote 2016", 4],
        ["word 2016", 4],
        ["excel 2016", 4],
        ["powerpoint 2016", 4],
    ]

    for term, menu in order:
        time.sleep(.2)
        BetaScript(script % (term, menu))



def load_extra_apps():
    apps = [
        "cortana",
        "duolingo - learn languages",
        "twitter",
    ]


if __name__ == "__main__":
    s_09()
