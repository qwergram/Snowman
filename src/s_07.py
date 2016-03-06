from util import do, p, BetaScript, kill, usernames, AlphaScript
import subprocess, time, os, os.path

p("Importing s_07!")

def s_07():
    set_username() # 1 operation
    p("Ran 0 checks 2 operations 0 tests")


def set_username():
    script = """
    send #{up}
    sleep 500
    click 547 350
    sleep 500
    send {fname} {lname}
    sleep 500
    send {enter}
    """

    do("control userpasswords", "ignore")
    time.sleep(2)
    BetaScript(script.format(fname=usernames()['fname'], lname=usernames()['lname'], enter='{enter}', up='{up}'))
    time.sleep(1)
    kill()


# def side_load():
#     do('powershell -ExecutionPolicy Bypass "D:\\App\\Add-AppDevPackage.ps1" -action install -bypass true -section all', 'ignore')


if __name__ == "__main__":
    s_07()
