import os
import sys
import argparse
import ffmpeg

lossless_extensions = (".flac", ".wav")
destination_codec = 'alac'

def main():
	args = term_args()
	
	if args.path is None or args.output_path is None:
        	print('input path or output path not specified')
        	exit(1)
		
	base_dir = args.path
	output_dir =  args.output_path
	print(f'Base Directory  = { base_dir}')
	print(f'Output Directory = {output_dir}')

	print(f'Output Codec = {destination_codec}')

	for root, subs, files in os.walk(base_dir):
		for file in files:
			if file.endswith(lossless_extensions):	
				convert(file, root, output_dir)

def convert(file, path, output_dir):
	print(file)
	file_folder = os.path.basename(path)
	destination_folder =  os.path.join(output_dir, file_folder)
	if (os.path.exists(destination_folder) is False):
		os.mkdir(destination_folder)

	for file_extension in lossless_extensions:
		if (file.endswith(file_extension)):
			out_file = file.split(file_extension)[0] 
	cmd = f'ffmpeg -i "{os.path.join(path , file)}" -y -v 0 -vcodec copy -acodec {destination_codec} "{os.path.join(destination_folder,out_file)}.m4a"'
	
	os.system(cmd)
	
def term_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", type=str, help="Path to be transcoded.")
    parser.add_argument("-o", "--output_path", type=str, help="Output path")
    parser.add_argument("-c", "--output_codec", type=str, help="Output codec")
    return parser.parse_args()

if __name__ == '__main__': 
    main()
