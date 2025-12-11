import argparse
import filetype
import os
import shutil


def main():
    args = term_args()

    if args.path is None:
        print("Please provide directory!")
        exit(1)

    directory = args.path
    paths = []

    # Only looking leaf directorys containing one image file
    for root, dirs, files in os.walk(directory):
        cover_art_present = False
        for file in files:
            if file == "cover.jpg":
                cover_art_present = True
                break
        if not cover_art_present and "[" in root:
            print(root)
    else:
        print("No directories found!")


def term_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", type=str, help="Path to be searched.")
    return parser.parse_args()


if __name__ == '__main__': 
    main()
