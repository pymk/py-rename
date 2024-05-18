"""
Unit tests for hasher module.
"""
import os
import tempfile
import unittest

from pyrename.hasher import calculate_sha1


class TestHasher(unittest.TestCase):
    """
    Tests the calculate_sha1() function.
    """

    def setUp(self):
        self.test_file = tempfile.NamedTemporaryFile(delete=False)
        self.test_file.write(b"Hello, world!")
        self.test_file.close()

    def tearDown(self):
        os.remove(self.test_file.name)

    def test_calculate_sha1(self):
        """
        Tests the calculate_sha1() function.
        """
        expected_hash = "943a702d06f34599aee1f8da8ef9f7296031d699"
        self.assertEqual(calculate_sha1(self.test_file.name), expected_hash)

if __name__ == "__main__":
    unittest.main()
