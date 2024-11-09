import numpy as np


def colorize_image(gray_array, thresholded_image):
    # Create a color version of the grayscale image with red highlights for white pixels
    color_image = np.stack((gray_array, gray_array, gray_array), axis=-1)
    color_image[thresholded_image] = [255, 0, 0]  # Red color for white pixels
    return color_image
