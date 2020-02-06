from Req import Req
from Parser import parse
from datetime import date

def main():
    parseText()
    outputText()

    with open("Output.txt", "r") as f:
        print(f.read())

def parseText(file = "To Parse.txt"):
    with open(file, 'r') as f:
        parse(f.read().splitlines())

def outputText(file = "Output.txt"):
    with open(file, "w") as f:
        f.write(date.today().strftime("[Requirements]\n%B %d, %Y\n\n") + Req.fAll())

if __name__ == "__main__":
    main()
