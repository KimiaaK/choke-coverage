# File: batch_process_images.py

from process_image import process_image
import numpy as np
import matplotlib.pyplot as plt
import os


def batch_process_images(image_folder):
    # Gather all image paths from the specified folder
    image_paths = [
        os.path.join(image_folder, file)
        for file in os.listdir(image_folder)
        if file.endswith((".png", ".jpg", ".jpeg"))
    ]

    percentages = [process_image(path) for path in image_paths]

    # Calculate and print average percentage
    average_percentage = sum(percentages) / len(percentages)
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
    plt.xticks(range(1, len(percentages_sort) + 1))
    plt.grid(True)
    plt.show()


# Folder containing images
if __name__ == "__main__":
    image_folder = "images"
    batch_process_images(image_folder)
