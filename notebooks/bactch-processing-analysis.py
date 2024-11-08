# Stage 3: Batch Processing and Analysis
# File: batch_processing_analysis.py

import numpy as np
import matplotlib.pyplot as plt
from image_analysis import process_image


def batch_process_images(image_paths):
    percentages = []
    for path in image_paths:
        percentage, _, _, _ = process_image(path)
        percentages.append(percentage)

    # Calculate the average percentage
    average_percentage = sum(percentages) / len(percentages)

    # Print the results
    print("White pixels percentage for each image:")
    for i, percentage in enumerate(percentages, start=1):
        print(f"Image {i}: {percentage:.2f}%")

    print(
        f"\nAverage percentage of white pixels across all images: {average_percentage:.2f}%"
    )

    # Plotting the percentages as a linear plot
    percentages_sort = np.sort(percentages)
    plt.figure(figsize=(8, 5))
    plt.plot(
        range(1, len(percentages_sort) + 1),
        percentages_sort,
        marker="o",
        linestyle="-",
        color="b",
    )
    plt.title("Rate of White Pixels Across Images")
    plt.xlabel("Image Number")
    plt.ylabel("Percentage of White Pixels (%)")
    plt.xticks(range(1, len(percentages_sort) + 1))  # Set x-ticks to image indices
    plt.grid(True)
    plt.show()


# List of image paths
image_paths = [
    "Pic1.png",
    "Pic2.png",
    "Pic3.png",
    "Pic4.png",
]

# Batch process images
batch_process_images(image_paths)
