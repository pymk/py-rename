"""
Main module to rename files in a directory to their SHA-1 checksums.

This module parses command-line arguments to get the directory path,
filters files by supported extensions, computes the SHA-1 hash for each file,
and renames the files to their hash values.
"""

import argparse

from pyrename.file_utils import list_filtered_files, rename_files
from pyrename.hasher import calculate_sha1


def main():
    """
    Rename files in a directory to their SHA-1 checksums.

    Parses command-line argument to get the directory path, filters files by
    supported extensions, computes the SHA-1 hash for each file, and renames
    the files to their hash values.
    """
    parser = argparse.ArgumentParser(description='Rename files to their SHA-1 checksum')
    parser.add_argument('path', type=str, help='The path to the file directory')
    args = parser.parse_args()

    dir_path = args.path
    extensions = {"jpeg", "jpg", "png", "JPEG", "JPG", "PNG"}

    full_path_files = list_filtered_files(dir_path, extensions)

    if len(full_path_files) == 0:
        print(f"No files found in {dir_path} with the following extensions: {extensions}")
        return

    hashes = [calculate_sha1(file) for file in full_path_files]

    rename_files(full_path_files, hashes, dir_path)

if __name__ == "__main__":
    main()
