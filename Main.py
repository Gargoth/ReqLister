from Req import Req
from Parser import parse
from datetime import date

def main():
    with open("test.txt", 'r') as f:
        parse(f.read().splitlines())

    print(Req.fAll())
    outputText("your momma.txt")

def outputText(file):
    with open(file, "w") as f:
        f.write(date.today().strftime("[Requirements]\n%B %d, %Y\n\n") + Req.fAll())

if __name__ == "__main__":
    main()
