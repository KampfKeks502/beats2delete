# Beats2Delete - Beat Saber (PCVR/Steam)

This script will remove songs depending on your selection (Favorites/Playlist maps)

At the end of the program you'll be asked if you want to delete all non-matching maps or
just move them to a different folder (in case you want to recover the maps)

Script tested using Python 3.8 (64-bit) - Win10

# Demo Video - YouTube
### Remove all non-favorite maps in Beat Saber | Beats2Delete Demo
[![Remove all non-favorite maps in Beat Saber](https://img.youtube.com/vi/zKhkO2SO7eU/maxresdefault.jpg)](https://youtu.be/zKhkO2SO7eU)

# How does it work
Upon starting the script you'll have to select a few things...

## 1. Select the maps you want to keep:
- Favorites
- Playlists
- Favorites and Playlists

## 2. Select the action you want to perform:
- Move maps to temp folder  [Recommended]
- Delete maps

### Move maps to temp folder:
Moves all maps that don't match the previously selected criteria to a "temporary" folder.
This directory is located inside the default game Folder and is called "_beats2delete"
E.g.: "G:\Steam\steamapps\common\Beat Saber\_beats2delete"
There you'll find all the maps that have been sorted out.
If you're sure that you don't need these songs anymore you can just delete the entire "_beats2delete" folder

#### Restore maps:
To restore the maps just move them back into the "Beat Saber_Data\CustomLevels" folder
and restart BeatSaber


### Delete maps:
Well... this option will delete all maps that don't match the previously selected criteria.
Remember: This can't be undone!


## 3. Select the Compare-Mode
If you've chosen an option including a playlist you'll be prompted with these options:
- Map name and map author  [Recommended]
- Hash ID

### **TL;DR:  If you're not sure then just use the first option (Map name and map author)**

**The Long Answer ...**

### Map name and map author:
The script will compare the maps by their names and authors to decide whether or not to keep a song.
Some authors release multiple songs with the same name. Therefore, both versions of the map are preserved
even if only one of them is saved in a playlist.

### Hash ID:
To solve the problem of the first version, the Hash-ID-Compare mode is used. Each map has a unique hash,
even if the title and author are exactly the same. The second option compares both hashes,
the current map hash (calculated just-in-time) and the hash stored inside of the playlist files.
(located inside the Game Directory [e.g.: "G:\Steam\steamapps\common\Beat Saber\Playlists\*.bplist"])
Therefore, only the exact map saved in a playlist is retained.


### The Problem with Hash ID:
The only useable informations for map comparison inside the playlist files (*.bplist) are:
- songName
- levelAuthorName
- hash

I discovered an anomaly in the hashes stored in the playlist files. Some of them (rather small percentage)
differ from the actual map hashes and therefore are not kept in Hash-ID-Compare mode.
As a result it's recommended to use the first option until I figure out what's causing this discrepancy
and how to fix it.

If you know more about this problem, feel free to contact me. I'd love to hear what's causing this behavior :)

# How to use
1. Adjust the path to your BeatSaber folder inside start.bat to your needs.\
2. run start.bat


# Args
```
usage: beats2delete.exe [-h] [-H] -p  [-d] [-f] [-pl]

Delete/Move all BeatSaber maps that are not in a playlist

optional arguments:
  -h, --help       show this help message and exit
  -H, --hash       deletes all maps based on the song's hash
  -p , --path      Path to BeatSaber: e.g. -p "G:\Steam\steamapps\common\Beat Saber" !no environment variables!
  -d, --delete     delete maps
  -f, --favorite   keep favorites (can be combined with --playlist)
  -pl, --playlist  keep maps that are in a playlist
```
