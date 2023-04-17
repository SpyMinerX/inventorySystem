import json, os, datetime

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class config(object):
    def get(self, group, element):
        conf = json.load(open(os.curdir + '/config.json'))
        return conf[group][element]

def loadConfig():
    return config()
def logINFO(event, message):
    print(f"{datetime.now()} - [{event} : INFO] {message}")


def logWARN(event, message):
    print(f"{bcolors.WARNING}{datetime.now()} - [{event} : WARNING] {message}{bcolors.ENDC}")


def logERROR(event, message):
    print(f"{bcolors.FAIL}{datetime.now()} - [{event} : ERROR] {message}{bcolors.ENDC}")