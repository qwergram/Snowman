from util import do, p, BetaScript, kill, usernames
import subprocess, time, os, os.path

p("Importing s_05!")

def s_05():
    # Don't call any other functions, it's called in the function below
    # I'm just a fucking moron and coded it like a piece of shit
    score = install_office() # 1 test 1 operation
    for x in range(2):
        BetaScript("send {LWin}")
        time.sleep(.2)
        BetaScript("send {Lwin}")
    p("Ran 3 operations 3 tests {}% pass".format((score/1)*100))


def office_login():
    do("powershell start microsoft-edge:http://aka.ms/365")
    script1 = """WinActivate, Sign in to your account
    PixelGetColor, EOffice, 1894, 283, RGB
    PixelGetColor, ELock, 358, 125, RGB
    PixelGetColor, EBar, 1957, 572, RGB

    send, !{tab}
    sleep, 500
    send, %EOffice%%ELock%%EBar%{enter}"""

    script2 = """WinActivate, Sign in to your account
    sleep, 500
    Send, {fname}.{lname}@mssummit.net{tab}
    sleep, 500
    Send, P@ssword1
    sleep 200
    send {tab}
    sleep 200
    send {space}
    sleep, 500
    send {enter}"""

    while True:
        time.sleep(5)
        if str(BetaScript(script1, True)) == str('0xEB3C000x107C100xF'):
            break
        else:
            p("Waiting 5 seconds...")

    time.sleep(.75)
    BetaScript(script2.format(fname=usernames()['fname'], lname=usernames()['lname'], tab="{tab}", space="{space}", enter="{enter}"))
    return True


def download_office_exe():
    script1 = """WinActivate, Office 365
    sleep 500
    PixelGetColor, EOfficeLogo, 525, 385, RGB ;0x0D9390F
    PixelGetColor, EUpperBar, 814, 217, RGB ;0x000000
    PixelGEtColor, ENotify, 2392, 211, RGB ; 0xF
    PixelGetColor, EInstall, 2052, 717, RGB ;0x0D9390F
    PixelGetColor, EWord, 899, 676, RGB ;0x2B579A
    PixelGetColor, EExcel, 1111, 642, RGB ;0x207346
    PixelGetColor, EOnenote, 1621, 663, RGB ;0x80397B
    ;0xD9390F0x0000000xD9390F0x2B579A0x2073460xD1B7CF
    ;0xD9390F0x0000000xD9390F0x2B579A0x2073460x80397B
    Send, !{tab}
    sleep, 500
    Send, %EOfficeLogo%%EUpperBar%%EInstall%%EWord%%EExcel%%EOnenote%%ENotify%{enter}"""

    script2 = """send, #1
    sleep 1000
    send, {tab}
    sleep, 250
    send, {tab}
    sleep, 250
    send, {tab}
    sleep, 250
    send, {tab}
    sleep, 250
    send, {tab}
    sleep, 250
    send, {tab}
    sleep, 250
    send, {tab}
    sleep, 250
    send, {tab}
    sleep, 250
    send, {tab}
    sleep, 250
    send, {tab}
    sleep, 250
    send, {tab}
    sleep, 250
    send, {tab}
    sleep, 250
    send, {tab}
    sleep, 250
    send, {tab}
    sleep, 250
    send, {tab}
    sleep, 250
    send, {tab}
    sleep, 250
    send, {tab}
    sleep, 250
    send, {tab}
    sleep, 250
    send, {tab}
    sleep, 250
    send, {tab}
    sleep, 250
    send, {tab}
    sleep, 250
    send, {tab}
    sleep, 250
    send, {space}
    sleep 250
    send, {tab}{space}
    sleep, 250
    send, {tab}{enter}"""

    while True:
        time.sleep(3)
        if str(BetaScript(script1, True)) != str("0xD9390F0x0000000xD9390F0x2B579A0x2073460x80397B0xF"):
            p("Will try again in 3 seconds...")
        else:
            break


    BetaScript(script2)

    while True:
        time.sleep(15)
        check = os.listdir("C:\\Users\\CIO\\Downloads\\")
        okay = False
        for f in check:
            if f.startswith("Setup") and "O365ProPlus" in f and f.endswith('.exe'):
                okay = f
                break
        if okay:
            break
        else:
            p("Will try again in 15 seconds...")

    kill()
    return "C:\\Users\\CIO\\Downloads\\" + f

def install_office():
    office_login()
    f = download_office_exe()
    do(f)

    while True:
        p("Checking to see if build completed...")
        time.sleep(3),
        check = os.path.exists("C:\\Program Files (x86)\\Microsoft Office\\root\\Office16")
        check = check and os.path.isfile("C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\excel.exe")
        check = check and os.path.isfile("C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\lync.exe")
        check = check and os.path.isfile("C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\msaccess.exe")
        check = check and os.path.isfile("C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\mspub.exe")
        check = check and os.path.isfile("C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\onenote.exe")
        check = check and os.path.isfile("C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\outlook.exe")
        check = check and os.path.isfile("C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\powerpnt.exe")
        check = check and os.path.isfile("C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\winword.exe")
        if check:
            time.sleep(5)
            kill("OfficeC2RClient.exe", True)
            return True
        else:
            p("Error Code: MA_365II")



if __name__ == "__main__":
    s_05()
