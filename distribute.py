#!/usr/bin/python3
import sys
import os
import re
from urllib.parse import unquote


def get_songs(filename):
    # Pattern for matching only filenames from paths
    pattern = re.compile(r"(?:\\|\/)?([^\n\r\.\\\/]+\..+)")
    # Infer directory name from filename
    directory = os.path.splitext(pattern.search(filename).group(1))[0]
    # Read file and build songs using pattern for lines that aren't comments
    with open(filename, 'r') as rf:
        songs = [
            directory + '\\' + unquote(match.group(1)) for match in (
                pattern.search(line) for line in rf.readlines() if
                line[0] != "#"
            ) if match
        ]
    return songs


def get_distributed(songs):
    # Get total number of songs
    total_songs = sum(len(sublist) for sublist in songs)
    distributed = []
    last_next = None
    while len(distributed) < total_songs:
        # Order sublists by their length because we want to reduce the largest
        songs.sort(key=len, reverse=True)
        if songs[0][0] == last_next and len(songs) > 1 and len(songs[1]) > 0:
            # Take song from second largest list if the largest was used before
            # and it's possible to do so
            distributed.append(songs[1][0])
            songs[1].remove(songs[1][0])
            # Remember the next song of this list
            last_next = songs[1][0] if len(songs[1]) > 0 else None
        else:
            # Otherwise, take song from the largest list
            distributed.append(songs[0][0])
            songs[0].remove(songs[0][0])
            # Remember the next song of this list
            last_next = songs[0][0] if len(songs[0]) > 0 else None
    return distributed


def main():
    # Make sure we have at least one filename
    if len(sys.argv) < 2:
        print("No filename given")
        sys.exit(1)
    # Get songs from playlists
    playlists = [get_songs(filename) for filename in sys.argv[1:]]
    # Distribute songs
    distributed = get_distributed(playlists)
    # Write to file
    with open('distributed.m3u8', 'w') as f:
        f.write('\n'.join(distributed))


if __name__ == '__main__':
    main()
