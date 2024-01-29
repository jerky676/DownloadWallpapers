import praw
from base.image_config import ImageConfig
from base.download_image import DownloadImage
from reddit.config import RedditConfig
from praw.models import SubredditHelper

class RedditImages(DownloadImage):

    def __init__(self, config:ImageConfig):
        self.reddit_config = RedditConfig(config)
        self.reddit = praw.Reddit(
            client_id = self.reddit_config.client_id,
            client_secret= self.reddit_config.client_secret,
            user_agent = self.reddit_config.user_agent)
    
    @property
    def config(self):
        return self.reddit_config

    def get_images(self):
        keywords = self.reddit_config.get_keywords()

        images = []

        for keyword in keywords:
            print(f"keyword: {keyword}")

            urls = self.get_urls(keyword)

            if len(urls) > 0:
                downloaded_images = self.download_images(urls)
                images.extend(downloaded_images)
            else:
                print("No images found")


        print('Done')


    def get_urls(self,keyword):
        subreddit = self.reddit.subreddit(self.reddit_config.search_sub_reddits)

        try:
            print(f"Searching {self.reddit_config.search_sub_reddits}")
            print(f"query={keyword}")
            print(f"time_filter={self.reddit_config.time_filter}")
            print(f"limit={self.reddit_config.post_limit}")
            print(f"sort={self.reddit_config.sort}")
            posts = subreddit.search(query=keyword,
                                    time_filter=self.reddit_config.time_filter,
                                    limit=self.reddit_config.post_limit,
                                    sort=self.reddit_config.sort)


            return list([post.url for post in posts ])
        except praw.exceptions.PRAWException as e:
            print(f"An error occurred: {e}")
            return []