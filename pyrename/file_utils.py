"""
File utilities module for handling file operations.

This module provides functions to list files in a directory that match given
extensions and to rename files to their corresponding hash names.
"""

import os


def list_filtered_files(dir_path, extensions):
    """
    List all files in a directory that match the given extensions.

    Args:
        dir_path (str): The directory path to search for files.
        extensions (set): A set of file extensions to filter by.

    Returns:
        list: A list of full file paths that match the given extensions.
    """
    file_list = os.listdir(dir_path)
    filtered_files = [file for file in file_list if file.split('.')[-1].lower() in extensions]
    full_path_files = [os.path.join(dir_path, file) for file in filtered_files]
    return full_path_files

def rename_files(original_files, hashed_files, dir_path):
    """
    Rename a list of files to their corresponding hash names.

    Args:
        original_files (list): A list of full paths to the original files.
        hashed_files (list): A list of hashed file names (with extensions).
        dir_path (str): The directory path where the files are located.
    """
    for original_name, hash_ext in zip(original_files, hashed_files):
        new_name = os.path.join(dir_path, hash_ext)
        print(f"{os.path.basename(original_name)} -> {os.path.basename(new_name)}")
        os.rename(original_name, new_name)
