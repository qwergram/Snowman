from util import do, p, BetaScript, kill, GetTaskName
import subprocess, time

p("Importing s_02!")

def s_02():
    launch_start_up_programs()
    launch_native_apps()
    p("Ran 2 interations on 5 apps (10 operations) (no tests ran to confirm)")


def launch_start_up_programs():
    warmups = [
        ["powershell start microsoft-edge:http://bing.com", "MicrosoftEdge.exe"],
        ["control.exe /name Microsoft.NetworkAndSharingCenter", None]
    ]
    for cmd, killcmd in warmups:
        for x in range(2):
            do(cmd, "ignore")
            time.sleep(2-x)
            kill(killcmd, True)


def launch_native_apps():
    launch_weather = """send, {Lwin}
    sleep, 1500
    send, Weather
    sleep, 2000
    send, {enter}"""

    launch_store = """send, #3
    sleep, 500"""

    launch_surface = """send {Lwin}
    sleep 500
    send surface
    sleep 500
    send {enter}"""

    for script in [launch_weather, launch_store, launch_surface]:
        for x in range(2):
            BetaScript(script)
            time.sleep(2-x)
            kill("ApplicationFrameHost.exe")


if __name__ == "__main__":
    s_02()
