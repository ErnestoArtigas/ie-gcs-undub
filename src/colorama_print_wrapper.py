"""
Code written by Ernesto Artigas.
Licence GNU General Public Licence v3.0.
"""


import colorama

def print_colored_text(color, content):
  print(color + content + colorama.Style.RESET_ALL)


def print_red_text(content):
  print_colored_text(colorama.Fore.RED, content)


def print_green_text(content):
  print_colored_text(colorama.Fore.GREEN, content)
