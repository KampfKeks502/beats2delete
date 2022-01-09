# python 3.8

import json
import os.path
import sys
import hashlib
import argparse

import bs_parser as cparser
import bs_hash




parser = argparse.ArgumentParser(description="Delete/Move all BeatSaber maps that are not in a playlist")


parser.add_argument("-H", "--hash", action="store_true", required=False, help="deletes all maps based on the song's hash")


parser.add_argument("-p", "--path", required=True, type=str, metavar="", help="Path to BeatSaber: e.g.  -p \"G:/Steam/steamapps/common/Beat Saber\"  !!!Forward slashes ONLY!!!")

parser.add_argument("-d", "--delete", action="store_true", required=False, help="delete maps")
args = parser.parse_args()




def sort_songs(beatsaber_path, compare_hash, delete):
    customLevels_path = beatsaber_path + "/Beat Saber_Data/CustomLevels"
    playlist_path = beatsaber_path + "/Playlists"

    songs = cparser.customLevels_parser(customLevels_path)
    plsongs = cparser.get_songs_from_playlists(playlist_path)

    #for plsong in plsongs:
    #    print(plsong.songName)
    # sort songs
    in_playlist = []
    not_in_playlist = []

    if not compare_hash:
        for song in songs:
            is_in_playlist = False
            for plsong in plsongs:
                #print(plsong.songAuthorName)
                if song.songName == plsong.songName and song.levelAuthorName == plsong.levelAuthorName:
                    in_playlist.append(song)
                    is_in_playlist = True
                    break
            if not is_in_playlist:
                not_in_playlist.append(song)

    else:
        for song in songs:
            is_in_playlist = False
            for plsong in plsongs:
                #print(plsong.songAuthorName)
                if song.hash == plsong.hash:
                    in_playlist.append(song)
                    is_in_playlist = True
                    break
            if not is_in_playlist:
                not_in_playlist.append(song)



    print("remove:", len(not_in_playlist), "maps")
    print("Keep  :", len(in_playlist), "maps")


    if not delete:
        INput = input(str("Move " + str(len(not_in_playlist)) + " maps to temp folder? [y/n]\n"))
        if INput == "y" or  INput == "Y":
            print("moving...")
        else:
            print("abort...")
            sys.exit()
    else:
        INput = input(str("Delete " + str(len(not_in_playlist)) + " Songs? [y/n]     !!!This will be permanent and can't be undone!!!\n"))
        if INput == "y" or  INput == "Y":
            print("deleting ...")
        else:
            print("abort ...")
            sys.exit()



if __name__ == "__main__":
    sort_songs(args.path, args.hash, args.delete)
