import json
import os
import sys
import random
from reddit.reddit_config import RedditConfig
from filter import Filter


class Config:
    checks =[]

    def __init__(self, config_json_file):
        self.__config_json_file = config_json_file

        if not os.path.isfile(self.__config_json_file):
            print(f"Config file does not exist {self.__config_json_file}")
            sys.exit(1)

        with open(self.__config_json_file, "r") as f:
            config_json = json.load(f)

        self._pull_new_images:bool = config_json["pullNewImages"]
        self._random_keyword:bool = config_json["randomKeyword"]
        self._wallpapers_path = config_json ["wallpapersPath"]

        if "~" in self._wallpapers_path:
            self._wallpapers_path = os.path.expanduser(self._wallpapers_path)

        self.filter =  Filter(config_json["filter"])
        self._reddit_config = RedditConfig(config_json["reddit"], self.filter )
   
    @property
    def wallpapers_path(self):
        return self._wallpapers_path
   
    @property
    def reddit_config(self):
        return self._reddit_config