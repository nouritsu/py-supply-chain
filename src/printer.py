from colorama import Fore
import sys


def pinfo(msg):
    print(f"[{Fore.BLUE}INFO{Fore.RESET}]: {msg}", file=sys.stderr)


def pwarning(msg):
    print(f"[{Fore.YELLOW}WARNING{Fore.RESET}]: {msg}", file=sys.stderr)


def perror(msg, code):
    print(f"[{Fore.RED}ERROR{Fore.RESET}]: {msg}", file=sys.stderr)
    sys.exit(code)
