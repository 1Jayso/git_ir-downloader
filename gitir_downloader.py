from genericpath import isfile
from bs4 import BeautifulSoup
import wget
import os
from pathlib import Path
import urllib.request, urllib.error, urllib.parse
import linecache
import shutil

text_url = input("Paste url to download the text file: ")
txt = text_url.split('/')[-2]
#the index of the slit could change
dir_name = txt.split('--')[-1] 
file_name = 'saved_file.txt'

absolute_path = os.path.dirname(__file__)
relative_path = dir_name
full_path = os.path.join(absolute_path, relative_path)



def create_dir(path):
    try:
        isFile = os.path.exists(path)
        if isFile:
            os.chdir(path)
            print("Directory has been changed to " + path)
        else:
            os.makedirs(path)
            print("Successfully created the directory %s" % path)
            os.chdir(path)
    except OSError:
        print("Creation of the directory %s failed" % path)

create_dir(path=dir_name)


folder_name = []
def open_file():
    line = linecache.getline(file_name, 2)
    new_folder_name = line.split('/')[-2] 
    folder_name.append(new_folder_name)
    print(line)
    with open(file_name, 'r+') as fp:
        
        # read an store all lines into list
        lines = fp.readlines()
        # move file pointer to the beginning of a file
        fp.seek(0)
        # truncate the file
        fp.truncate()

        # start writing lines
        # iterate line and line number
        for number, line in enumerate(lines):
            # note: list index start from 0
            if number not in [0, 1, 2]:
                fp.write(line)



def save_file(file_name, text_url):
    try:
        response = urllib.request.urlopen(text_url)
        webContent = response.read().decode('UTF-8')
        # print(webContent)
        f = open(file_name, 'w')
        f.write(webContent)
        f.close
        print("\nText file has been downloaded!!")
        print()
    except OSError:
        print(f"Downloding of {text_url} failed")
save_file(file_name, text_url)
open_file()


links = []
def download_links(): 
    try:
        lines = [line.strip() for line in open(file_name, 'r+')]
        links.append(lines)
        print(sorted(links))
    except OSError:
        print(OSError)
download_links()


def download_videos():
    dlLinks = sorted(links)

    for link in dlLinks:
        print("Downloding Videos ...")
        for dl in link:
            file_name = dl.split('/')[-1] 
            file_name = file_name.replace("-%20", " ")
            print(file_name)

            if os.path.exists(file_name):
                print(file_name, "already downloaded")
            else:
                print(f"Downloading file {file_name}")
                # start Download
                wget.download(dl, bar=wget.bar_adaptive)
                print(f"\nDownloaded! {file_name} ")
                print("Downloads completed !")
                print()
        return

def cleanupTempFiles(folder_path):
    full_path = os.path.join(absolute_path, folder_path)
    os.chdir(full_path)
    folder = os.listdir(full_path)
    for item in folder:
        if item.endswith(".tmp"):
            os.remove(os.path.join(full_path, item))
        else:
            print("There are no .tmp files in this directory")
    print("All .tmp Files have been deleted successfully")
    

download_videos()
os.chdir(absolute_path)
shutil.move(full_path, folder_name[0])
cleanupTempFiles(folder_name[0])


# https://git.ir/media/download-links/packt-data-structures-and-algorithms-the-complete--b216f699b98f467395115dbc6691e429.txt