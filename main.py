# Copyright University College London 2019
# Author: Alexander Whitehead, Institute of Nuclear Medicine, UCL
# For internal research only.


import os
import numpy
from PIL import Image


class Config:
    def __init__(self, top=0, bottom=0, left=0, right=0, input_suffix="", output_suffix=""):
        self.top = top
        self.bottom = bottom

        self.left = left
        self.right = right

        self.input_suffix = input_suffix
        self.output_suffix = output_suffix


def parse(config):
    with open("./data/config/config.par", 'r') as file:
        for line in file:
            line = line.rstrip()

            split_array = line.split("top:=")

            if len(split_array) == 2:
                config.top = int(split_array[1])

                continue

            split_array = line.split("bottom:=")

            if len(split_array) == 2:
                config.bottom = int(split_array[1])

                continue

            split_array = line.split("left:=")

            if len(split_array) == 2:
                config.left = int(split_array[1])

                continue

            split_array = line.split("right:=")

            if len(split_array) == 2:
                config.right = int(split_array[1])

                continue

            split_array = line.split("input_suffix:=")

            if len(split_array) == 2:
                config.input_suffix = str(split_array[1])

                continue

            split_array = line.split("output_suffix:=")

            if len(split_array) == 2:
                config.output_suffix = str(split_array[1])

                continue

    return config


def find(suffix):
    output_files = []
    path = "./data/images/"
    files = os.listdir(path)

    for i in range(len(files)):
        if files[i].endswith(suffix):
            output_files.append("./data/images/" + files[i])

    return output_files


def get_output_path(path, config):
    woop = '.' + path.split('.')[1] + config.output_suffix + '.' + config.input_suffix
    return woop


def crop(files, config):
    for i in range(len(files)):
        image = Image.open(files[i])
        image_array = numpy.array(image)

        image_array = image_array[config.top:config.bottom, config.left:config.right]

        image = Image.fromarray(image_array)
        image.save(get_output_path(files[i], config))


def main():
    config = Config(top=0, bottom=0, left=0, right=0, input_suffix="", output_suffix="")
    config = parse(config)

    files = find(config.input_suffix)

    crop(files, config)

    return 1


main()
