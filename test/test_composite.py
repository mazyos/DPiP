import unittest
import composite

class TestFile (unittest.TestCase):
    def setUp(self):
        self._file = composite.File('file for test', 99, 10)
    def tearDown(self):
        self._file = None
    def test_get_size(self):
        self.assertEqual(99, self._file.get_size())
    def test_get_numOfContents(self):
        self.assertEqual(10, self._file.get_numOfContents())

class TestFolder (unittest.TestCase):
    def setUp(self):
        self._folder = composite.Folder('folder for test')
        self._f1 = composite.File('f1', 1, 1)
        self._f2 = composite.File('f2', 2, 2)

    def tearDown(self):
        self._folder = None

    def test_get_size(self):
        self._folder.add(self._f1)
        self.assertEqual(1, self._folder.get_size())

        self._folder.add(self._f2)
        self.assertEqual(3, self._folder.get_size())

    def test_get_numOfContents(self):
        self._folder.add(self._f1)
        self.assertEqual(1, self._folder.get_numOfContents())
        self._folder.add(self._f2)
        self.assertEqual(2, self._folder.get_numOfContents())

    def test_composite(self):
        self._folder.add(self._f1)
        folder2 = composite.Folder('folder2')
        folder2.add(self._f2)
        self._folder.add(folder2)

        self.assertEqual(3, self._folder.get_size())





if __name__ == '__main__':
    unittest.main()