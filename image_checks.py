from PIL import Image

class ImageChecks:
    
    @staticmethod
    def is_good_aspect_ratio(img:Image):
        print("checking image")
        print("checking aspect ratio")
        ratio = abs(img.width/img.height)
        print(f"{img.width}/{img.height}")
                    
        return True if 1.5 <= ratio <= 1.8 else False
    