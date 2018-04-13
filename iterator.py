class Book (object):
    def __init__(self, title):
        self._title = title
    def get_title(self):
        return self._title

class BookShelf (object):
    '''Bookを集約する本棚オブジェクト。Book集合へのiteratorを提供する'''
    def __init__(self):
        self._shelf = []
        self._index = 0
    def add_book(self, book):
        self._shelf.append(book)
    def __iter__(self):
        self._index = 0
        return self
    def __next__(self):
        if self._index == len(self._shelf):
            raise StopIteration
        b = self._shelf[self._index]
        self._index = self._index + 1
        return b