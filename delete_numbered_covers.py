import argparse
import os
import re


def main():
    args = term_args()

    if args.path is None:
        print("Please provide directory!")
        exit(1)

    directory = os.path.normpath(args.path)
    
    if not os.path.isdir(directory):
        print(f"Error: '{directory}' is not a valid directory!")
        exit(1)

    files_to_delete = []
    # Pattern to match cover.N.jpg or cover.N.png where N is any number
    pattern = re.compile(r'^cover\.(\d+)\.(jpg|png)$', re.IGNORECASE)

    # Recursively walk through the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            match = pattern.match(file)
            if match:
                number = int(match.group(1))
                # Only include files where number >= 1 (exclude cover.0.*)
                if number >= 1:
                    file_path = os.path.join(root, file)
                    files_to_delete.append(file_path)

    if files_to_delete:
        print(f"\nFound {len(files_to_delete)} numbered cover files to delete:\n")
        for file_path in sorted(files_to_delete):
            print(file_path)
        
        print("\n" + "="*60)
        print(f"Total files to delete: {len(files_to_delete)}")
        print("="*60)
        print("\nDelete the following files?")
        print("[Y]es, [N]o")
        choice = input("> ").lower().strip()

        if choice == "y":
            deleted_count = 0
            failed_count = 0
            for file_path in files_to_delete:
                try:
                    os.remove(file_path)
                    deleted_count += 1
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    failed_count += 1
                    print(f"Cannot delete: {file_path} - {str(e)}")
            
            print(f"\nCompleted: {deleted_count} deleted, {failed_count} failed")
        else:
            print("Deletion cancelled.")
    else:
        print("No numbered cover files found!")


def term_args():
    parser = argparse.ArgumentParser(
        description="Find and optionally delete numbered cover art files (cover.1.jpg, cover.2.png, etc.)."
    )
    parser.add_argument("-p", "--path", type=str, help="Path to directory to search for numbered cover files.")
    return parser.parse_args()


if __name__ == '__main__': 
    main()
