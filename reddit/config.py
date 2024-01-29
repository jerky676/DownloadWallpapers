import random
from base.image_filter import ImageFilter
from base.image_config import ImageConfig

class RedditConfig(ImageConfig):

    def __init__(self, config_json_file):
        super().__init__(config_json_file)
        self.__reddit_data =  self._config_json["reddit"]
        self._client_id:str = self.__reddit_data["clientId"]
        self._client_secret:str = self.__reddit_data["clientSecret"]
        self._user_agent:str = self.__reddit_data["userAgent"]
        self._sub_reddits:list[str] = self.__reddit_data["subReddits"]
        self._sort:str = "relevance"
        self._time_filter:str = "all"
        self._post_limit:int = self._filter.image_count * 3
        self._max_keywords:int = 5
        self.sort_options = ["relevance", "top", "new", "hot", "controversial", "rising"]

    def get_keywords(self):
        if len(self._filter.keywords) > self._max_keywords:
            keywords = random.choices(self._filter.keywords, k=self._max_keywords)
        else:
            keywords = self._filter.keywords

        return list(map(self.convert_keyword,keywords))

    def convert_keyword(self, keyword):
        return keyword.replace(' ', ' AND ')

    @property 
    def client_id(self):
        return self._client_id

    @property 
    def client_secret(self):
        return self._client_secret
    
    @property 
    def user_agent(self):
        return self._user_agent

    @property 
    def filter(self):
        return self._filter
    
    @property
    def sort(self):
        #return self._sort
        return random.choice(self.sort_options)

    @property
    def time_filter(self):
        return self._time_filter
    
    @property
    def search_sub_reddits(self):
        return '+'.join(self.sub_reddits)

    @property
    def sub_reddits(self):
        return self._sub_reddits
    
    @property
    def post_limit(self):
        return self._post_limit



