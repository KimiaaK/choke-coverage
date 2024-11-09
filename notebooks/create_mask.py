import numpy as np


def create_mask(gray_array, offset_x=-10):
    # Calculate the center, radius, and apply mask
    height, width = gray_array.shape
    radius = min(height, width) // 3
    center_x = width // 2 + offset_x  # Adjusted center x
    center_y = height // 2
    y, x = np.ogrid[:height, :width]
    mask = (x - center_x) ** 2 + (y - center_y) ** 2 <= radius**2
    return mask
