import sys
import cv2
from duo import Duotone
from scale import automatic_brightness_and_contrast
import json
from PIL import Image, ImageColor


colors = {
    "dark": [80, 40, 90],
    "green": [190, 230, 180],
    "gray": [210, 210, 210],
    "yellow": [250, 215, 130],
    "blue": [140, 200, 250],
    "pink": [220, 160, 220],
    "red": [250, 160, 140],
    "purple": [170, 150, 250],
    "white": [255, 255, 255]
}

class Converter(object):
    def __init__(self, img_file):
        self.img_file = img_file
        self.colors = colors

    def convert(self, light="green", dark="dark", contrast=0.5, number=0):
        if self.img_file[-4:] != ".jpg":
            print("Only .jpg accepted")
            return
        img = cv2.imread(self.img_file)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = automatic_brightness_and_contrast(img)
        bw_file = self.img_file.replace(".jpg", "-bw.jpg")
        cv2.imwrite(bw_file, img)
        img = Image.open(bw_file)
        light_values = colors[light]
        dark_values = colors[dark]
        result = Duotone.process(img, light_values, dark_values, contrast)
        dt_file = self.img_file.replace(".jpg", "-%d.jpg" % number)
        result.save(dt_file, "JPEG")


    def main(self, filter=None, contrast=0.5):
        if filter == None:
            for i, light in enumerate(["green", "yellow", "blue", "pink", "red", "purple", "gray"]):
                print(i, light)
                self.convert(light=light, dark="dark", contrast=contrast, number=i)
        else:
            for i, light in enumerate(["green", "yellow", "blue", "pink", "red", "purple", "gray"]):
                if light == filter:
                    self.convert(light=light, dark="dark", contrast=contrast, number=i)
