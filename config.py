# -*- coding: utf-8 -*-


import _config 

class Config(object):
    def __init__(self):
        self._config = _config._config
 
    def get_property(self, property_name):
        if property_name not in self._config.keys():
            return None
        return self._config[property_name]
 

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