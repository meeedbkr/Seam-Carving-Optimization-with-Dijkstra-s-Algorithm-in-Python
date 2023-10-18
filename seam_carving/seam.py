import numpy as np

def find_seam(energy):
    """
    Find a seam in an energy map.

    Args:
        energy (numpy.ndarray): Energy map.

    Returns:
        list of tuple: Seam coordinates.
    """
    height, width = energy.shape
    dp = np.copy(energy)
    
    for y in range(1, height):
        for x in range(0, width):
            left = max(0, x - 1)
            right = min(width - 1, x + 1)
            dp[y, x] += min(dp[y-1, left], dp[y-1, x], dp[y-1, right])
    
    seam = []
    x = np.argmin(dp[-1, :])
    for y in range(height - 1, -1, -1):
        seam.append((x, y))
        left = max(0, x - 1)
        right = min(width - 1, x + 1)
        choices = [dp[y-1, left], dp[y-1, x], dp[y-1, right]]
        x += (choices.index(min(choices)) - 1)
    return seam



def remove_seam(image, seam):
    """
    Remove a seam from an image.

    Args:
        image (numpy.ndarray): Input image.
        seam (list of tuple): Seam coordinates.

    Returns:
        numpy.ndarray: Image with seam removed.
    """
    height, width, _ = image.shape
    newImg = np.zeros((height, width - 1, 3), dtype=np.float64)

    for y in range(height):
        j = 0
        for x in range(width):
            if x != seam[y][0]:
                newImg[y, j] = image[y, x]
                j += 1

    return newImg

    return new_image