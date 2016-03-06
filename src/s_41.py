import os, sys, io, json

def p(text):
    print('[n]', text)

def s_41():
    p(current_config())
    p("Select an option: ")
    p("1. Create a Tiger Woods config file for this surface")
    p("2. Reset the config file for this surface")
    p("3. Set the config file values for this surface")
    r = input("Select the number of the choice: ")
    if r[0] == "1":
        tiger_woods()
    elif r[0] == "2":
        reset_config()
    elif r[0] == "3":
        print("If you type the name incorrectly, just hit Ctrl+C and re run this program")
        fname = input("Custom firstname: ")
        lname = input("Custom lastname: ")
        custom_config(fname, lname)
    else:
        return


def current_config():
    try:
        with io.open("C:\\Users\\CIO\\AppData\\Roaming\\config.json") as f:
            data = json.loads(f.read())
        return "\n[n] ".join(["The current config file on this surface points to:", data.get('fname'), data.get('lname')])
    except IOError:
        return "There is currently no config file on this surface."


def custom_config(fname, lname):
    with io.open("C:\\Users\\CIO\\AppData\\Roaming\\config.json", "w") as f:
        f.write(json.dumps({
            "status": "image",
            "fname": fname,
            "lname": lname
        }))


def tiger_woods():
    custom_config("Tiger", "Woods")


def reset_config():
    os.system("del C:\\Users\\CIO\\AppData\\Roaming\\config.json")


if __name__ == "__main__":
    s_41()
