from sys import argv as args
from create_pass import gen_password


# -l,--length=<len>
# -nn, --no-numbers
# -ns,--no-symbols

def print_help():
    print("\n\nWelcome to PassGen")
    print("\n", "-"*40)
    print("-h, --help - help")
    print("-l, --length=<len> - length of password")
    print("-nn, --no-numbers - no numbers")
    print("-ns, --no-symbols - no symbols\n")


def main():
    _len = 8
    _symbols = True
    _numbers = True

    if "-h" in args or "--help" in args:
        print_help()
        return
    if "-nn" in args or "--no-numbers" in args:
        _numbers = False
    if "-ns" in args or "--no-symbols" in args:
        _symbols = False
    for arg in args:
        if "--length" in arg:
            _len = int(arg[len("--length")+1:])
            break
        elif "-l" in arg:
            _len = int(arg[3:])
            break

    print(f"your password is: {gen_password(_len,_numbers,_symbols)}")


if __name__ == '__main__':
    main()
