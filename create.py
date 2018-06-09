#!/usr/bin/python3
import sys
import os


def write_playlist(directory):
    # Use directory name as playlist name
    dir = os.path.basename(os.path.normpath(directory))
    # Create relative paths using the directory name and file names
    songs = ["{}/{}".format(dir, f) for f in os.listdir(directory)]
    # Write paths to file
    with open("{}.m3u8".format(dir), 'w') as f:
        f.write('\n'.join(songs))


if __name__ == '__main__':
    # Make sure we have at least one filename
    if len(sys.argv) < 2:
        print("No filename given")
        sys.exit(1)
    # Create playlists
    for directory in sys.argv[1:]:
        write_playlist(directory)
