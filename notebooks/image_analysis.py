# Stage 2: Image Analysis
# File: image_analysis.py

import numpy as np
import matplotlib.pyplot as plt
from image_processing_setup import load_and_preprocess_image, define_circle_region


def process_image(image_path, lower_threshold=165, upper_threshold=255):
    # Load and preprocess the image
    image, gray_array = load_and_preprocess_image(image_path)

    # Define the circular region of interest
    center_x, center_y, radius, mask = define_circle_region(gray_array)

    # Apply the threshold and mask to identify white pixels
    # Apply the thresholds to create a black and white image, then apply the mask
    thresholded_image = (
        (gray_array >= lower_threshold) & (gray_array <= upper_threshold)
    ) & mask
    # Create a color version of the grayscale image
    color_image = np.stack((gray_array, gray_array, gray_array), axis=-1)
    color_image[thresholded_image] = [255, 0, 0]  # Red color for white pixels

    white_pixels_count = np.sum(thresholded_image)
    total_pixels_in_circle = np.sum(mask)
    white_pixels_percentage = (white_pixels_count / total_pixels_in_circle) * 100

    # Visual representation for debugging (optional)
    return white_pixels_percentage, image, thresholded_image, color_image, mask
