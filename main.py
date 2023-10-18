import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from seam_carving.energy import calculate_energy

def main():
    image = mpimg.imread('images/input/test.jpg').astype(np.int64)
    energy = calculate_energy(image)

    plt.imshow(energy)
    plt.show()

if __name__ == "__main__":
    main()
