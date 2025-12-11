# JBOMLS

**Just a Bunch Of Music Library Scripts**

A collection of Python scripts for maintaining and organizing music libraries. These tools help with cleanup, transcoding, metadata management, and library maintenance tasks.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Scripts](#scripts)
  - [Cleanup Scripts](#cleanup-scripts)
  - [Transcoding Scripts](#transcoding-scripts)
  - [Metadata Scripts](#metadata-scripts)
  - [Utility Scripts](#utility-scripts)

## Requirements

- Python 3.6+
- ffmpeg (must be installed and available in PATH)
- Dependencies listed in `requirements.txt`:
  - `ffmpeg-python`
  - `filetype`
  - `mutagen` (for FLAC metadata editing)

## Installation

1. Clone or download this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Ensure `ffmpeg` is installed and accessible from your command line

## Scripts

### Cleanup Scripts

#### cleanup_orphan_dirs.py

Removes directories that contain only a single image file (typically orphaned cover art directories).

**Usage:**
```bash
python cleanup_orphan_dirs.py -p /path/to/music/library
```

**Example:**
The following directory would be deleted:
```
/Music/Talk Talk/[1991] Laughing Stock/
    └── cover.jpg
```

The following directory would **not** be deleted (contains audio files):
```
/Music/Talk Talk/[1982] The Party's Over/
    ├── cover.jpg
    ├── 01 Talk Talk.flac
    ├── 02 It's So Serious.flac
    └── ...
```

#### cleanup_orphan_dirs_v2.py

Finds album directories (at depth 1: `library/artist/album`) that don't contain audio files. Checks for audio files with a specific pattern (looking for '01 ' in filenames). If an album directory doesn't contain matching audio files, it will offer to delete the directory.

**Usage:**
```bash
python cleanup_orphan_dirs_v2.py -p /path/to/music/library
```

#### cleanup_orphan_dirs_v3.py

An improved version of the orphan directory cleanup script. Uses the `filetype` library to properly detect audio files and recursively checks subdirectories for any music files. If an album directory (at depth 1: `library/artist/album`) has no music files anywhere within it, it will offer to delete the directory. More reliable than v2 as it uses proper audio file detection rather than filename pattern matching.

**Usage:**
```bash
python cleanup_orphan_dirs_v3.py -p /path/to/music/library
```

### Transcoding Scripts

#### flac_to_lame.py

Transcodes FLAC files in a directory to MP3 format. Supports both 320kbps and V0 quality settings.

**Usage:**
```bash
python flac_to_lame.py -p /path/to/flac/directory -t 320 v0
```

**Options:**
- `-p, --path`: Path to directory containing FLAC files
- `-t, --transcodes`: Transcode options - choose `320` (320kbps), `v0` (V0 quality), or both

**Note:** Creates subdirectories `mp3_320/` and/or `mp3_v0/` in the source directory.

#### hifi_to_cdq.py

Transcodes lossless audio files (FLAC, WAV, MKA) to CD quality FLAC (16-bit, 44.1kHz).

**Usage:**
```bash
python hifi_to_cdq.py -p /path/to/audio/directory
```

**Note:** Creates a `transcode/` subdirectory in the source directory with the converted files.

#### recursive_transcode.py

Recursively transcodes lossless audio files (FLAC, WAV) throughout a directory structure and rebuilds the original folder structure at the destination. Converts to ALAC format by default.

**Usage:**
```bash
python recursive_transcode.py -p /path/to/source -o /path/to/destination
```

**Options:**
- `-p, --path`: Source directory to transcode
- `-o, --output_path`: Destination directory for transcoded files

### Metadata Scripts

#### plexamp_release_type.py

Updates RELEASETYPE metadata tags in FLAC files to the format required by Plex/Plexamp. Plex/Plexamp requires specific formatting for release types to properly categorize albums.

**Usage:**
```bash
python plexamp_release_type.py -p /path/to/music/library
```

**Example:**
A file with release type "Live" will be updated to "album;live" so it appears under Plex/Plexamp's Live Albums grouping.

**Supported Release Types:**

| Original Release Type | Updated Release Type |
|----------------------|---------------------|
| live                 | album;live          |
| compilation          | album;compilation   |
| remix                | album;remix         |
| mixtape              | album;mixtape       |
| soundtrack           | album;soundtrack    |

### Utility Scripts

#### folder_to_cover.py

Renames `folder.jpg` files to `cover.jpg` throughout a directory structure. Useful for standardizing cover art filenames in your music library.

**Usage:**
```bash
python folder_to_cover.py -p /path/to/music/library
```

#### no_cover.py

Reports album directories (those with "[" in the path, indicating album naming convention) that don't have a `cover.jpg` file. Prints out the paths of directories missing cover art.

**Usage:**
```bash
python no_cover.py -p /path/to/music/library
```

#### non_log_flacs.py

Scans a music library and reports on lossless albums (at depth 1: `library/artist/album`) that do not have a log file in the album directory. Useful for identifying albums that may be missing EAC/ripping logs.

**Usage:**
```bash
python non_log_flacs.py -p /path/to/music/library
```

**Example:**
The following directory would show up in the report (no log file):
```
/Music/Radiohead/[1997] Karma Police (Single)/
    ├── cover.jpg
    └── 01 Karma Police.flac
```

The following directory would **not** show up (has log file):
```
/Music/Radiohead/[1997] Karma Police (Single)/
    ├── cover.jpg
    ├── 01 Karma Police.flac
    └── Karma Police.log
```

## Contributing

Contributions are welcome! Feel free to submit issues, improvements, or new scripts.
