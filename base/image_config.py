import json
import os
import sys
from base.image_filter import ImageFilter


class ImageConfig:

    def __init__(self, config_json_file):
        self._config_json_file = config_json_file

        if not os.path.isfile(self._config_json_file):
            print(f"Config file does not exist {self._config_json_file}")
            sys.exit(1)

        with open(self._config_json_file, "r") as f:
            self._config_json = json.load(f)

        self._pull_new_images:bool = self._config_json["pullNewImages"]
        self._random_keyword:bool = self._config_json["randomKeyword"]
        self._wallpapers_path = self._config_json ["wallpapersPath"]

        if "~" in self._wallpapers_path:
            self._wallpapers_path = os.path.expanduser(self._wallpapers_path)

        self._filter = ImageFilter(self._config_json["filter"])

   
    @property
    def wallpapers_path(self):
        return self._wallpapers_path
   
    @property
    def filter(self):
        return self._filter
    
    @property
    def config_json(self):
        return self._config_json