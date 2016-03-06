from util import p, BetaScript
import subprocess, time

p("Importing s_01!")

def s_01():
    p("Detecting Windows Settings...")
    score = test_os_version() + test_internet_connection() + test_tile_positions()
    p("Ran 3 tests {}% passed".format(int((score/3)*100)))


def test_tile_positions():
    p("Determining Tile positions...")
    snowman = """Send {LWin}
    Sleep 750
    PixelGetColor, ECalendar, 550, 133, RGB
    PixelGetColor, EPhotos, 886, 357, RGB
    PixelGetColor, ENews, 1732, 595, RGB
    PixelGetColor, EOnenote, 1538, 795, RGB
    PixelGetColor, ESurface, 832, 1084, RGB
    PixelGetColor, EPaint, 1347, 1069, RGB
    send, !{tab}
    sleep, 750
    send, %ECalendar%%Ephotos%%ENews%%EOnenote%%ESurface%%EPaint%{enter}"""
    if not str(BetaScript(snowman, True)) == str("0x0078D70x0078D70xD134380x80397B0x0078D70xFCD116"):
        p("Tiles incorrectly configured!")
        return False
    return True


def test_os_version():
    p("Determining if you have the right build version...")
    is_right_build = subprocess.check_output('powershell [environment]::OSVersion.Version.Major -eq 10 -and [environment]::OSVersion.Version.Build -eq 10586', shell=True).strip().decode()
    if is_right_build != "True":
        p("You have the wrong build of Windows! (Not 10586)")
        p('Warning Code: S1W')
        p("Hit [Enter] to continue anyways...")
        p('OR')
        i("Hit [CTRL + C] to stop Snowman and reset the OS")
    return True

def test_internet_connection():
    while True:
        p("Making sure you're not connected to the internet...")
        good_internet = True
        try:
            subprocess.check_output('ping www.google.com')
        except subprocess.CalledProcessError:
            good_internet = False
            break
        if good_internet:
            p("Please disconnect from the internet!")
            p("Error Code S2W")
            p("Testing again in 5 seconds...")
            time.sleep(5)
    return True

if __name__ == "__main__":
    s_01()
