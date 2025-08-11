import random


def sorting_print(group, element):
    if not hasattr(sorting_print, 'group_style'):
        sorting_print.group_style = {}
    if group not in sorting_print.group_style:
        sorting_print.group_style[group] = random.randint(31, 37)

    print(f'\033[1;{sorting_print.group_style[group]}m{group} '
          f'\033[0;{sorting_print.group_style[group]}m{element}\033[m')