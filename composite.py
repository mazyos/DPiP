class FileSystemObject (object):
    '''fileやfolderに対する抽象基底クラス、Composite Pattern 実装'''
    def get_size (self):
        pass
    def get_numOfContents(self):
        pass

class File (FileSystemObject):
    '''Fileを抽象するオブジェクト'''
    def __init__(self, name, size, line):
        self._name = name
        self._size = size
        self._line = line
    def get_name(self):
        return self._name
    def get_size(self):
        return self._size
    def get_numOfContents(self):
        return self._line

class Folder (FileSystemObject):
    '''Folderを抽象するオブジェクト'''
    def __init__(self, name):
        self._name = name
        self._fso = []
    def get_name(self):
        return self._name
    def get_size(self):
        s = 0
        for f in self._fso:
            s  = s + f.get_size()
        return s
    def get_numOfContents(self):
        return len(self._fso)
    def add(self, fileSystemObject):
        self._fso.append(fileSystemObject)
    def remove(self, fileSystemObject):
        self._fso.remove(fileSystemObject)
