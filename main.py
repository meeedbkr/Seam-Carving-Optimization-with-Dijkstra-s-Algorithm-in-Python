import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from seam_carving.energy import calculate_energy
from seam_carving.seam import find_seam, remove_seam
from seam_carving.visualize import draw_seam
import os

def main():
    input_folder = 'images/input'
    output_folder = 'images/seam_output'
    image_name = 'test'
    removed_pixels = 100

    image = mpimg.imread(os.path.join(input_folder, f'{image_name}.jpg')).astype(np.float64)

    for i in range(removed_pixels):  # Adjust the number of seams to remove
        energy = calculate_energy(image)
        seam = find_seam(energy)

        # Draw and save the image with the seam
        image_with_seam = draw_seam(np.copy(image), seam)

        # Normalize the pixel values to 0-1 range
        # image_with_seam = image_with_seam / 255.0

        # Save the intermediate seam images
        if i % 50 == 0 and i>0:
            intermediate_folder = os.path.join(output_folder, image_name, 'seamed_examples')
            os.makedirs(intermediate_folder, exist_ok=True)
            filename = os.path.join(intermediate_folder, f'seam_{image_name}_{i}.png')
            mpimg.imsave(filename, image_with_seam)
            print(f'Saved: {filename}')

        # Remove the seam from the original image
        image = remove_seam(image, seam)

    # Normalize the pixel values of the final image to 0-1 range
    image = image / 255.0

    # Save the final result
    result_folder = os.path.join(output_folder, image_name)
    os.makedirs(result_folder, exist_ok=True)
    result_filename = os.path.join(result_folder, f'result_{image_name}_{removed_pixels}_pixels_removed.png')
    mpimg.imsave(result_filename, image)
    print(f'Final result saved: {result_filename}')

if __name__ == "__main__":
    main()