import os
import sys
import argparse
import ffmpeg

lossless_extensions = (".flac", ".wav")

def main():
	args = term_args()
	
	if args.path is None:
		print('no path')
		exit(1)

	print(f'Processing {args.path} ')
	
	base_dir = args.path
	print('Base Directory  = ' + base_dir)
	
	for root, subs, files in os.walk(base_dir):
		for file in files:
			if file.endswith(lossless_extensions):	
				convert(file, root)

def convert(file, path):
	print(file)
	for file_extension in lossless_extensions:
		out_file = file.split(file_extension)[0] 
	cmd = f'ffmpeg -i "{os.path.join(path , file)}" -y -v 0 -vcodec copy -acodec alac "/tmp/{out_file}.m4a"'
	os.system(cmd)
	
def term_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", type=str, help="Path to be transcoded.")
    return parser.parse_args()

if __name__ == '__main__': 
    main()
