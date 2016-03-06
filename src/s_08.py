from util import do, p, BetaScript, kill, usernames
import subprocess, time, os, os.path

p("Importing s_08!")

def s_08():
    if input("Do you want to clear tiles? If no, will start pinning operation. (y/N)").lower().startswith("y"):
        clear_tiles() # 1 operation
        time.sleep(.2)
        input("press {enter} when startmenu (AND TASKBAR DOES NOT CONTAIN ANY APPS EXCEPT FOR EDGE, EXPLORER AND STORE) is empty")


    add_first_block()
    time.sleep(.2)
    add_second_block()
    time.sleep(.2)
    add_third_block()
    time.sleep(.2)
    add_fourth_block()
    time.sleep(.2)
    add_fifth_block()
    time.sleep(.2)
    add_sixth_block()
    p("Ran 0 checks 1 operation @ 27 iterations 0 tests")


def add_sixth_block():
    Get_caught_up = [
        "photos 1 medium".split(),
        "calendar 1 medium".split(),
        "mail 1 medium".split(),
        "flipboard 1 medium".split(),
        ["camera", "1", "medium"],
        ["skype video", "1", "medium"],
        # "DUOLINGO_SPECIAL 1 medium".split(),
        # "TWITTER_SPECIAL 1 medium".split()
    ]
    script = """
    send {LWin}
    sleep 900
    send {text}
    sleep 500
    send {AppsKey}
    sleep 600
    {down}
    send {enter}
    """
    name_group = """
    send {LWin}
    sleep 900
    click 1887 557
    sleep 400
    send Get caught up{enter}
    sleep 200
    send {esc}
    """
    for search_term, menu_index, app_size in Get_caught_up:
        BetaScript(script.format(
            LWin="{LWin}",
            text=search_term,
            AppsKey="{AppsKey}",
            down=("send {down}\nsleep 200\n" * int(menu_index)),
            enter="{enter}",
        ))

    BetaScript(name_group)



def add_fifth_block():
    Play_and_explore = [
        ["new york crossword","1", "medium"],
        "xbox 1 medium".split(),
        "solitaire 1 medium".split(),
        ["fresh paint", "1", "medium"],
        ["movies & tv", "1", "medium"],
        "groove 1 medium".split()
    ]
    script = """
    send {LWin}
    sleep 900
    send {text}
    sleep 400
    send {AppsKey}
    sleep 400
    {down}
    send {enter}
    """
    name_group = """
    send {LWin}
    sleep 900
    click 1274 585
    sleep 400
    send Play and explore{enter}
    sleep 200
    send {esc}
    """
    for search_term, menu_index, app_size in Play_and_explore:
        BetaScript(script.format(
            LWin="{LWin}",
            text=search_term,
            AppsKey="{AppsKey}",
            down=("send {down}\nsleep 200\n" * int(menu_index)),
            enter="{enter}",
        ))

    BetaScript(name_group)


def add_fourth_block():
    Get_productive = [
        ["word 2016", "3", "medium"],
        "powerpoint 3 medium".split(),
        "excel 3 medium".split(),
        ["skype for business 2016", "3", "medium"],
        ["drawboard pdf", "1", "medium"],
        # "SPECIAL_CORTANA 1 medium".split(),
    ]
    script = """
    send {LWin}
    sleep 900
    send {text}
    sleep 400
    send {AppsKey}
    sleep 400
    {down}
    send {enter}
    """
    name_group = """
    send {LWin}
    sleep 900
    click 644 588
    sleep 400
    send Get productive{enter}
    sleep 200
    send {esc}
    """
    for search_term, menu_index, app_size in Get_productive:
        BetaScript(script.format(
            LWin="{LWin}",
            text=search_term,
            AppsKey="{AppsKey}",
            down=("send {down}\nsleep 200\n" * int(menu_index)),
            enter="{enter}",
        ))

    BetaScript(name_group)


def add_third_block():
    pin_weather_and_money = """
    send {LWin}
    sleep 900
    send weather
    sleep 400
    send {AppsKey}
    sleep 200
    send {down}
    sleep 200
    send {enter}
    sleep 200
    send {esc}
    sleep 200
    send {LWin}
    sleep 900
    send money
    sleep 400
    send {AppsKey}
    sleep 200
    send {down}
    sleep 200
    send {enter}
    sleep 200
    send {esc}
    """
    pin_sports_and_news = """
    send {LWin}
    sleep 900
    send sports
    sleep 400
    send {AppsKey}
    sleep 200
    send {down}
    sleep 200
    send {enter}
    sleep 200
    send {LWin}
    sleep 900
    send news
    sleep 400
    send {AppsKey}
    sleep 200
    send {down}
    sleep 200
    send {enter}
    sleep 200
    send {esc}
    """
    resize_window = """
    send {LWin}
    sleep 900
    click down 1821 654
    sleep 200
    click up 2351 594
    sleep 200
    send {esc}
    """
    resize_weather = """
    send {LWin}
    sleep 900
    click right 1976 228
    sleep 400
    send {down}
    sleep 200
    send {down}
    sleep 200
    send {right}
    sleep 300
    send {down}
    sleep 200
    send {down}
    sleep 200
    send {down}
    sleep 200
    send {enter}
    sleep 200
    send {esc}
    """
    resize_news = """
    send {LWin}
    sleep 900
    click right 2086 375
    sleep 400
    send {down}
    sleep 200
    send {down}
    sleep 200
    send {right}
    sleep 300
    send {down}
    sleep 200
    send {down}
    sleep 200
    send {down}
    sleep 200
    send {enter}
    sleep 200
    send {esc}
    """
    name_group = """
    send {LWin}
    sleep 900
    click 1883 69
    sleep 400
    send Life at a glance
    sleep 200
    send {enter}
    sleep 200
    send {esc}
    """
    Life_at_a_glance = [
        "weather 1 wide".split(),
        "money 1 medium".split(),
        "sports 1 medium".split(),
        "news 1 wide".split(),
    ]
    BetaScript(pin_weather_and_money)
    time.sleep(.2); BetaScript(resize_window)
    time.sleep(.2); BetaScript(resize_weather)
    time.sleep(.2); BetaScript(pin_sports_and_news)
    time.sleep(.2); BetaScript(resize_news)
    time.sleep(.2); BetaScript(name_group)

def clear_tiles():
    script = """
    send {Lwin}
    sleep 500

    ; Get to Tiles
    send {tab}
    sleep 200
    send {right}
    sleep 200

    send {down}
    sleep 200

    ;send {right}
    ;sleep 200

    send {AppsKey}
    sleep 200
    send {down}
    sleep 200
    send {enter}
    ; DEBUG:
    send {esc}
    sleep 200
    ;send {esc}
    sleep 200
    """

    # If run on first time, create a file called "S_08.LCK"
    # If file exists, then check with user to see if startmenu is empty

    for x in range(27):
        BetaScript(script)


def add_second_block():
    pin_outlook = """
    send {LWin}
    sleep 900
    send Outlook
    sleep 400
    send {AppsKey}
    sleep 400
    send {down}
    sleep 200
    send {down}
    sleep 200
    send {down}
    sleep 200
    send {enter}
    """
    resize_window = """
    send {LWin}
    sleep 900
    click left down 1166 712
    sleep 500
    click left up 1730 712
    """
    pin_surface = """
    send {LWin}
    sleep 200
    send {LWin}
    sleep 900
    send surface
    sleep 400
    send {AppsKey}
    sleep 400
    send {down}
    sleep 200
    send {enter}
    sleep 500
    send {LWin}
    sleep 700
    click right 1490 160
    sleep 400
    send {down}
    sleep 200
    send {down}
    sleep 200
    send {right}
    sleep 200
    send {down}
    sleep 200
    send {down}
    sleep 200
    send {down}
    sleep 200
    send {enter}
    sleep 200
    send {LWin}
    """
    NameGroup = """
    send {LWin}
    sleep 900
    click 1367 78
    sleep 300
    send Customize your device
    sleep 200
    send {enter}
    sleep 200
    send {LWin}
    """
    pin_store_and_settings = """
    send {Lwin}
    sleep 900
    send store
    sleep 400
    send {AppsKey}
    sleep 400
    send {down} ; Unlike every other native app, the option is 2 down
    sleep 200
    send {down} ; I think it's because it's pinned to the taskbar
    sleep 200
    send {enter}
    sleep 200
    send {LWin}
    sleep 900
    send settings
    sleep 400
    send {AppsKey}
    sleep 400
    send {down}
    sleep 200
    send {enter}
    sleep 200
    send {esc}
    """
    resize_store = """
    send {LWin}
    sleep 900
    click right 1258 409
    sleep 400
    send {down}
    sleep 200
    send {down}
    sleep 200
    send {right}
    sleep 200
    send {down}
    sleep 200
    send {down}
    sleep 200
    send {down}
    sleep 200
    send {enter}
    sleep 200
    send {esc}
    """
    Customize_your_device = [
        "outlook 3 medium".split(),
        "surface 1 wide".split(),
        "store 1 wide".split(),
        "settings 1 medium".split()
    ]
    BetaScript(pin_outlook)
    BetaScript(resize_window)
    BetaScript(pin_surface)
    time.sleep(0.2); BetaScript(pin_store_and_settings)
    BetaScript(resize_store)
    time.sleep(0.2); BetaScript(NameGroup)

def add_first_block():
    script = """
    send {LWin}
    sleep 900
    send {text}
    sleep 400
    send {AppsKey}
    sleep 400
    {down}
    send {enter}
    """

    resize_script = """
    send {LWin}
    sleep 750
    click, right, 672, 134
    sleep 500
    send {down}
    sleep 200
    send {down}
    sleep 200
    send {right}
    sleep 200
    send {size_down}
    send {enter}
    """

    name_group = """
    ;send {Lwin}
    click 607 66
    sleep 800
    send Welcome to the CIO Summit{!}{enter}
    sleep 200
    send {LWin}
    """

    CIOApp = """
    send {LWin}
    sleep 900
    click 157, 1111
    sleep 400
    click 437 59
    sleep 500
    send {LWin}
    sleep 1000
    send {LWin}
    sleep 900
    click 157, 1111
    sleep 400
    click down 498 230
    sleep 200
    click up 498 624
    sleep 200
    click right 62 529
    sleep 400
    send {down}
    sleep 200
    send {enter}
    sleep 200
    send {esc}
    """

    Welcome_to_the_CIO_Summit_BANG = [
        ["north america cio summit apportal", "1", "4"],
        # ["onenote 2016", "3", "medium"],
        "edge 2 medium".split(),
    ]

    # BetaScript(CIOApp)



    for search_term, menu_index, app_size in Welcome_to_the_CIO_Summit_BANG:
        time.sleep(.2)
        BetaScript(script.format(
            LWin="{LWin}",
            text=search_term,
            AppsKey="{AppsKey}",
            down=("send {down}\nsleep 200\n" * int(menu_index)),
            enter="{enter}",
        ))

    # Resize CIO App
    BetaScript(resize_script.format(
        LWin="{LWin}",
        down="{down}",
        right="{right}",
        enter="{enter}",
        size_down=("send {down}\nsleep 200\n" * int(4))
    ))

    # Add onenote back up
    BetaScript(script.format(
        LWin="{LWin}\nsleep 200\nsend {LWin}",
        text="Onenote 2016",
        AppsKey="{AppsKey}",
        down=("send {down}\nsleep 200\n" * int(3)),
        enter="{enter}\nsleep 200\nsend {lwin}",
    ))
    time.sleep(.2)
    BetaScript(name_group)
    BetaScript("send {esc}")


if __name__ == "__main__":
    s_08()
