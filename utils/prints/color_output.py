from typing import Callable, List
import re

RESET = "\033[0m"
BOLD = "\033[1m"
THIN = "\033[2m"
ITALIC = "\033[3m"
UNDER = "\033[4m"
CROSS = "\033[9m"

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"


def bold(string: str) -> str: return BOLD + string + RESET
def thin(string: str) -> str: return THIN + string + RESET
def italic(string: str) -> str: return ITALIC + string + RESET
def under(string: str) -> str: return UNDER + string + RESET
def cross(string: str) -> str: return CROSS + string + RESET


def red(string: str) -> str: return RED + string + RESET
def green(string: str) -> str: return GREEN + string + RESET
def yellow(string: str) -> str: return YELLOW + string + RESET
def blue(string: str) -> str: return BLUE + string + RESET
def magenta(string: str) -> str: return MAGENTA + string + RESET
def cyan(string: str) -> str: return CYAN + string + RESET


r = red
g = green
y = yellow
b = blue
m = magenta
c = cyan


def colors() -> List[Callable[[str], str]]: return [r, g, y, b, m, c]


def true_false_out(string: str, is_valid: bool) -> str:
    if is_valid:
        return g(string)
    return r(string)


def highlight(string: str, pattern: str, color: Callable[[str], str]) -> str:
    find_substrings = re.findall(pattern, string)
    for substring in find_substrings:
        string = string.replace(substring, color(substring))
    return string
