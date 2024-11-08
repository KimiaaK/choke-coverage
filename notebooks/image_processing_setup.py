# Stage 1: Image Processing Setup
# File: image_processing_setup.py

from PIL import Image
import numpy as np

def load_and_preprocess_image(image_path):
    # Load the image
    image = Image.open(image_path)

    # Convert the image to grayscale
    gray_image = image.convert('L')

    # Convert the grayscale image to a numpy array
    gray_array = np.array(gray_image)
    
    return image, gray_array

def define_circle_region(gray_array):
    # Calculate the center and radius of the circle for the region of interest
    height, width = gray_array.shape
    center_x, center_y = width // 2, height // 2
    radius = min(center_x, center_y) // 2
    
    return center_x, center_y, radius
