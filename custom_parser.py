# python 3.8

import json
import os.path
import sys
import custom_hash

# song obj
class Song:
    songName = None
    songAuthorName = None
    levelAuthorName = None
    difficulties = []

    hash = None

    song_path = None

    def __init__(self, songName, songAuthorName, levelAuthorName, difficulties, hash, song_path):
        self.songName = songName
        self.songAuthorName = songAuthorName
        self.levelAuthorName = levelAuthorName
        self.difficulties = difficulties

        self.hash = hash
        self.song_path = song_path

    def hash(self, hash):
        self.hash = hash

    def print(self):
        print("songName: " + self.songName)
        print("songAuthorName: " + self.songAuthorName)
        print("levelAuthorName: " + self.levelAuthorName)
        print("difficulties:" , self.difficulties)

        print("hash: " + self.hash)
        print("Path: " + self.song_path)


class PlSong:
    songName = None
    songAuthorName = None
    hash = None

    def __init__(self, songName, songAuthorName, hash):
        self.songName = songName
        self.songAuthorName = songAuthorName
        self.hash = hash


# json to python dictionary
def json_to_dict(json_data):
    return json.loads(json_data)


def read_json(file):
    try:
        json = open(file, "r", encoding="utf-8").read()
        return json
    except:
        print("Error reading Info.dat [" + file + "]")


def get_diff_files(dictionary):
    diff_list = []
    try:
        for each_diff in dictionary["_difficultyBeatmapSets"][0]["_difficultyBeatmaps"]:
            diff_list.append(each_diff["_beatmapFilename"])
    except:
        print("Error parsing map difficulties")
        sys.exit()
    return diff_list


# parses a song folder for data
def song_parser(song_folder):
    #check if Info.dat exist
    info_file = song_folder + "/Info.dat"
    if not os.path.isfile(info_file):
        print("Error parsing song: \"Info.dat\" not found in " + song_folder)
    # parse json (json to python dictionary)
    data = json.loads(read_json(info_file))


    songName = data["_songName"]
    songAuthorName = data["_songAuthorName"]
    levelAuthorName = data["_levelAuthorName"]
    difficulties = get_diff_files(data)

    # create hash
    file_list = []
    file_list.append(song_folder + "/" + "Info.dat")
    for diff in difficulties:
        file_list.append(song_folder + "/" + diff)
    try:
        song_hash = custom_hash.hash_string(file_list, uppercase=True)
    except:
        print("Error creating hash of song")
        print("Song: " + song_folder)
        sys.exit()

    #create song obj

    try:
        song = Song(songName, songAuthorName, levelAuthorName, difficulties, song_hash, song_folder)
        return song
    except:
        print("oops, something went wrong with:")
        print(songName)
        print(songAuthorName)
        print(levelAuthorName)
        print(difficulties)
        print(song_folder)
        sys.exit()



# parses all custom levels
def customLevels_parser(path):
    # get all song dirs
    try:
        song_dirs = os.listdir(path)
        print("Songs found:" , len(song_dirs))
        root_dirs = []
        for dir in song_dirs:
            root_dirs.append(path + "/" + dir)
    except:
        print("Error parsing customLevels")
        print("Make sure the path to the BeatSaber folder is correct")
        sys.exit()

    # parse all songs to one Songs obj create_song_array
    song_list = []
    for dir in root_dirs:
        song_list.append(song_parser(dir))
    return song_list


# parse playlists (*.bplist files)
def playlists_parser(playlist_path):
    playlist_root_paths = []
    try:
        pfiles = os.listdir(playlist_path)
    except:
        print("Error parsing playlist")
        print("check if the beatsaber path is valid")

    for file in pfiles:
        if ".bplist" in file:
            playlist_root_paths.append(playlist_path + "/" + file)
    # for pl in playlist_root_paths:
    #     print(pl)
    print("Playlists: ", len(playlist_root_paths))
    return playlist_root_paths

def parse_playlist_hash(playlist):
    data = json.loads(read_json(playlist))
    hash_list = []
    for songs in data["songs"]:
        hash_list.append(songs["hash"])
    return hash_list


def get_song_hashes_from_playlists(path_to_playlist_folder):
    playlists = playlists_parser(path_to_playlist_folder)
    all_hashes = []
    for playlist in playlists:
        all_hashes += parse_playlist_hash(playlist)
    # remove duplicates from list
    all_hashes = list(dict.fromkeys(all_hashes))
    print("Songs in Playlist: " , len(all_hashes))
    return all_hashes





#customLevels_parser("G:/Steam/steamapps/common/Beat Saber/Beat Saber_Data/CustomLevels")
#playlists_parser("G:/Steam/steamapps/common/Beat Saber/Playlists")
#get_song_hashes_from_playlists("G:/Steam/steamapps/common/Beat Saber/Playlists")
