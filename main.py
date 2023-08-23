#!/usr/bin/env python3

import os
import json
from config import Config
from reddit.reddit_images import RedditImages

def main():
    config = Config(f"{os.path.dirname(os.path.realpath(__file__))}/config.json")

    reddit_images = RedditImages(config)
    reddit_images.get_images()

    # wall_paper = WallPapers(config)
    # wall_paper.choose_random_wallpaper()


if __name__ == "__main__":
    main()