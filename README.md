# ie-gsc-undub -  Inazuma Eleven Go Chrono Stone Undub

## Description

This project is aim to generate an European CIA file with Japanese dubbing. It takes a Japanese CIA and an European CIA as input files. The program works in three steps :

- Extracting both CIA files into distinct folders, Decrypting the CCIs and RomFS of both roms.

- Iterating into the European ```romfs/snd/product/stream``` folder and replacing the files that exists in the Japanese release.
  - It for the moment only verify if files with prefixes (en, fr, ...) exists without prefix in the Japanese release and move the Japanese version into the European folder, renaming it with the proper prefix.
  - This method doesn't copy the credits cutscene's music and doesn't copy the music from the Japanese release. They are the same music, however the sound is lower in Japanese. When modding the game with this method, some voices can be too low because of the European music higher volume.

- Repacking the European RomFS, the CCIs and repacking everything into a CIA file.

## Roots

This project was born when extracting the game files to get the music files. I felt an undubbing would be a good project to work my Python skills and working with subprocesses. I however found a project much more robust, replacing in every scripts the translated names of characters, techniques and places with their Japanese original names.

[Here is the link](https://gbatemp.net/threads/inazuma-eleven-go-2-chrono-stone-neppu-raimei-complete-undub-v3.593505/), if you want to play that version.

This version is more basic but should be crash free, because of the simplier audio replacing.


## Dependencies

**Libraries** :
- [3dstool](https://github.com/dnasdw/3dstool)
- [ctrtool](https://github.com/3DSGuy/Project_CTR/releases/tag/ctrtool-v1.2.0)
- [makerom](https://github.com/3DSGuy/Project_CTR/releases/tag/makerom-v0.18.3)

**Python modules** :
- colorama
- yaspin
- python-dotenv
- optparse

## Usage

```
Usage: main.py -j path/to/japanese_rom.cia -e path/to/european_rom.cia

Options:
  -h, --help            show this help message and exit
  -j JAPANESE_ROM, --japanese-rom=JAPANESE_ROM 
                        Path of the japanese rom
  -e EUROPEAN_ROM, --european-rom=EUROPEAN_ROM
                        Path of the european rom
```

### Roms
Here are the MD5 of the files used for testing this program. They were all extracted from a modded 3DS with GodMode9. There shouldn't be problems of mismatch version, this list is just for giving more informations.

- **Inazuma Eleven Go - Chrono Stone - Neppuu.cia** : 5d1a0250d2b78bdeb61adf99ea3a1291
- **Inazuma Eleven Go - Chrono Stone - Wildfire.cia** : 93beae09ffe8656d4a8c5f6695cba9dd

- **Inazuma Eleven Go - Chrono Stone - Raimei.cia** : cc4543b4f869d935021276f3571ef2f8
- **Inazuma Eleven Go - Chrono Stone - Thunderflash.cia** : 90fb538561554d5333f52e8eeca7072f

You can use a Neppuu rom for undubbing Thunderflash and vice versa, both games have the audio for both game.

### Libraries

You need to download the three programs listed in [the dependencies section](#dependencies). Edit the .env file and changed the path for the location of the three programs. You can enter an absolute path to the program or place them in the ```lib``` folder and add a relative path in the .env.

## Issues

There are three missing 4 missing files in the Japanese release, this is the list (each files has prefixed, _en, _fr, ...)
- se_ev01_0300_01.bcstm  = Attack Mode of Team Omega.
- se_ev02_0180.bcstm = Teleport Mode of Team Omega.
- se_ev03_0580.bcstm = Capture Mode of Team Omega.
- se_ev08_0260.bcstm = Ambient crowd.

Because of the method of replacing only the sound file with regional prefix, the credits songs are not copied over the undubbed. This will be quickly fix.

## Credits

The extracting and repacking of CIA files scripts originates from [Asia81's HackingToolkit9DS](https://github.com/Asia81/HackingToolkit9DS) project. Because I had some issues when trying to use it on another Windows installation, I translated his batch scripts into a Python script, ```managing_cia.py```.