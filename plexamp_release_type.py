from mutagen.flac import FLAC
import argparse
import os

plex_release_types = {
    "live": "album;live",
    "compilation": "album;compilation",
    "remix": "album;remix",
    "mixtape": "album;mixtape",
    "soundtrack": "album;soundtrack"
}


def main():
    args = term_args()
        
    if args.path is None:
        print("Please provide directory!")
        exit(1)

    directory = args.path
    filetypes = (".flac")

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(filetypes):
                if file.endswith(".flac"):
                    try:
                        audio = FLAC(root + "/" + file)
                        rt = audio["releasetype"][0].lower().strip()
                        p = root + "/" + file
                        update_release_type(audio, rt, p)
                    except:
                        continue

def update_release_type(track, rt, p):
    track["releasetype"] = plex_release_types[rt]
    print(p + " - UPDATED TO " + plex_release_types[rt])
    track.save()


def term_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", type=str, help="Path to library.")
    return parser.parse_args()


if __name__ == '__main__': 
    main()