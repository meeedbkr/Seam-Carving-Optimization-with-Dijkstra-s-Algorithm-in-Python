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