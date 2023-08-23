from abc import ABC, abstractmethod


class DownloadImage(ABC):

    @abstractmethod
    def get_images():
        pass