"""
Unit tests for file_utils module.
"""
import os
import tempfile
import unittest

from pyrename.file_utils import list_filtered_files, rename_files


class TestFileUtils(unittest.TestCase):
    """
    Tests for file_utils module.
    """
    def setUp(self):
        self.test_dir = tempfile.TemporaryDirectory()
        self.test_files = ['test1.jpg', 'test2.png', 'test3.txt', 'TEST4.JPEG']
        self.full_paths = []

        for file in self.test_files:
            path = os.path.join(self.test_dir.name, file)
            with open(path, mode="w", encoding="utf-8") as f:
                f.write("test content")
            self.full_paths.append(path)

    def tearDown(self):
        self.test_dir.cleanup()

    def test_list_filtered_files(self):
        """
        Tests for list_filtered_files() function.
        """
        extensions = {"jpg", "png", "jpeg", "JPG"}
        filtered_files = list_filtered_files(self.test_dir.name, extensions)
        expected_files = [
            os.path.join(self.test_dir.name, 'test1.jpg'),
            os.path.join(self.test_dir.name, 'test2.png'),
            os.path.join(self.test_dir.name, 'TEST4.JPEG')
        ]
        self.assertCountEqual(filtered_files, expected_files)

    def test_rename_files(self):
        """
        Unit test for rename_files() function.
        """
        original_files = self.full_paths[:2]
        hashed_files = ["hashed1.jpg", "hashed2.png"]
        rename_files(original_files, hashed_files, self.test_dir.name)

        for original, new_name in zip(original_files, hashed_files):
            new_path = os.path.join(self.test_dir.name, new_name)
            self.assertTrue(os.path.exists(new_path))
            self.assertFalse(os.path.exists(original))

if __name__ == "__main__":
    unittest.main()
