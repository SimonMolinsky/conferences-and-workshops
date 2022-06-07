import numpy as np
import matplotlib.pyplot as plt

def show_band(band, color_map='gray', remove_negative=True):
    matrix = band.astype(float)
    if remove_negative:
        matrix[matrix <= 0] = np.nan
    fig = plt.figure(figsize=(11,11))
    image_layer = plt.imshow(matrix)
    image_layer.set_cmap(color_map)
    plt.colorbar()
    plt.show()
    
if __name__ == '__main__':
    test_band = np.random.randint(low=0, high=255, size=(200, 200))
    show_band(test_band)