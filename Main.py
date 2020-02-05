from Req import Req
from Parser import parse

def main():
    with open("test.txt", 'r') as f:
        parse(f.read().splitlines())

    print()
    print(Req.fAll())

if __name__ == "__main__":
    main()
