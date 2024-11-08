# Stage 2: Image Analysis
# File: image_analysis.py

import numpy as np
import matplotlib.pyplot as plt
from image_processing_setup import load_and_preprocess_image, define_circle_region


def process_image(image_path, lower_threshold=165, upper_threshold=255):
    # Load and preprocess the image
    image, gray_array = load_and_preprocess_image(image_path)

    # Define the circular region of interest
    center_x, center_y, radius = define_circle_region(gray_array)

    # Create a mask for the circular region
    y, x = np.ogrid[: gray_array.shape[0], : gray_array.shape[1]]
    distance_from_center = (x - center_x) ** 2 + (y - center_y) ** 2
    mask = distance_from_center <= radius**2

    # Apply the threshold and mask to identify white pixels
    thresholded_image = (gray_array >= lower_threshold) & (
        gray_array <= upper_threshold
    )
    white_pixels_in_circle = np.sum(thresholded_image & mask)
    total_pixels_in_circle = np.sum(mask)

    # Calculate the percentage of white pixels
    white_pixels_percentage = (white_pixels_in_circle / total_pixels_in_circle) * 100

    # Visual representation for debugging (optional)
    return white_pixels_percentage, image, thresholded_image, mask
