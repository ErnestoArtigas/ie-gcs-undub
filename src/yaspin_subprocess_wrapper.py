"""
Code written by Ernesto Artigas.
Licence GNU General Public Licence v3.0.
"""


import os
import subprocess
from colorama_print_wrapper import print_red_text
from yaspin import yaspin


def spinner_with_subprocess_error_handling(spinner_text, subprocess_arguments):
  subprocess_arguments[0] = os.path.abspath(subprocess_arguments[0])

  with yaspin(text=spinner_text, color="green") as spinner:
    process = subprocess.Popen(subprocess_arguments, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, _ = process.communicate()

    if (process.returncode == 0):
      spinner.ok("✅")
    else:
      spinner.fail("❌")
      print_red_text(stdout.decode())
      exit(1)
