import os, io, subprocess, json, time, urllib.request
import os.path

CONFIG = {}

def p(text):
    print('[n]', text)


def do(cmd, errors="strict"):
    assert errors in "strict ignore".split()
    if errors == "strict":
        return subprocess.check_output(cmd).decode()
    else:
        try:
            return subprocess.check_output(cmd)
        except subprocess.CalledProcessError:
            return False

def kill(image_name="", force=False):
    if image_name:
        if force:
            do("taskkill /F /IM {}".format(image_name))
        else:
            do("taskkill /IM {}".format(image_name))
    else:
        BetaScript("send !{f4}")


def config():
    global CONFIG
    if CONFIG: return CONFIG
    try:
        with open("D:\\config.json") as config:
            try:
                return json.loads(config.read().strip())
            except ValueError:
                p("Configuartion File (config.json) corrupt.")
                sys.exit("Error Code: S_4E")
    except IOError:
        p("Configuration File (config.json) missing.")
        sys.exit("Error Code: S_3E")

def key_shortcuts(fname, lname):
    if not "basic.exe" in str(do("tasklist", "ignore")):
        BetaScript("run D:\\src\\basic.exe %s %s" % (fname, lname))


def usernames():
    location = "C:\\Users\\CIO\\AppData\\Roaming\\config.json"
    try:
        with io.open(location) as c:
            c = json.loads(c.read())
        key_shortcuts(c['fname'], c['lname'])
        return c
    except IOError:
        with urllib.request.urlopen(config()['luna'] + '/' + config()['key'] + '/get') as data:
            data = data.read().decode()
        c = json.loads(data)
        with io.open(location, 'w') as c:
            c.write(str(data))
        return usernames()


class GetTaskName:

    def __init__(self):
        self.difference = []
        self.first = do("tasklist").split(" ", 1)[0]

    def second_run(self):
        self.second = do("tasklist").split(" ", 1)[0]
        for line in self.second:
            if line not in self.first:
                self.difference.append(line)


class AlphaScript:

    def __init__(self, script):
        with io.open("D:\\src\\tmp.bat", "w") as f:
            f.write(script)
        do("D:\\src\\tmp.bat")
        do("del D:\\src\\tmp.bat")


class BetaScript:

    def __init__(self, script, await_input=False):
        self.script = script + "\n".join(["^!x::Exit"])
        with io.open("D:\\src\\tmp.py", "w") as f:
            f.write(script)
        os.system('D:\\src\\happysnowman.exe D:\\src\\tmp.py')
        if await_input:
            self.await_input()
        os.system("del D:\\src\\tmp.py")

    def await_input(self):
        self.script = input("/!\: ")

    def __str__(self):
        return self.script


if __name__ == "__main__":
    print(usernames())
