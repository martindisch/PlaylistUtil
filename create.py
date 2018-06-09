#!/usr/bin/python3
"""This module can be used to create playlist files for files in given
directories. Use as

./create.py /path/to/first/ /path/to/second

This will create playlists `first.m3u8` and `second.m3u8` in the working
directory.

"""
import sys
import os


def write_playlist(directory):
    """Create a playlist file for all files in the directory.

    It will only list all files in the directory (not recurse into
    subdirectories) and check neither whether a file is a file and not a
    directory nor whether it's actually a sound file.
    The resulting playlist file will have the name of the directory and the
    songs will be ordered alphabetically by filename.

    Parameters
    ----------
    directory : str
        The path to the directory containing the files
    """
    # Use directory name as playlist name
    dir = os.path.basename(os.path.normpath(directory))
    # Create relative paths using the directory name and file names
    songs = ["{}/{}".format(dir, f) for f in os.listdir(directory)]
    # Sort songs alphabetically
    songs.sort()
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
