import os
import praw
from config import Config
import requests
from download_image import DownloadImage
from image_checks import ImageChecks
from PIL import Image
from io import BytesIO

class RedditImages(DownloadImage):

    def __init__(self, config: Config):
        self.config =  config
        self.reddit = praw.Reddit(
            client_id = config.reddit_config.client_id,
            client_secret= config.reddit_config.client_secret,
            user_agent = config.reddit_config.user_agent)

                     
    def download_image(self, url):
        filename = os.path.basename(url)
        file_exists=os.path.isfile(os.path.join(self.config.wallpapers_path,filename))

        print(f"url: {url}")
        print(f"filename: {filename}")
        print(f"file_exists: {file_exists}")

        if not file_exists:             
            full_path = os.path.join(self.config.wallpapers_path, filename)
            response = requests.get(url)

            print(f"status: {response.status_code}")

            if response.status_code >= 200 and response.status_code < 300:

                try:
                    img = Image.open(BytesIO(response.content))

                    is_good_aspect_ratio = ImageChecks.is_good_aspect_ratio(img)
                    print(f"Is a good aspect ratio {is_good_aspect_ratio}")

                    if is_good_aspect_ratio:
                        print(f"downloading {filename}")
                        img.save(full_path)
                        return full_path
                    else:
                        return ""
                except Exception as e:
                    print(f"An error occurred: {e}")
                    return ""
            else:
                return ""
        else:
            return ""

    def get_images(self):
        posts = self.get_submissions()
        
        count=0
        download_imgs = []

        for post in posts:
            if post.url.endswith(tuple(self.config.filter.image_extensions)):
                count=count+1
                print(f"count: {count}")
                
                try:
                    url = (post.url)
                    img = self.download_image(url)
                    if img != "":
                        download_imgs.append(img)

                    print(f"download_count: {len(download_imgs)}")         
                    if len(download_imgs) >= self.config.reddit_config.filter.image_count:
                        print("Gathered enough images")
                        break
                except Exception as e:
                    print(f"url: {url}")
                    print(f"An error occurred: {e}")

        print('Done')
        return download_imgs
    

    def get_submissions(self):
        search_sub_reddits = self.config.reddit_config._reddit_filter.search_sub_reddits
        search_keywords = self.config.reddit_config.get_all_keywords()
        time_filter = "month" # options all, day, hour, month, week, year
        post_limit =  self.config.reddit_config._reddit_filter.post_limit # 
        sort = "new"


        subreddit = self.reddit.subreddit(search_sub_reddits)

        # format keyword list
        
        
        try:
            print(f"Searching {search_sub_reddits}")
            print(f"query={search_keywords}")
            print(f"time_filter={time_filter}")
            print(f"limit={post_limit }")
            print(f"sort={sort}")
            return subreddit.search(query=search_keywords, time_filter=time_filter, limit=post_limit , sort=sort)
        except praw.exceptions.PRAWException as e:
            print(f"An error occurred: {e}")
            return []