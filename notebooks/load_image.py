# File: load_image.py

from PIL import Image
import numpy as np


def load_image(image_path):
    # Load and convert the image to grayscale
    image = Image.open(image_path)
    gray_image = image.convert("L")
    gray_array = np.array(gray_image)
    return image, gray_array
