from util import do, p, BetaScript, kill, GetTaskName
import subprocess, time, winsound

p("Importing s_04!")

def s_04():
    setup_to_internet()
    score = test_internet()

    p("Ran 1 operation 1 test {}% pass".format((score/1)*100))


def setup_to_internet():
    do("control.exe /name Microsoft.NetworkAndSharingCenter", "ignore")
    time.sleep(.75)

    script = """WinActivate, Network and Sharing Center
    sleep, 500
    IfWinActive, Network and Sharing Center
    send, #{up}
    sleep, 750
    click, 690, 380
    sleep, 750
    send, {down 2}{enter}
    sleep, 500
    send, MSFTOPEN{tab}
    sleep, 500
    send, n
    sleep, 500
    send, {tab}{space}{enter}
    sleep, 750
    send, {tab}{enter}
    sleep, 500
    send, !{f4}"""

    p("Plug in ethernet cable now if you wish to!")
    for x in range(3):
        winsound.Beep(2000, 500)
        time.sleep(.5)

    BetaScript(script)

def test_internet():
    while True:
        try:
            import urllib.request
            test = urllib.request.urlopen("http://www.google.com", timeout=3).read()
            return True
        except:
            p("Still no internet! Will try again in 3 seconds...")
            time.sleep(3)


if __name__ == "__main__":
    s_04()
