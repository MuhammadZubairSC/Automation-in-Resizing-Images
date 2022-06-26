!/usr/bin/env python3
import os
from PIL import Image
import glob

def load_images(folder):
    imageList = glob.glob(r"/home/student-00-6fe25b91bf27/supplier-data/images/*.tiff")
    print(imageList)
    try:
        for imgage in imageList:
            with Image.open(imgage) as im:
                im_rgb = im.convert("RGB")
                im_resize = im_rgb.resize((600,400))
                ConvertFormat=img.replace(".tiff", '')
                im.save(ConvertFormat+".jpeg", "JPEG")
                im.close()

    except IOError as e:
        print(e)

if __name__ == "__main__":
    filePath=os.path.join(os.getcwd(),'supplier-data/images/')
    print(filePath)
    dir = load_images(filePath)
