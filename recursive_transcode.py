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
				convert(os.path.join(root , file))

#ffmpeg -i "$i" -y -v 0 -vcodec copy -acodec alac "${i%.flac}".m4a
def convert(file):
	print(file)
	#stream = ffmpeg.input(file)
	#print(stream)
	#print(ffmpeg.get_args(stream))
	#TODO replace with output param / look for all input params
	for file_extension in lossless_extensions:
		out_file = file.split(file_extension)[0] + ".m4a" 
	cmd = f'ffmpeg -i {file} -y -v 0 -vcodec copy -acodec alac "{out_file}"'
	os.system(cmd)
	#ffmpeg.output(stream, '/tmp/'+ 1, **{'acodec':'alac'}, **{'vcodec':'copy'})
	#ffmpeg.output(stream, (output_dir + "/" + file), **{'sample_fmt':'s16'}, **{'ar':44100})
	#print(ffmpeg.get_args(stream, overwrite_output=False))
	#ffmpeg.run(stream)
	
def term_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", type=str, help="Path to be transcoded.")
    return parser.parse_args()

if __name__ == '__main__': 
    main()
