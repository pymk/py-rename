"""
Hasher module for computing SHA-1 checksums.

This module provides a function to calculate the SHA-1 checksum of a file's
contents and return the hash combined with the original file extension.
"""

import hashlib
import os


def calculate_sha1(file_path):
    """
    Calculate the SHA-1 checksum of a file's contents and return the hash
    combined with the original file extension.

    Args:
        file_path (str): The full path to the file.

    Returns:
        str: The SHA-1 hash of the file contents with the original file extension.
    """
    with open(file_path, "rb") as f:
        content = f.read()
    file_hash = hashlib.sha1(content).hexdigest()
    ext = os.path.splitext(file_path)[1]
    return f"{file_hash}{ext}"
