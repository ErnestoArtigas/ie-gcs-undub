# ie-gsc-undub -  Inazuma Eleven Go Chrono Stone Undub

## Description

This project is aim to generate an European CIA file with Japanese dubbing. It takes a Japanese CIA and an European CIA as input files.

## Usage

Download your OS specific release, unzip it and use like this :

```
main -j path/to/japanese_rom.cia -e path/to/european_rom.cia
```

```
Options:
  -h, --help            show this help message and exit
  -j JAPANESE_ROM, --japanese-rom=JAPANESE_ROM 
                        Path of the japanese rom
  -e EUROPEAN_ROM, --european-rom=EUROPEAN_ROM
                        Path of the european rom
```

## Building

### Dependencies

#### Python modules :
- colorama
- yaspin
- python-dotenv
- optparse

The python modules are listed in the [requirements.txt](requirements.txt) you can install it with pip :

```
python -m pip install -r requirements.txt
```

#### Libraries :
- [3dstool](https://github.com/dnasdw/3dstool)
- [ctrtool](https://github.com/3DSGuy/Project_CTR/releases/tag/ctrtool-v1.2.0)
- [makerom](https://github.com/3DSGuy/Project_CTR/releases/tag/makerom-v0.18.3)

A script was written to download and set the env file with the right values. The script is cross-plateform.

```
python setup-libraries.py
```

For Powershell scripting (Github Action with a windows runner, out-null or > $null option), there is a ```--no-yaspin-output``` argument for avoiding Yaspin crashes.

```
python setup-libraries.py --no-yaspin-output
```

If you already have the three programs installed, you can edit the .env file and change each program's path. For the moment, only relative paths are working.


### Usage

```
src/main.py -j path/to/japanese_rom.cia -e path/to/european_rom.cia
```

```
Options:
  -h, --help            show this help message and exit
  -j JAPANESE_ROM, --japanese-rom=JAPANESE_ROM 
                        Path of the japanese rom
  -e EUROPEAN_ROM, --european-rom=EUROPEAN_ROM
                        Path of the european rom
```

## Roms
Here are the MD5 of the files used for testing this program. They were all extracted from a modded 3DS with GodMode9. There shouldn't be problems of mismatch version, this list is just for giving more informations.

- **Inazuma Eleven Go - Chrono Stone - Neppuu.cia** : 5d1a0250d2b78bdeb61adf99ea3a1291
- **Inazuma Eleven Go - Chrono Stone - Wildfire.cia** : 93beae09ffe8656d4a8c5f6695cba9dd

- **Inazuma Eleven Go - Chrono Stone - Raimei.cia** : cc4543b4f869d935021276f3571ef2f8
- **Inazuma Eleven Go - Chrono Stone - Thunderflash.cia** : 90fb538561554d5333f52e8eeca7072f

You can use a Neppuu rom for undubbing Thunderflash and vice versa, both games have the audio for both game.

## Technical description

The program works in three steps :

- Extracting both CIA files into distinct folders, Decrypting the CCIs and RomFS of both roms.

- Iterating into the European ```romfs/snd/product/stream``` folder and replacing the files that exists in the Japanese release.

- Repacking the European RomFS, the CCIs and repacking everything into a CIA file.

## Issues

There are three missing 4 missing files in the Japanese release, this is the list (each files has prefixed, _en, _fr, ...)
- se_ev01_0300_01.bcstm  = Attack Mode of Team Omega.
- se_ev02_0180.bcstm = Teleport Mode of Team Omega.
- se_ev03_0580.bcstm = Capture Mode of Team Omega.
- se_ev08_0260.bcstm = Ambient crowd.

Because of the method of replacing only the sound file with regional prefix, the credits songs are not copied over the undubbed. This will be quickly fix.

This method doesn't copy the credits cutscene's music and doesn't copy the music from the Japanese release. They are the same music, however the sound is lower in Japanese. When modding the game with this method, some voices can be too low because of the European music higher volume.

## Roots

This project was born when extracting the game files to get the music files. I felt an undubbing would be a good project to work my Python skills and working with subprocesses. I however found a project much more robust, replacing in every scripts the translated names of characters, techniques and places with their Japanese original names.

[Here is the link](https://gbatemp.net/threads/inazuma-eleven-go-2-chrono-stone-neppu-raimei-complete-undub-v3.593505/), if you want to play that version.

This version is more basic but should be crash free, because of the simplier audio replacing.

## Credits

The extracting and repacking of CIA files scripts originates from [Asia81's HackingToolkit9DS](https://github.com/Asia81/HackingToolkit9DS) project. Because I had some issues when trying to use it on another Windows installation, I translated his batch scripts into a Python script, [managing_cia.py](src/managing_cia.py).