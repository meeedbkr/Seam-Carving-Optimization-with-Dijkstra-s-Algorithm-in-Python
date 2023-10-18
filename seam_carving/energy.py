import numpy as np

def calculate_energy(image):
    """
    Calculate the energy map of an image.

    Args:
        image (numpy.ndarray): Input image.

    Returns:
        numpy.ndarray: Energy map.
    """
    gray_image = np.mean(image, axis=2)
    gradient_x = np.gradient(gray_image, axis=1)
    gradient_y = np.gradient(gray_image, axis=0)
    energy = np.sqrt(gradient_x**2 + gradient_y**2)
    return energy
