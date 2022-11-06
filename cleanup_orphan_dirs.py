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
        if len(files) == 1 and filetype.is_image(os.path.join(root,files[0])) and not dirs:
            paths.append(root)
            print(root)

    if paths:
        print()
        print("Delete the following directories?")
        print("[Y]es, [N]o")
        choice = input("> ").lower().strip()

        if choice == "y":
            for path in paths:
                shutil.rmtree(path)
    else:
        print("No directories found!")


def term_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", type=str, help="Path to be transcoded.")
    return parser.parse_args()


if __name__ == '__main__': 
    main()
