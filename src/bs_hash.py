# python 3.8

import os.path
import hashlib
import sys


def hash(listoffiles):
    #check if files exist
    for file in listoffiles:
        if not os.path.isfile(file):
            print("Error checking filelist: file does not exist")
            print("File: " + file)
            sys.exit()
    # hash files
    hash_obj = hashlib.sha1(open(listoffiles[0], 'rb').read())
    for fname in listoffiles[1:]:
        hash_obj.update(open(fname, 'rb').read())
    # return checksum as bytes
    return hash_obj.digest()


# create hex string from bytes
def bytes_to_hex(bytes, uppercase_string=False):
    hex = bytes.hex()
    if uppercase_string:
        hex = hex.upper()
    return hex


# create hash string
# from one or more files
def hash_string(listoffiles, uppercase=False):
    return bytes_to_hex(hash(listoffiles), uppercase_string=uppercase)


'''
filelist = ["G:/Steam/steamapps/common/Beat Saber/Beat Saber_Data/CustomLevels/16591 (食虫植物Carnivorous Plant - Fefy)/Info.dat",
"G:/Steam/steamapps/common/Beat Saber/Beat Saber_Data/CustomLevels/16591 (食虫植物Carnivorous Plant - Fefy)/HardStandard.dat",
"G:/Steam/steamapps/common/Beat Saber/Beat Saber_Data/CustomLevels/16591 (食虫植物Carnivorous Plant - Fefy)/ExpertStandard.dat",
"G:/Steam/steamapps/common/Beat Saber/Beat Saber_Data/CustomLevels/16591 (食虫植物Carnivorous Plant - Fefy)/ExpertPlusStandard.dat"  ]
'''
# example
#print(hash_string(filelist, uppercase=True))
