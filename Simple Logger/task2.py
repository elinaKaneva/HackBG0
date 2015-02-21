import datetime
import requests


levels_text = {
    1: "INFO",
    2: "WARNING",
    3: "PLSCHECKFFS"
}


def create_log(level, message):
    today = datetime.datetime.today()
    todayISO = today.isoformat().split(".")[0]
    rule = "{lvl}::{time}::{mess}"
    return rule.format(lvl=levels_text[level], time=todayISO, mess=message)


class MyLogger:

    def __init__(self, level, message):
        self.level = level
        self.message = message

    def log(self):
        pass


class ConsoleLogger(MyLogger):

    def log(self):
        print(create_log(self.level, self.message))


class FileLogger(MyLogger):

    def log(self):
        with open("log.txt", "a") as myfile:
            myfile.write(create_log(self.level, self.message))
            myfile.write('\n')
            myfile.close()


class HTTPLogger(MyLogger):

    def log(self):
        payload = {"mess": create_log(self.level, self.message)}
        print(payload)
        r = requests.post("http://192.168.0.106:3000", data=payload)
        print(r)


c = ConsoleLogger(2, "test 2")
c.log()

f1 = FileLogger(1, "line 1")
f1.log()
f2 = FileLogger(2, "line 2")
f2.log()

h = HTTPLogger(3, "test 3")
h.log()
