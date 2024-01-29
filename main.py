#!/usr/bin/env python3

import os
import json
# from bing.config import BingConfig
from base.image_config import ImageConfig
from reddit.config import RedditConfig
from reddit.images import RedditImages
from bing.images import BingImages

def main():
    config_file = f"{os.path.dirname(os.path.realpath(__file__))}/config.json"
   
    #bing_config = BingConfig(config_json["bing"], self.filter )
    # bing_images = BingImages(config)
    # images = bing_images.get_images()


    reddit_images = RedditImages(config_file)
    reddit_images.get_images()


if __name__ == "__main__":
    main()