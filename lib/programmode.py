from lib import utils

class Stockholm():
    """Defines """
    def __init__(self, silence, crypt):
        self.silence = silence
        self.crypt = crypt
        self.key = utils.KeyExist()
        self._lst = utils.load_list_ext()

    def set_key(self, k):
        self.key = k
    
    def set_crypt(self, k):
        self.crypt = k
    
    def set_silence(self, k):
        self.silence = k