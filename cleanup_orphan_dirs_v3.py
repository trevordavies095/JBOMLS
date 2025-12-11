import argparse
import filetype
import os
import shutil


def is_audio_file(file_path):
    """Check if a file is an audio file using filetype library."""
    try:
        kind = filetype.guess(file_path)
        if kind is None:
            # Fallback to extension check if filetype can't determine
            audio_extensions = ['.mp3', '.aac', '.ogg', '.flac', '.wav', '.alac', 
                              '.aiff', '.dsd', '.pcm', '.opus', '.m4a', '.mp4', 
                              '.m4p', '.ape', '.wma', '.ac3', '.dts']
            return any(file_path.lower().endswith(ext) for ext in audio_extensions)
        return kind.mime.startswith('audio/')
    except Exception:
        # Fallback to extension check on error
        audio_extensions = ['.mp3', '.aac', '.ogg', '.flac', '.wav', '.alac', 
                          '.aiff', '.dsd', '.pcm', '.opus', '.m4a', '.mp4', 
                          '.m4p', '.ape', '.wma', '.ac3', '.dts']
        return any(file_path.lower().endswith(ext) for ext in audio_extensions)


def has_music_files(directory):
    """Check if a directory contains any music files (recursively checks subdirectories)."""
    try:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                if is_audio_file(file_path):
                    return True
    except Exception:
        pass
    return False


def main():
    args = term_args()

    if args.path is None:
        print("Please provide directory!")
        exit(1)

    directory = os.path.normpath(args.path)
    paths_to_delete = []

    # Walk through the directory structure
    # We're looking for album directories (depth 1: library/artist/album)
    for root, dirs, files in os.walk(directory, topdown=True):
        # Calculate depth from the root directory
        depth = root[len(directory) + len(os.path.sep):].count(os.path.sep)
        
        # Check album directories (depth 1: library/artist/album)
        if depth == 1:
            if not has_music_files(root):
                paths_to_delete.append(root)

    if paths_to_delete:
        print(f"\nFound {len(paths_to_delete)} album directories without music files:\n")
        for path in sorted(paths_to_delete):
            print(path)
        
        print("\n" + "="*60)
        print(f"Total directories to delete: {len(paths_to_delete)}")
        print("="*60)
        print("\nDelete the following directories?")
        print("[Y]es, [N]o")
        choice = input("> ").lower().strip()

        if choice == "y":
            deleted_count = 0
            failed_count = 0
            for path in paths_to_delete:
                try:
                    shutil.rmtree(path)
                    deleted_count += 1
                    print(f"Deleted: {path}")
                except Exception as e:
                    failed_count += 1
                    print(f"Cannot delete: {path} - {str(e)}")
            
            print(f"\nCompleted: {deleted_count} deleted, {failed_count} failed")
        else:
            print("Deletion cancelled.")
    else:
        print("No directories found without music files!")


def term_args():
    parser = argparse.ArgumentParser(
        description="Find and optionally delete album directories that don't contain music files."
    )
    parser.add_argument("-p", "--path", type=str, help="Path to music library (library/artist/album structure).")
    return parser.parse_args()


if __name__ == '__main__': 
    main()

