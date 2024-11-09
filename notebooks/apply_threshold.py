import numpy as np


def apply_threshold(gray_array, lower_threshold=165, upper_threshold=255):
    # Define the threshold values for white pixels
    return (gray_array >= lower_threshold) & (gray_array <= upper_threshold)
