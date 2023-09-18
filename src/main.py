"""
Code written by Ernesto Artigas.
Licence GNU General Public Licence v3.0.
"""


import dotenv
import os
import shutil
from colorama_print_wrapper import print_red_text, print_green_text
from managing_cia import unpack_cia, repack_cia
from optparse import OptionParser
from yaspin import yaspin


dotenv.load_dotenv()


def replace_european_romfs_files(japanese_path_name, european_path_name):
  entries = sorted(os.listdir(european_path_name))

  with yaspin(text="Replacing european romfs files by japanese one...", color="green") as spinner:
    try:
      for entry_name in entries:
        entry_name_splitted = entry_name.split('.')
        suffix = entry_name_splitted[0][-2:]

        if (
            suffix == os.getenv('SUFFIX_ENGLISH') or
            suffix == os.getenv('SUFFIX_GERMAN') or
            suffix == os.getenv('SUFFIX_FRENCH') or
            suffix == os.getenv('SUFFIX_ITALIAN') or
            suffix == os.getenv('SUFFIX_SPANISH')
            ):
            japanese_filename = '{}.{}'.format(entry_name_splitted[0][slice(len(entry_name_splitted[0])-3)], entry_name_splitted[1])

            if (os.path.isfile(os.path.join(japanese_path_name, japanese_filename))):
              shutil.copyfile(os.path.join(japanese_path_name, japanese_filename), os.path.join(european_path_name, entry_name))

      spinner.ok("✅")
    except Exception as error:
      spinner.fail("❌")
      print_red_text(str(error))
      exit(1)

  return


def main():
  parser = OptionParser(usage="main.py -j path/to/japanese_rom.cia -e path/to/european_rom.cia")
  parser.add_option(
    "-j", "--japanese-rom", action="store", type="string", dest="japanese_rom", help="Path of the japanese rom", metavar="JAPANESE_ROM"
  )
  parser.add_option(
    "-e", "--european-rom", action="store", type="string", dest="european_rom", help="Path of the european rom", metavar="EUROPEAN_ROM"
  )
  (options, _) = parser.parse_args()

  if (
      options.japanese_rom == None or
      options.european_rom == None
    ):
    print_red_text("Missing argument, you need to provide the path of both rom.")
    print_green_text(f"Usage > {parser.usage}")
    exit(1)

  if (
      options.japanese_rom.isdigit() or
      options.european_rom.isdigit()
    ):
    print_red_text("The arguments provided are not string. You need to enter valid arguments.")
    print_green_text(f"Usage > {parser.usage}")
    exit(1)

  absolute_path_japanese_rom = os.path.abspath(options.japanese_rom)
  japanese_rom_file = absolute_path_japanese_rom.split(os.path.sep)[-1]
  japanese_rom_file_name = japanese_rom_file.split('.')[0]

  absolute_path_european_rom = os.path.abspath(options.european_rom)
  european_rom_file = absolute_path_european_rom.split(os.path.sep)[-1]
  european_rom_file_name = european_rom_file.split('.')[0]

  print("Unpacking japanese rom...")
  unpack_cia(japanese_rom_file_name, absolute_path_japanese_rom)
  print_green_text("Unpacking japanese rom completed.", "\n")

  print("Unpacking european rom...")
  unpack_cia(european_rom_file_name, absolute_path_european_rom)
  print_green_text("Unpacking european rom completed.", "\n")


  replace_european_romfs_files(f"{japanese_rom_file_name}_unpacked/ExtractedRomFS/snd/product/stream", f"{european_rom_file_name}_unpacked/ExtractedRomFS/snd/product/stream")


  print("Repacking european rom...")
  repack_cia(european_rom_file_name)
  print_green_text("Repacking european rom completed.")


  print("Deleting temporary folder...")
  shutil.rmtree(f"{japanese_rom_file_name}_unpacked", ignore_errors=True)
  shutil.rmtree(f"{european_rom_file_name}_unpacked", ignore_errors=True)
  print_green_text("Temporary folder deleted.")


  if (os.path.isfile(f"{european_rom_file_name}_edited.cia")):
    print_green_text(f"Rom exported : {european_rom_file_name}_edited.cia")
  else:
    print_red_text("The file wasn't created, please read the logs.")


if __name__ == "__main__":
  main()
