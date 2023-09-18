"""
Code written by Ernesto Artigas.
Licence GNU General Public Licence v3.0.
"""


import dotenv
import os
from colorama_print_wrapper import print_red_text, print_green_text
from yaspin_subprocess_wrapper import spinner_with_subprocess_error_handling


dotenv.load_dotenv()


def create_directory(directory_name):
  path = os.path.join(os.getcwd(), directory_name)
  try:
    os.mkdir(path)
  except OSError as error:
    raise error


def extracting_ccis(file_name, absolute_file_path):
  spinner_with_subprocess_error_handling("Extracting Decrypted CCIs...",
    [
      os.getenv("CTRTOOL_PATH"),
      f"--contents={file_name}_unpacked/DecryptedApp", absolute_file_path
    ]
  )


def renaming_ccis(file_name):
  ccis = sorted(os.listdir("{}_unpacked".format(file_name)))
  for i in range(len(ccis)):
    os.rename("{}_unpacked/{}".format(file_name, ccis[i]), "{}_unpacked/DecryptedPartition{}.bin".format(file_name, i))


def extracting_decrypted_partition_0(file_name):
  spinner_with_subprocess_error_handling("Extracting DecryptedPartition0.bin...",
    [
      os.getenv("3DSTOOL_PATH"), "-xvtf", "cxi", f"{file_name}_unpacked/DecryptedPartition0.bin",
      "--header", f"{file_name}_unpacked/HeaderNCCH0.bin",
      "--exh", f"{file_name}_unpacked/DecryptedExHeader.bin", "--exh-auto-key",
      "--exefs", f"{file_name}_unpacked/DecryptedExeFS.bin", "--exh-auto-key", "--exefs-top-auto-key",
      "--romfs", f"{file_name}_unpacked/DecryptedRomFS.bin","--romfs-auto-key",
      # "--logo", f"{file_name}_unpacked/LogoLZ.bin",
      "--plain", f"{file_name}_unpacked/PlainRGN.bin",
    ]
  )


def extracting_decrypted_partition_1(file_name):
  spinner_with_subprocess_error_handling("Extracting DecryptedPartition1.bin...",
    [
      os.getenv("3DSTOOL_PATH"), "-xvtf", "cfa", f"{file_name}_unpacked/DecryptedPartition1.bin",
      "--header", f"{file_name}_unpacked/HeaderNCCH1.bin",
      "--romfs", f"{file_name}_unpacked/DecryptedManual.bin","--romfs-auto-key",
    ]
  )


def extracting_decrypted_exe_fs(file_name):
  spinner_with_subprocess_error_handling("Extracting DecryptedExeFS.bin...",
    [
      os.getenv("3DSTOOL_PATH"), "-xvtfu", "exefs", f"{file_name}_unpacked/DecryptedExeFS.bin",
      "--header", f"{file_name}_unpacked/HeaderExeFS.bin",
      "--exefs-dir", f"{file_name}_unpacked/ExtractedExeFS"
    ]
  )


def extracting_decrypted_rom_fs(file_name):
  spinner_with_subprocess_error_handling("Extracting DecryptedRomFS.bin...",
    [
      os.getenv("3DSTOOL_PATH"), "-xvtf", "romfs", f"{file_name}_unpacked/DecryptedRomFS.bin",
      "--romfs-dir", f"{file_name}_unpacked/ExtractedRomFS",
    ]
  )


def extracting_decrypted_manual(file_name):
  spinner_with_subprocess_error_handling("Extracting DecryptedManual.bin...",
    [
      os.getenv("3DSTOOL_PATH"), "-xvtf", "romfs", f"{file_name}_unpacked/DecryptedManual.bin",
      "--romfs-dir", f"{file_name}_unpacked/ExtractedManual",
    ]
  )


def repacking_decrypted_rom_fs(file_name):
  spinner_with_subprocess_error_handling("Repacking DecryptedRomFS.bin...",
    [
      os.getenv("3DSTOOL_PATH"), "-cvtf", "romfs", f"{file_name}_unpacked/DecryptedRomFS.bin",
      "--romfs-dir", f"{file_name}_unpacked/ExtractedRomFS",
    ]
  )


def repacking_decrypted_exe_fs(file_name):
  spinner_with_subprocess_error_handling("Repacking DecryptedExeFS.bin...",
    [
      os.getenv("3DSTOOL_PATH"), "-cvtfz", "exefs", f"{file_name}_unpacked/DecryptedExeFS.bin",
      "--header", f"{file_name}_unpacked/HeaderExeFS.bin",
      "--exefs-dir", f"{file_name}_unpacked/ExtractedExeFS"
    ]
  )


def repacking_decrypted_manual(file_name):
  spinner_with_subprocess_error_handling("Repacking DecryptedManual.bin...",
    [
      os.getenv("3DSTOOL_PATH"), "-cvtf", "romfs", f"{file_name}_unpacked/DecryptedManual.bin",
      "--romfs-dir", f"{file_name}_unpacked/ExtractedManual",
    ]
  )


def repacking_decrypted_partition_0(file_name):
  spinner_with_subprocess_error_handling("Repacking DecryptedPartition0.bin...",
    [
      os.getenv("3DSTOOL_PATH"), "-cvtf", "cxi", f"{file_name}_unpacked/DecryptedPartition0.bin",
      "--header", f"{file_name}_unpacked/HeaderNCCH0.bin",
      "--exh", f"{file_name}_unpacked/DecryptedExHeader.bin", "--exh-auto-key",
      "--exefs", f"{file_name}_unpacked/DecryptedExeFS.bin", "--exh-auto-key", "--exefs-top-auto-key",
      "--romfs", f"{file_name}_unpacked/DecryptedRomFS.bin","--romfs-auto-key",
      # "--logo", f"{file_name}_unpacked/LogoLZ.bin",
      "--plain", f"{file_name}_unpacked/PlainRGN.bin",
    ]
  )


def repacking_decrypted_partition_1(file_name):
  spinner_with_subprocess_error_handling("Repacking DecryptedPartition1.bin...",
    [
      os.getenv("3DSTOOL_PATH"), "-cvtf", "cfa", f"{file_name}_unpacked/DecryptedPartition1.bin",
      "--header", f"{file_name}_unpacked/HeaderNCCH1.bin",
      "--romfs", f"{file_name}_unpacked/DecryptedManual.bin","--romfs-auto-key",
    ]
  )


def repacking_edited_cia(file_name):
  spinner_with_subprocess_error_handling("Repacking edited cia file...",
    [
      os.getenv("MAKEROM_PATH"), "-target", "p", "-ignoresign", "-f", "cia", 
      "-content", f"{file_name}_unpacked/DecryptedPartition0.bin:0:0x00",
      "-content", f"{file_name}_unpacked/DecryptedPartition1.bin:1:0x01",
      "-o", f"{file_name}_edited.cia"
    ]
  )


def unpack_cia(file_name, absolute_file_path):
  # Create directory for unpacking the CIA.
  try:
    create_directory(f"{file_name}_unpacked")
    print_green_text(f"Created {file_name}_unpacked folder.")
  except Exception as error:
    print_red_text(str(error))
    exit(1)

  # Extract Decrypted CCIs.
  extracting_ccis(file_name, absolute_file_path)

  # Renaming CCIs.
  renaming_ccis(file_name)

  # Extract DecryptedPartition0.bin.
  extracting_decrypted_partition_0(file_name)

  # Extract DecryptedPartition1.bin.
  extracting_decrypted_partition_1(file_name)

  # Extract DecryptedRomFS.bin.
  extracting_decrypted_rom_fs(file_name)

  # # Extract DecryptedExeFS.bin.
  # extracting_decrypted_exe_fs(file_name)
  # # Extract DecryptedManual.bin.
  # extracting_decrypted_manual(file_name)

  # Delete unused files.
  os.remove(f"{file_name}_unpacked/DecryptedPartition0.bin")
  os.remove(f"{file_name}_unpacked/DecryptedPartition1.bin")
  os.remove(f"{file_name}_unpacked/DecryptedRomFS.bin")


def repack_cia(file_name):
  # Repacking DecryptedRomFS.bin.
  repacking_decrypted_rom_fs(file_name)

  # Repacking DecryptedPartition0.bin.
  repacking_decrypted_partition_0(file_name)

  # Repacking DecryptedPartition1.bin.
  repacking_decrypted_partition_1(file_name)

  # Repacking Edited CIA.
  repacking_edited_cia(file_name)

  # # Repacking DecryptedExeFS.bin.
  # repacking_decrypted_exe_fs(file_name)
  # # Repacking DecryptedManual.bin.
  # repacking_decrypted_manual(file_name)