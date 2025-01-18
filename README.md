# w3-speech-export
All you need to export W3 speech

## Usage

Download all files from this repository and make sure you have Python installed (tested on 3.13) and then:

### To export speech files from the game
1. Set `game dir' and `lang` variables in `export_w3speech.py`
2. Run `export_w3speech.py`

### To add actors to filenames
- Run `add_actors.py`

### To copy all actor files to another folder
1. Set `actor_name` and `new_folder` variables in `copy_by_actor.py`
2. Run `copy_by_actor.py`

## Credits
- `export_w3speech.py`, `add_actors.py`, `copy_by_actor.py`, actors dictionary (`ids_dict.txt`) are created by SieeleLushen
- `w3unpack.exe` is a part of w3utils by [JTGizmo](https://github.com/JTGizmo/Extracting-Voice-Over-Audio-from-Witcher-3)
- Other files are vgmstream's files and libs (WIN x64 release), all rights reserved by [its authors](https://github.com/vgmstream/vgmstream?tab=License-1-ov-file#readme)
