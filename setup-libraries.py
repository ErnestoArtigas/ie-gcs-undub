"""
Code written by Ernesto Artigas.
Licence GNU General Public Licence v3.0.
"""


import dotenv
import os
import platform
import sys
import tarfile
# Add to the sys path the src directory for accessing its modules.
sys.path.append(os.path.join(os.getcwd(), "src"))
from colorama_print_wrapper import print_red_text
from downloader import download_files, unzip
from yaspin import yaspin


dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv()


def extract_tar_gz_file(lib_path, tar_gz_file):
  with yaspin(text=f"{tar_gz_file} extracting...", color="green") as spinner:
    try:
      tar = tarfile.open(os.path.join(lib_path, tar_gz_file), "r:gz")
      tar.extractall(lib_path)
      tar.close()
      os.remove(os.path.join(lib_path, tar_gz_file))
      spinner.ok("✅")
    except Exception as error:
      spinner.fail("❌")
      print_red_text(str(error))
      exit(1)


def extract_zip_file(lib_path, zip_file):
  with yaspin(text=f"{zip_file} extracting...", color="green") as spinner:
    try:
      unzip(os.path.join(lib_path, zip_file), lib_path)
      os.remove(os.path.join(lib_path, zip_file))
      spinner.ok("✅")
    except Exception as error:
      spinner.fail("❌")
      print_red_text(str(error))
      exit(1)


def create_download_links_dictionary():
  download_links = {}

  match platform.system():
    # None of the three programs have different x64 - x86 or arm packages.
    case "Linux":
      download_links["3DSTOOL_PATH"] = "https://github.com/dnasdw/3dstool/releases/download/v1.2.6/3dstool_linux_x86_64.tar.gz"
      download_links["CTRTOOL_PATH"] = "https://github.com/3DSGuy/Project_CTR/releases/download/ctrtool-v1.2.0/ctrtool-v1.2.0-ubuntu_x86_64.zip"
      download_links["MAKEROM_PATH"] = "https://github.com/3DSGuy/Project_CTR/releases/download/makerom-v0.18.3/makerom-v0.18.3-ubuntu_x86_64.zip"

    case "Windows":
      download_links["3DSTOOL_PATH"] = "https://github.com/dnasdw/3dstool/releases/download/v1.2.6/3dstool.zip"
      if (platform.architecture()[0] == "64bit"):
        download_links["CTRTOOL_PATH"] = "https://github.com/3DSGuy/Project_CTR/releases/download/ctrtool-v1.2.0/ctrtool-v1.2.0-win_x64.zip"
      else:
        download_links["CTRTOOL_PATH"] = "https://github.com/3DSGuy/Project_CTR/releases/download/ctrtool-v1.2.0/ctrtool-v1.2.0-win_x86.zip"
      download_links["MAKEROM_PATH"] = "https://github.com/3DSGuy/Project_CTR/releases/download/makerom-v0.18.3/makerom-v0.18.3-win_x86_64.zip"

    case "Darwin":
      download_links["3DSTOOL_PATH"] = "https://github.com/dnasdw/3dstool/releases/download/v1.2.6/3dstool_macos_x86_64.tar.gz"
      if (platform.processor() == "i386"):
        download_links["CTRTOOL_PATH"] = "https://github.com/3DSGuy/Project_CTR/releases/download/ctrtool-v1.2.0/ctrtool-v1.2.0-macos_x86_64.zip"
        download_links["MAKEROM_PATH"] = "https://github.com/3DSGuy/Project_CTR/releases/download/makerom-v0.18.3/makerom-v0.18.3-macos_x86_64.zip"
      else:
        download_links["CTRTOOL_PATH"] = "https://github.com/3DSGuy/Project_CTR/releases/download/ctrtool-v1.2.0/ctrtool-v1.2.0-macos_arm64.zip"
        download_links["MAKEROM_PATH"] = "https://github.com/3DSGuy/Project_CTR/releases/download/makerom-v0.18.3/makerom-v0.18.3-macos_arm64.zip"

  return download_links


def set_env_variable(key, value):
  os.environ[key] =  value
  dotenv.set_key(dotenv_file, key, os.environ[key])


def assign_specific_os_executable_to_dictionary(dictionary, key):
  match platform.system():
    case "Linux" | "Darwin":
      dictionary[key] = f"./lib/{key.split('_')[0].lower()}"
    case "Windows":
      dictionary[key] = f"./lib/{key.split('_')[0].lower()}.exe"
  return dictionary[key]


def main():
  download_links = create_download_links_dictionary()

  download_files("lib", list(download_links.values()))

  # Assign the specific os executable of the downloaded libraries.
  for key in download_links:
    download_links[key] = assign_specific_os_executable_to_dictionary(download_links, key)

  lib_path = os.path.join(os.getcwd(), "lib")
  archive_files = sorted(os.listdir(lib_path))

  # Separate tar.gz from zip files for different extractions.
  tar_gz_files = list(filter((lambda x: "tar.gz" in x), archive_files))
  zip_files = list(filter((lambda x: "zip" in x), archive_files))

  for tar_gz_file in tar_gz_files:
    extract_tar_gz_file(lib_path, tar_gz_file)

  for zip_file in zip_files:
    extract_zip_file(lib_path, zip_file)

  # Update the env file with the right executable.
  for key in download_links:
    set_env_variable(key, os.path.abspath(download_links[key]))


if __name__ == "__main__":
  main()