# -*- coding: utf-8 -*-


import _config

config = {
    'DICT_FILE' : 'words.txt',
    'MIN_WORD_LEN' : 1 ,
    'MIN_DICT_WORD_LEN' : 2
}

class Config(object):
    def __init__(self):
        self._config = dict(_config._config.items() + config.items())

    def get_property(self, property_name):
        if property_name not in self._config.keys():
            return None
        return self._config[property_name]

    @property
    def dict_file_path(self):
        return self.get_property('DICT_FILE')

    @property
    def minimum_word_length(self):
        return self.get_property('MIN_WORD_LEN')

    @property
    def minimum_dict_word_length(self):
        return self.get_property('MIN_DICT_WORD_LEN')

class TwitterConfig(Config):

    @property
    def consumer_key(self):
        return self.get_property('consumer_key')

    @property
    def consumer_secret(self):
        return self.get_property('consumer_secret')

    @property
    def access_token(self):
        return self.get_property('access_token')

    @property
    def access_secret(self):
        return self.get_property('access_secret')


if __name__ == "__main__":
    print "Testing Config"
    conf = Config()
    print conf.minimum_dict_word_length
    print conf.minimum_word_length
