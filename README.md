# JBOMLS
Just a Bunch Of Music Library Scripts

This is a handful of scripts that I use to maintain my music library.
The code is subpar. Contribute if you'd like!

## cleanup_orphan_dirs.py
This script will look through a provided path (music library) and remove any directory that holds just one image file.

### Example:
Below would be deleted

```
/Music/Talk Talk/[1991] Laughing Stock

Music
+-- Talk Talk
    +-- [1991] Laughing Stock
        +-- cover.jpg
```

However the below directory would not be deleted

```
/Music/Talk Talk/[1982] The Party's Over

Music
+-- Talk Talk
    +-- [1982] The Party's Over
        +-- cover.jpg
        +-- 01 Talk Talk.flac
        +-- 02 It’s So Serious.flac
        ...
```

## flac_to_lame.py
Pretty straightforward this script will transcode a directory containing flac files into MP3 320 and/or MP3 V0 files.

## hifi_to_cdq.py
This script will trancode any flac file into CD quality 16bit, 44.1kHz.

## plexamp_release_type.py
Plex/Plexamp does not read RELEASETYPE metatags unless it is in a correct format. This script will go through and update the RELEASETYPE for any flac file in a provided directory.

### Example:

01 Talk Talk.flac has a release type of Live. This will not show under Plex/Plexamp's Live Albums grouping. 
This script will change the release type from Live to album;live. The file will then show under the Live Albums grouping.


| Release Type | New Release Type  |
|--------------|-------------------|
| live         | album;live        |
| compilation  | album;compilation |
| remix        | album;remix       |
| mixtape      | album;mixtape     |
| soundtrack   | album;soundtrack  |

## recursive_transcode.py
Will recursively transcode a folder and all of it's subfolders to the destination file type.  Rebuilds the original folder structure while copying the transcoded files to the destination. 

## non_log_flacs.py
This script will look through the provided path and go 2 folders deep (depth=1) and report on any lossless album that does not have a log file in that directory.

### Example:
Below would show up on the report since there is no log file in the album directory.

```
/Music/Talk Talk/[1991] Laughing Stock

Music
+-- Radiohead
    +-- [1997] Karma Police (Single)
        +-- cover.jpg
        +-- 01 Karma Police
```

However the below directory would not show up on the report

```
/Music/Radiohead/[1997] Karma Police (Single)

Music
+-- Radiohead
    +-- [1997] Karma Police (Single)
        +-- cover.jpg
        +-- 01 Karma Police
        +-- Karma Police.log
```