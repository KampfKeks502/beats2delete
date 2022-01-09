# python 3.8

import json
import os.path
import sys
import hashlib

import custom_parser as cparser
import custom_hash as chash

bs_path = "G:/Steam/steamapps/common/Beat Saber"


def sort_songs(beatsaber_path):
    customLevels_path = beatsaber_path + "/Beat Saber_Data/CustomLevels"
    playlist_path = beatsaber_path + "/Playlists"

    songs = cparser.customLevels_parser(customLevels_path)
    plhashes = cparser.get_song_hashes_from_playlists(playlist_path)

    # sort songs
    in_playlist = []
    not_in_playlist = []


    for song in songs:
        if song.hash in plhashes:
            in_playlist.append(song)
        else:
            not_in_playlist.append(song)

    print("Not in playlist:", len(not_in_playlist))
    print("In playlist    :", len(in_playlist))
    for hash in plhashes:
        print(hash)
    print("")
    for song in in_playlist:
        print(song.hash)

    print("check")
    too_much = plhashes
    too_less = []
    for s in in_playlist:
        too_less.append(s.hash)

    for son in too_much:
        if not son in too_less:
            print(son)

    for song in songs:
        if song.songName =="osu!memories":
            print(song.song_path)
            print(song.hash)





sort_songs(bs_path)
