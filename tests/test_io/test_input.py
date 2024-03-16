import unittest
from app.io.input import read_from_file, read_from_file_pandas


class TestReadFromFile(unittest.TestCase):

    def test_read_from_file(self):
        text_from_file = read_from_file('./data/text.txt')
        self.assertTrue(isinstance(text_from_file, str))
        self.assertTrue(len(text_from_file) > 0)

    def test_read_from_file_invalid_type(self):
        with self.assertRaises(TypeError) as _:
            read_from_file(5)

    def test_read_from_non_existing_file(self):
        with self.assertRaises(FileNotFoundError) as _:
            read_from_file('./data/unknown.txt')


class TestReadFromFilePandas(unittest.TestCase):

    def test_read_from_file(self):
        text_from_file = read_from_file_pandas('./data/jsn.json')
        print(type(text_from_file))
        self.assertTrue(len(text_from_file) > 0)

    def test_read_from_file_invalid_type(self):
        with self.assertRaises(TypeError) as _:
            read_from_file_pandas(5)

    def test_read_from_non_existing_file(self):
        with self.assertRaises(FileNotFoundError) as _:
            read_from_file_pandas('./data/unknown.json')


if __name__ == '__main__':
    unittest.main()
