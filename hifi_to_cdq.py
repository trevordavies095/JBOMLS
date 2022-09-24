from pathlib import Path
import argparse
import ffmpeg
import os


def main():
    args = term_args()
    if args.path is None:
        print("Bad!")
        exit(1)
    directory = args.path
    output_dir = directory + "/transcode"
    Path(output_dir).mkdir(exist_ok=True)

    lossless_extensions = (".flac", ".wav")

    for file in os.listdir(directory):
        if file.endswith(lossless_extensions):
            stream = ffmpeg.input(directory + "/" + file)
            file = file.split(".")[0] + ".flac"
            stream = ffmpeg.output(stream, (output_dir + "/" + file), **{'sample_fmt':'s16'}, **{'ar':44100})
            ffmpeg.run(stream)


def term_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", type=str, help="Path to be transcoded.")
    return parser.parse_args()


if __name__ == '__main__': 
    main()