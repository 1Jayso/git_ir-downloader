from genericpath import isfile
from bs4 import BeautifulSoup
import wget
import os

text_url = input("Paste url to download the text file: ")

txt = text_url.split('/')[-1]

#the index of the slit could change
dir_name = txt.split('--')[-1] 


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

textfile = text_url.split('/')[5]


def open_file():
    with open(textfile, 'r+') as fp:
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


def download_text_file(text_url):
    try:
        isFile = os.path.isfile(textfile)
        if isFile:
            print()
            print("File already exist !!")
            open_file()
        else:
            wget.download(text_url)
            print("\nDownload completed!!")
            open_file()
            print()
    except OSError:
        print(f"Downloding of {text_url} failed")


download_text_file(text_url)


links = []


def list_of_downloads(): 
    try:

        lines = [line.strip() for line in open(textfile, 'r+')]
        links.append(lines)

        print(sorted(links))
    except OSError:
        print(OSError)


list_of_downloads()


def download_videos():
    dlLinks = sorted(links)

    for link in dlLinks:
        print("Downloding Videos ...")
        for dl in link:
            file_name = dl.split('/')[-1] 
            print(file_name)

            if os.path.exists(file_name):
                print(file_name, "already downloaded")

            else:
                print(f"Downloading file {file_name}")
                # start Download
                wget.download(dl, bar=wget.bar_adaptive)
                print(f"\nDownloaded! {file_name} ")
                print()
        return


download_videos()


# https://git.ir/media/download-links/packt-data-structures-and-algorithms-the-complete--b216f699b98f467395115dbc6691e429.txt