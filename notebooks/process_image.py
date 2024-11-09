from load_image import load_image
from create_mask import create_mask
from apply_threshold import apply_threshold
from colorize_image import colorize_image
from plot_results import plot_results
import numpy as np


def process_image(image_path):
    image, gray_array = load_image(image_path)
    mask = create_mask(gray_array)
    thresholded_image = apply_threshold(gray_array) & mask
    color_image = colorize_image(gray_array, thresholded_image)

    # Calculate the percentage of white pixels
    white_pixels_count = np.sum(thresholded_image)
    total_pixels_in_circle = np.sum(mask)
    white_pixels_percentage = (white_pixels_count / total_pixels_in_circle) * 100

    # Plotting the results
    plot_results(image, thresholded_image, color_image)

    return white_pixels_percentage
