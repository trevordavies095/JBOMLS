from pathlib import Path
import argparse
import os


def main():
    args = term_args()

    if args.path is None:
        print("Please provide directory!")
        exit(1)
    
    directory = args.path
    for option in args.transcodes:
        Path(directory + "/mp3_" + option).mkdir(exist_ok=True)

    for file in os.listdir(directory):
        if file.endswith(".flac"):
            for option in args.transcodes:
                input = directory + "/" + file
                output = directory+ "/mp3_" + option + "/" + file.split(".flac")[0] + ".mp3"
                transcode(input, output, option)


def transcode(input, output, option):
    opt = {
        "320": "-b:a 320k",
        "v0": "-q:a 0"
    }

    cmd = "ffmpeg -i \"{}\" -codec:a libmp3lame {} \"{}\"".format(input, opt[option], output)
    os.system(cmd)


def term_args():
    mp3_transcodes = ["320", "v0"]
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", type=str, help="Path to be transcoded.")
    parser.add_argument("-t", "--transcodes", type=str, nargs='+', help="Choices for transcodes", choices=mp3_transcodes)
    return parser.parse_args()


if __name__ == '__main__': 
    main()
