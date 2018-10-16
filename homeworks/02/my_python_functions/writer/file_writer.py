import os
import pickle as pkl

class FileWriter:
    
    def __init__(self, path):
        """path - путь до файла"""
        if self._check_path(path):
            self.path_= path
            self.file = None
        else:
            self.path_=path
            os.system('"">c:\1.tx')
        
    def _check_path(self, path):
        return os.path.isdir(path)
    @property 
    def path(self):
        return self.path_
    @path.setter
    def path(self, path):
        if self._check_path(path):
            self.path_=path
        else:
            raise Exception("There is no path!")
    @path.getter
    def path(self):
        if self.path_!=None:
            return self.path_
        else:
            raise Exception("There is no path!")
    @path.deleter
    def path(self):
        del self.path_
    def print_file(self):
        if os.path.exists(self.path_):
            if os.path.isfile(self.path_):
                file = open(self.path_)
                for i in f:
                    print(i)
                    file.close
            else: 
                raise Exception("File is empty")
        else:
            raise Exception("There is no way")
    
    def __enter__(self):
        self.my_file=open(self.path, 'a')
        return self.my_file
    def __exit__(self, *args):
        self.my_file.close()
        del self.my_file
    def save_yourself(self, file_name):
        with open(file_name, 'wb') as dF:
            pkl.dump(self, dF)
    
    @classmethod
    def load_file_writer(cls, pickle_file):
        with open(pickle_file, 'rb') as dF:
            my_file=pkl.load(dF)
            return my_file