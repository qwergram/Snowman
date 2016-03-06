from util import do, p, BetaScript, kill, usernames
import subprocess, time, os, os.path

p("Importing s_06!")

def s_06():
    change_weather() # 1 operation
    launch_store() # 2 checks 1 operation
    update_surface_app(False) # 1 test 2 operations
    p("USER CHECK:")
    p("IF THE BUTTON SAYS \"UPDATE\" THEN CLICK ON IT AND THEN CLOSE THE STORE ONCE UPDATE COMPLETED. DO NOT INSTALL OTHER UPDATES.")
    p("IF THE BUTTON SAYS \"OPEN\" CLOSE THE STORE WITHOUT UPDATING OR OPENING ANYTHING.")
    p("WHEN COMPLETE, PUSH {ENTER}")
    input("...")
    # start_surface_app() # 1 operation 1 test
    # update_surface_app(False) # 1 test 2 operations (Run a second time because need to test to see if surface app is ready)
    # set_pen_settings() # 1 operation
    p("Ran 2 checks 8 operations 3 tests")


def change_weather():
    script = """send, {Lwin}
    sleep, 1500
    send, Weather App
    sleep, 2000
    send, {enter}
    sleep, 2000
    send, {tab 2}98052{enter}"""

    BetaScript(script)
    time.sleep(2)
    kill()


def launch_store():
    scripts = [""";0
    send, #3""",
    """ ;1
    WinActivate, Store
    send #{up}
    sleep 500
    click 2308, 129
    sleep 200
    send Surface""",
    """
    WinActivate, Store
    sleep 300
    send {down}
    sleep 200
    send {down}
    sleep 200
    send {down}
    sleep 200
    send {enter}""",
    """
    WinActivate, Store
    sleep, 500
    PixelGetColor, ESurfaceLogo, 2194, 342, RGB
    MouseMove, 2194, 342
    sleep 200
    send #4
    sleep 200
    send %ESurfaceLogo%
    send, {enter}
    """
    ]

    # Launch surface app then kill
    BetaScript(scripts[0])
    time.sleep(1.5)
    kill()

    # Test if surface icon appears, if not, kill everything and start again
    while True:
        time.sleep(1)
        BetaScript(scripts[0]) # just opens store
        time.sleep(0.5)
        BetaScript(scripts[1]) #
        time.sleep(1)
        if str(BetaScript(scripts[3], True)) == str('0x0078D7'):
            BetaScript(scripts[2])
            return
        else:
            kill("ApplicationFrameHost.exe")

def update_surface_app(click):

    script = """WinActivate, Store
    sleep 500
    PixelGetColor, ESurfaceLogo, 186, 247, RGB ;0x0078D7
    PixelGetColor, EBlueBlob, 937, 275, RGB ;0x054ABC
    PixelGetColor, EInstall, 267, 929, RGB ;0xFFFFFF
    PixelGetColor, EComments, 943, 1194, RGB ;0xFFFFFF
    Send, !{tab}
    sleep, 500
    ; 0x00787D70x054ABC0xFFFFFF0xFFFFFF
    Send, %ESurfaceLogo%%EBlueBlob%%EInstall%%EComments%{enter}"""

    for x in range(5):
        time.sleep(3)
        if str(BetaScript(script, True)) == str("0x0078D70x054ABC0xF0xF"):
            # BetaScript("WinActivate Store\nsleep 500\nsend {enter}")
            if click:
                BetaScript("WinActivate Store\nclick, 267, 929")
            return True
        else:
            p("Trying again in 3 seconds...")
    else:
        launch_store()
        update_surface_app()

def start_surface_app():
    script1 = """send {Lwin}
    sleep 500
    send surface
    sleep 500
    send {enter}
    sleep 2000
    send #{up}"""

    script2 = """WinActivate, Surface
    sleep 750
    PixelGetColor, ESurface, 593, 298, RGB ; 0x0E0E0E
    PixelGetColor, EBar, 57, 631, RGB ; 0xF2F2F2
    PixelGetColor, EBlue, 1472, 1504, RGB ; 0x0078D7
    send #4
    sleep 500
    send %ESurface%%EBar%%EBlue%{enter}"""

    BetaScript(script1) # Launched in Windows store checks

    while True:
        time.sleep(3)
        if str(BetaScript(script2, True)) == str("0x0E0E0E0xF2F2F20x0078D7"):
            return True
        else:
            p("Waiting 3 seconds...")


def set_pen_settings():
    test = """WinActivate, Surface
    sleep 500
    send #{up}
    sleep 500
    PixelGetColor, UError, 1630, 1568
    sleep 200
    send !{tab}
    sleep 500
    send %UError%{enter}
    """

    script = ["""WinActivate, Surface
    sleep, 500
    send #{up}
    sleep 500
    send {down}
    sleep 200
    send {enter}
    """, """
    WinActivate, Surface
    sleep 500
    send #{up}
    sleep 500
    send {tab}
    sleep 200
    send {tab}
    sleep 200
    send {enter}
    sleep 200
    send {down}
    sleep 200
    send {down}
    sleep 200
    send {down}
    sleep 200
    send {down}
    sleep 200
    send {enter}
    sleep 400
    send {tab}
    sleep 200
    send {enter}
    sleep 1000
    send C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\ONENOTE.EXE
    sleep 200
    send {enter}"""]

    BetaScript(script[0])
    time.sleep(2)
    while True:
        if str(BetaScript(test, True)) == str('0xF'):
            break
        else:
            input("PLEASE PAIR PEN! HIT {ENTER} WHEN YOU DO.")
            time.sleep(3)

    BetaScript(script[1])
    time.sleep(2)

    kill("SurfaceApp.exe", True)



if __name__ == "__main__":
    s_06()
