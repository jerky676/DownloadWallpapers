from abc import ABC, abstractmethod, abstractproperty
import os
import time
import requests
from PIL import Image
from io import BytesIO
from base.image_config import ImageConfig


class DownloadImage(ABC):

    @abstractmethod
    def get_images(self):
        pass

    @abstractproperty
    def config(self)-> ImageConfig:
        pass

    def is_good_aspect_ratio(self,img:Image):
        print("checking image")
        print("checking aspect ratio")
        ratio = abs(img.width/img.height)
        print(f"{img.width}/{img.height}")
                    
        return True if 1.5 <= ratio <= 1.8 else False
   
    def download_images(self, urls):
        downloaded_images = []

        for url in urls:
            print(f"checking {url}")
            if url.endswith(tuple(self.config.filter.image_extensions)):
                image = self.download_image(url)

                if image is not None:
                    downloaded_images.append(image)

                print(f"downloaded {len(downloaded_images)} images")

                if len(downloaded_images) >= self.config.filter.image_count:
                    print("Gathered enough images")
                    break
        
        return downloaded_images
   
    def download_image(self, url):
        filename = os.path.basename(url)
        full_path = os.path.join(self.config.wallpapers_path, filename)

        if not os.path.isfile(full_path):       

            headers = {
                "user-agent": "curl/7.84.0",
                "accept": "*/*"
            }
            try:
                response = requests.get(url,headers=headers)
            except Exception as e:
                print(f"An error occurred: {e}")
                return None


            print(f"status: {response.status_code}")

            if response.status_code >= 200 and response.status_code < 300:

                try:
                    img = Image.open(BytesIO(response.content))

                    is_good_aspect_ratio = self.is_good_aspect_ratio(img)
                    print(f"Is a good aspect ratio {is_good_aspect_ratio}")

                    if is_good_aspect_ratio:
                        print(f"downloading {filename}")
                        img.save(full_path)
                        time.sleep(2) 
                        return full_path
                    else:
                        return  None
                except Exception as e:
                    print(f"An error occurred: {e}")
                    return None
            else:
                return None
        else:
            print(f"Already downloaded {filename}")
            return None