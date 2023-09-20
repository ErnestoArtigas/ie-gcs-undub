"""
Code written by Ernesto Artigas.
Licence GNU General Public Licence v3.0.
"""


import os
import requests
from colorama_print_wrapper import print_red_text, print_green_text
from tqdm import tqdm
from urllib.parse import unquote
from zipfile import ZipFile


def get_request_from_link(link):
  request = requests.get(link)
  if request.status_code != 200:
    request.raise_for_status()
  return request


def extract_decode_filename(url):
  return unquote(url.split("/")[-1])


def download_file(path, link):
  request = get_request_from_link(link)
  filename = extract_decode_filename(link)
  total_size = int(request.headers.get("content-length"))
  try:
    with open(os.path.join(path, filename), 'wb') as file:
      with tqdm(
          total=total_size,
          ncols=100,
          unit="B",
          unit_scale=True,
          desc=filename,
          initial=0,
          ascii=False,
          colour="green"
        ) as progress_bar:
        for chunk in request.iter_content(chunk_size=1024):
          if chunk:
            file.write(chunk)
            progress_bar.update(len(chunk))
  except Exception as error:
    raise (error)


def download_files(directory_name, link_array):
  try:
    if (os.path.exists(os.path.join(os.getcwd(), directory_name))):
      for element in link_array:
        download_file(os.path.join(os.getcwd(), directory_name), element)
      print_green_text("Finished downloading all files.")
    else:
      print_red_text(f"This path is incorrect : {os.path.join(os.getcwd(), directory_name)}")
  except Exception as error:
    print_red_text(str(error))


def unzip(filename, unzipping_path):
  with ZipFile(filename, "r") as zip_object:
    zip_object.extractall(path=unzipping_path)