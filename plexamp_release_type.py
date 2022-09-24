from mutagen.flac import FLAC
import os

directory = "/Volumes/Backup/Music/"
filetypes = (".flac")

plex_release_types = {
    "live": "album;live",
    "compilation": "album;compilation",
    "remix": "album;remix",
    "mixtape": "album;mixtape",
    "soundtrack": "album;soundtrack"
}

for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(filetypes):
            if file.endswith(".flac"):
                try:
                    audio = FLAC(root + "/" + file)
                    rt = audio["releasetype"][0].lower().strip()
                except:
                    continue

                if rt == "live":
                    audio["releasetype"] = plex_release_types["live"]
                    print(root + "/" + file + " - UPDATED TO " + plex_release_types["live"])
                    audio.save()
                elif rt == "compilation":
                    audio["releasetype"] = plex_release_types["compilation"]
                    print(root + "/" + file + " - UPDATED TO " + plex_release_types["compilation"])
                    audio.save()

                elif rt == "remix":
                    audio["releasetype"] = plex_release_types["remix"]
                    print(root + "/" + file + " - UPDATED TO " + plex_release_types["remix"])
                    audio.save()

                elif rt == "mixtape":
                    audio["releasetype"] = plex_release_types["mixtape"]
                    print(root + "/" + file + " - UPDATED TO " + plex_release_types["mixtape"])
                    audio.save()

                elif rt == "soundtrack":
                    audio["releasetype"] = plex_release_types["soundtrack"]
                    print(root + "/" + file + " - UPDATED TO " + plex_release_types["soundtrack"])
                    audio.save()