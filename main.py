import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from seam_carving.energy import calculate_energy
from seam_carving.seam import find_seam

def main():
    image = mpimg.imread('images/input/test.jpg').astype(np.int64)
    energy = calculate_energy(image)
    seam = find_seam(energy)
    print(seam)
    # plt.imshow(seam)
    # plt.show()

if __name__ == "__main__":
    main()
