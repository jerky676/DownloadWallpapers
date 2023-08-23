class Filter:

    def __init__(self, json_data):
        self._image_count:int = json_data["imageCount"]
        self._image_extensions:list[str] = json_data["imageExtensions"]
        self._keywords:list[str] = json_data["keywords"]
    
    @property
    def image_count(self):
        return self._image_count
    
    @property
    def image_extensions(self):
        return self._image_extensions

    @property
    def keywords(self):
        return self._keywords