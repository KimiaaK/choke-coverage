import matplotlib.pyplot as plt


def plot_results(image, thresholded_image, color_image):
    # Plotting the original, thresholded, and colorized images
    plt.figure(figsize=(15, 5))
    plt.subplot(1, 3, 1)
    plt.imshow(image)
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.imshow(thresholded_image, cmap="gray")
    plt.title("Thresholded Image")
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.imshow(color_image)
    plt.title("Visual Representation")
    plt.axis("off")

    plt.show()
