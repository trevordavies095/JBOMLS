import argparse
import filetype
import os
import shutil
import glob,os.path


def main():
    args = term_args()
    audio_extensions = ['.mp3', '.aac', '.ogg', '.flac', '.wav', '.alac', 'aiff', '.dsd', '.pcm', '.opus', '.m4a']

    if args.path is None:
        print("Please provide directory!")
        exit(1)

    path = os.path.normpath(args.path)
    paths = []

    for root, dirs, files in os.walk(path, topdown=True):
        depth = root[len(path) + len(os.path.sep):].count(os.path.sep)
        if depth == 1:
            combined = '\t'.join(files)
            audio_dir = False
            for ext in audio_extensions:
                if ext in combined and '01 ' in combined:
                    audio_dir = True
                    break
            
            if audio_dir == False:
                paths.append(root)
                print(root)

    if paths:
        print()
        print("Delete the following directories?")
        print("[Y]es, [N]o")
        choice = input("> ").lower().strip()

        if choice == "y":
            for path in paths:
                try:
                    shutil.rmtree(path)
                except Exception:
                    print("Cannot delete: " + path)
    else:
        print("No directories found!")



def term_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", type=str, help="Path to be searched.")
    return parser.parse_args()
    

if __name__ == '__main__': 
    main()
