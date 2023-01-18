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
    lossless_extensions = ["flac", "alac", "wav"]

    for root, dirs, files in os.walk(directory, topdown=True):
        depth = root[len(directory) + len(os.path.sep):].count(os.path.sep)
        if depth == 1:
            log_file_present = False
            combined = '\t'.join(files)
            for ext in lossless_extensions:
                if ext in combined and '.log' in combined:
                    log_file_present = True
                    break

            if log_file_present == False:
                paths.append(root)

    paths = sorted(paths)
    for path in paths:
        print(path)


def term_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", type=str, help="Path to be searched.")
    return parser.parse_args()


if __name__ == '__main__': 
    main()
