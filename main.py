# python 3.8

import json
import os
from os import path
import sys
import hashlib
import argparse
from subprocess import call, run, STDOUT
from datetime import datetime
import shutil

# custom imports
from src import bs_parser as cparser
from src import bs_hash




parser = argparse.ArgumentParser(description="Delete/Move all BeatSaber maps that are not in a playlist")


parser.add_argument("-H", "--hash", action="store_true", required=False, help="deletes all maps based on the song's hash")


parser.add_argument("-p", "--path", required=True, type=str, metavar="", help="Path to BeatSaber: e.g.  -p \"G:\\Steam\\steamapps\\common\\Beat Saber\"  !no environment variables!")

parser.add_argument("-d", "--delete", action="store_true", required=False, help="delete maps")

parser.add_argument("-f", "--favorite", action="store_true", required=False, help="keep favorites   (can be combined with --playlist)")
parser.add_argument("-pl", "--playlist", action="store_true", required=False, help="keep maps that are in a playlist")

args = parser.parse_args()




def sort_songs(beatsaber_path, compare_hash, delete, keep_playlist, keep_favorites):
    beatsaber_path = beatsaber_path.replace("\\", "/")
    if beatsaber_path[-1] == "/":
        beatsaber_path = beatsaber_path[:-1]
    customLevels_path = beatsaber_path + "/Beat Saber_Data/CustomLevels"
    playlist_path = beatsaber_path + "/Playlists"

    songs = cparser.customLevels_parser(customLevels_path)
    plsongs = cparser.get_songs_from_playlists(playlist_path)

    #for plsong in plsongs:
    #    print(plsong.songName)
    # sort songs
    keep = []
    dont_keep = []
    #oii = 1

    #playlist parser
    if keep_playlist:
        if not compare_hash:
            for song in songs:
                for plsong in plsongs:
                    if song.songName == plsong.songName and song.levelAuthorName == plsong.levelAuthorName:
                        song.ks()
                        break

        else:
            for song in songs:
                for plsong in plsongs:
                    # make hash comparison
                    if song.hash == plsong.hash:
                        song.ks()


    #favorites parser
    if keep_favorites:
        #fav list
        username = os.environ.get('USERNAME')
        playerdata_path = "C:/Users/" + username + "/AppData/LocalLow/Hyperbolic Magnetism/Beat Saber/PlayerData.dat"
        f_list = cparser.get_fav_hash(playerdata_path)

        for song in songs:
            for f_map in f_list:
                # compare song hash with favorite map hash
                if song.hash == f_map:
                    song.ks()





    #count rmv maps
    i_keep = 0
    i_rmv = 0
    for song in songs:
        if not song.keep:
            i_rmv += 1
        else:
            i_keep += 1

    print("")
    print("remove:", i_rmv, "maps")
    print("Keep  :", i_keep, "maps")


    if not delete:
        INput = input(str("Move " + str(i_rmv) + " maps to temp folder? [y/n]\n"))
        if INput == "y" or  INput == "Y":
            junk_mover(beatsaber_path, songs)
            print("\nDone")
        else:
            print("\nabort...")
            sys.exit()
    else:
        INput = input(str("Delete " + str(i_rmv) + " Songs? [Type in \"yes\" to confirm]     !!!This will be permanent and can't be undone!!!\n"))
        if INput == "yes" or  INput == "YES":
            junk_remover(songs)
            print("\nDone")
        else:
            print("\nabort ...")
            sys.exit()


def map_remover(dir):
    try:
        print("deleting...  " + dir)
        shutil.rmtree(dir)
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))
        sys.exit()


def map_mover(src, dst,):
    DEVNULL = open(os.devnull, 'wb')
    src = src.replace("/", "\\")
    dst = dst.replace("/", "\\")
    try:
        print("moving...  " + src)
        call(["robocopy", src, dst, "/MOVE", "/E", "/NDL", "/NFL", "/NJH", "/NJS", "/ns", "/nc"], stdout=DEVNULL)
    except Exception as err:
        print("Error moving files")
        print(err)
        sys.exit()


def make_dir(dir):
    DEVNULL = open(os.devnull, 'wb')
    try:
        os.mkdir(dir)
    except Exception as err:
        print("Error creating dir")
        print(err)
        sys.exit()


def junk_mover(bs_path, songs):
    now = datetime.now()
    time_str = now.strftime("%Y-%m-%d__%H-%M-%S")
    dir_path = bs_path + "/" + "_beats2delete"
    if not path.exists(dir_path):
        make_dir(dir_path)
    new_folder = dir_path + "/maps_" + time_str
    print("Moving maps to temp folder: " + new_folder)
    make_dir(new_folder)
    for song in songs:
        if not song.keep:
            # move
            song_folder = song.song_path.rsplit('/', 1)[-1]
            dst = new_folder + "/" + song_folder
            map_mover(song.song_path, dst)


def junk_remover(songs):
    for song in songs:
        if not song.keep:
            map_remover(song.song_path)





if __name__ == "__main__":
    if not args.favorite and not args.playlist:
        print("Please provide at least one parse option [-pl and/or -f]")
        sys.exit()
    # G:/Steam/steamapps/common/Beat Saber
    sort_songs(args.path, args.hash, args.delete, args.playlist, args.favorite)
