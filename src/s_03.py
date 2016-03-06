from util import do, p, BetaScript, kill, GetTaskName
import subprocess, time

p("Importing s_03!")

def s_03():
    launch_edge()
    change_edge()
    score = test_edge()
    p("Ran 2 operations, 1 test {}% pass".format((score/1)*100))


def test_edge():
    script = """WinActivate, Start
    sleep, 500
    send, #1
    sleep, 1500
    send, ^l
    sleep, 200
    send, ^c
    sleep, 200
    send !{f4}
    sleep, 500
    send, ^v{enter}"""
    skip = True
    while True:
        BetaScript(script)
        # NEVER sleep after running tests.
        if skip:
            test_result = "Norton Pengra is cool"
            skip = False
        else:
            test_result = input("/!\: ")

        p("Processing data...")
        if test_result != "http://aka.ms/cioS16":
            p("Error Code: MA2")
        else:
            break
    return True


def change_edge():
    script = """WinActivate, Start
    sleep, 750
    Send, #{up}
    sleep, 500
    send, {tab}
    sleep 200
    send, {tab}
    sleep 200
    send, {tab}
    sleep 200
    send, {tab}
    sleep 200
    send, {tab}
    sleep 200
    send, {tab}
    sleep 200
    send, {tab}
    sleep 200
    send, {tab}
    sleep 200
    send {enter}
    sleep, 500
    Send, {up}
    sleep, 200
    send, {enter}

    sleep, 750
    send, {tab 5}
    sleep, 500
    send, {space}
    sleep, 500

    send, {tab}{space}
    sleep, 500
    send, {down 2}
    sleep 200
    send {enter}
    sleep, 500
    send, {tab}
    sleep 200
    send, {tab}
    sleep 200
    send, {enter}
    sleep, 500
    send, +{tab}
    sleep, 700
    send, aka.ms/cioS16{enter}"""
    BetaScript(script)
    time.sleep(1.2)
    kill()

def launch_edge():
    do("powershell start microsoft-edge:http://aka.ms/365")
    time.sleep(.5)

if __name__ == "__main__":
    s_03()
