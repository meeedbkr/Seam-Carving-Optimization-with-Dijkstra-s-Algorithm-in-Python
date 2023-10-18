import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

def main():
    image = mpimg.imread('images/input/test.jpg').astype(np.int64)
    plt.imshow(image)
    plt.show()

if __name__ == "__main__":
    main()
