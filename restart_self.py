import os
import sys


def restart_program():
    """重启当前程序， 自重启
    """
    python = sys.executable
    os.execl(python, python, *sys.argv)
