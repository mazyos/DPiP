import unittest
import iterator

class BookTest (unittest.TestCase):
    def test_initiate (self):
        b = iterator.Book('title-01')
        self.assertEqual('title-01', b.get_title())

class BookShelfTest (unittest.TestCase):
    def test_initiate (self):
        bs = iterator.BookShelf()
        self.assertIsInstance(bs, iterator.BookShelf)
    def test_add_book(self):
        bs = iterator.BookShelf()
        b1 = iterator.Book('title-01')
        b2 = iterator.Book('title-02')
        bs.add_book(b1)
        bs.add_book(b2)

class ItereterTest (unittest.TestCase):
    def test_get_books(self):
        titles = ('title-01', 'title-02')
        bs = iterator.BookShelf()
        b1 = iterator.Book(titles[0])
        b2 = iterator.Book(titles[1])
        bs.add_book(b1)
        bs.add_book(b2)
        for b in bs:
            self.assertIn(b.get_title(), titles)


if __name__ == '__main__':
    unittest.main()
