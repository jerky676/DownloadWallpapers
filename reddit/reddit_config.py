from filter import Filter

class RedditFilter:

    def __init__(self, json_data:str):
        self._sub_reddits:list[str] = json_data["subReddits"]
        self._post_limit:int = json_data["postLimit"]

    @property
    def search_sub_reddits(self):
        return '+'.join(self.sub_reddits)

    @property
    def sub_reddits(self):
        return self._sub_reddits
    
    @property
    def post_limit(self):
        return self._post_limit


class RedditConfig:

    def __init__(self, json_data,filter:Filter):
        self._client_id:str = json_data["clientId"]
        self._client_secret:str = json_data["clientSecret"]
        self._user_agent:str = json_data["userAgent"]
        self._sort:str = "month"
        self._time_filter:str = "relevance"
        self._reddit_filter = RedditFilter(json_data["filter"])
        self._filter = filter

    def get_all_keywords(self):
        return ' OR '.join(['(' + self.convert_keyword(item) + ')' if ' ' in item else item for item in self._filter.keywords])
    
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
        return self._time_filter

    @property
    def time_filter(self):
        return self._sort


