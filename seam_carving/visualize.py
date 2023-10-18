import numpy as np
import matplotlib.image as mpimg

def draw_seam(image, seam):
    """
    Highlight a seam in the image.

    Args:
        image (numpy.ndarray): Input image.
        seam (list of tuple): Seam coordinates to highlight.

    Returns:
        numpy.ndarray: Image with seam highlighted.
    """
    for x, y in seam:
        image[y, x] = [255, 0, 0]  # Highlight seam in red
    return image / 255  # Normalize the values to the 0-1 range
