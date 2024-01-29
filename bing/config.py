from base.image_config import ImageConfig
from base.image_filter import ImageFilter

class BingConfig:

    def __init__(self, config:ImageConfig):
        self.__bing_data =  config.config_json["bing"]
        self._api_key:str = self.__bing_data["apiKey"]
        self._endpoint:str = self.__bing_data["endpoint"]
        self._filter = config.filter

        ImageConfig

    def get_all_keywords(self):
        return ' OR '.join(['(' + self.convert_keyword(item) + ')' if ' ' in item else item for item in self._filter.keywords])
    
    def convert_keyword(self, keyword):
        return keyword.replace(' ', ' AND ')

    @property 
    def api_key(self):
        return self._api_key
    
    @property
    def endpoint(self):
        return self._endpoint