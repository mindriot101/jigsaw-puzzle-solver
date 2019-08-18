#!/usr/bin/env python

from side_extractor import process_piece
import cv2


if __name__ == "__main__":
    image_filename = "images/IMG_20180415_211104234.jpg"
    image = cv2.imread(image_filename)

    result = process_piece(image)
