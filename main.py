import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from seam_carving.energy import calculate_energy
from seam_carving.seam import find_seam
from seam_carving.visualize import draw_seam

def main():
    image = mpimg.imread('images/input/test.jpg').astype(np.int64)
    energy = calculate_energy(image)
    seam = find_seam(energy)
    # Draw and save the image with the seam
    image_with_seam = draw_seam(np.copy(image), seam)
    plt.imshow(image_with_seam)
    plt.show()

if __name__ == "__main__":
    main()
