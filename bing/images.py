import requests
import os
from base.image_config import ImageConfig
from bing.config import BingConfig

class BingImages:
    def __init__(self, config: ImageConfig):
        self.__bing_data = config.config_json["bing"]
        self.__bing_config = BingConfig(config)
        self.api_key = self.__bing_config.api_key
        self.endpoint = self.__bing_config.endpoint # "https://api.cognitive.microsoft.com/bing/v7.0/images/search"

    def download_images(self, query, size="Medium", count=10, save_path="images"):
        headers = {"Ocp-Apim-Subscription-Key": self.api_key}
        params = {
            "q": query,
            "count": count,
            "size": size,
            "safeSearch": "Moderate",  # You can change this based on your requirements
        }

        response = requests.get(self.endpoint, headers=headers, params=params)

        if response.status_code == 200:
            results = response.json().get("value", [])
            if not results:
                print("No images found for the given query.")
                return

            if not os.path.exists(save_path):
                os.makedirs(save_path)

            for i, result in enumerate(results):
                image_url = result["contentUrl"]
                image_extension = image_url.split(".")[-1]
                image_filename = f"{query}_{i + 1}.{image_extension}"
                image_path = os.path.join(save_path, image_filename)

                try:
                    image_data = requests.get(image_url).content
                    with open(image_path, "wb") as image_file:
                        image_file.write(image_data)
                    print(f"Downloaded: {image_filename}")
                except Exception as e:
                    print(f"Error downloading {image_filename}: {str(e)}")

        else:
            print(f"Error: {response.status_code}, {response.text}")


# Example usage
if __name__ == "__main__":
    api_key = "YOUR_API_KEY"
    downloader = BingImageDownloader(api_key)

    query = "nature"
    size = "Medium"  # You can change this to "Small", "Large", "Wallpaper", etc.
    count = 5
    save_path = "downloaded_images"

    downloader.download_images(query, size, count, save_path)
