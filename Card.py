class Card(object):
    def __init__(self, img_path):
        self._img_path = img_path
        
    @property
    def img_path(self):
        return self._img_path

    @img_path.setter
    def img_path(self,value):
        self._img_path = value