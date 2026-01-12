from imaplib import Commands
import sys


def main():
    while True:
        sys.stdout.write("$ ")
        command = input()
        if command == "help":
            print("Available commands:")
            print("help - display this help message")
            print("quit - exit the shell")
        elif command == "exit":
            sys.exit(0)
        else:
            print(f"{command}: command not found")
        pass


if __name__ == "__main__":
    main()
