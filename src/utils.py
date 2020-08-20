import os
from webapp import app

class Utilities:
    def __init__(self):
        pass

    def clean(self):
        for the_file in os.listdir('./workdir/'):
            file_path = os.path.join('./workdir/', the_file)
            if os.path.isfile(file_path):
                os.unlink(file_path)
        for the_file in os.listdir('./result/'):
            file_path = os.path.join('./result/', the_file)
            if os.path.isfile(file_path):
                os.unlink(file_path)
        return None
        pass
