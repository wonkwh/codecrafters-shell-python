import logging
import os
import sys

logging.basicConfig(
    level=logging.INFO,  # DEBUG까지 보이게
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)  # 모듈명 기반 로거


def find_executable(cmd: str) -> str | None:
    # Check if the command is a built-in command
    # if cmd in ["echo", "exit", "type"]:
    #     return cmd
    path_value = os.environ.get("PATH")
    if not path_value:
        return None

    for directory in path_value.split(os.pathsep):
        full_path = os.path.join(directory, cmd)

        # 실행권한 확인
        if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
            return full_path

    return None


def main():
    builtin = {
        "echo": lambda: print("echo is a shell builtin"),
        "exit": lambda: print("exit is a shell builtin"),
        "type": lambda: print("type is a shell builtin"),
    }

    while True:
        sys.stdout.write("$ ")
        command = input()
        if command == "help":
            print("Available commands:")
            print("help - display this help message")
            print("quit - exit the shell")
        elif command.__contains__("type"):
            sub_cmd = command.split(" ")[1]
            logger.debug(f"Type command received: {sub_cmd}")
            # buildin[sub_cmd] 가 없을 경우
            if sub_cmd not in builtin:
                path = find_executable(sub_cmd)
                if path is None:
                    print(f"{sub_cmd}: not found")
                else:
                    print(f"{sub_cmd} is {path}")
            else:
                builtin[sub_cmd]()
        elif command.__contains__("echo"):
            # split command space arguments
            args = command.split(" ")
            print(" ".join(args[1:]))
        elif command == "exit":
            sys.exit(0)
        else:
            print(f"{command}: command not found")
        pass


if __name__ == "__main__":
    main()
