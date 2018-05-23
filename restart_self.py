import os
import sys


def restart_program():
    # 自重启
    python = sys.executable
    print(sys.argv)
    os.execl(python, python, *sys.argv)


if __name__ == '__main__':
    restart_program()