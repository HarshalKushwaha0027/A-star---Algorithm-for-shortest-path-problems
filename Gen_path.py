import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# Example matrix (Modify for your data)

def gen_path(grid,path):

    matrix = np.array(grid)

    # Create a color matrix (default white)
    color_matrix = np.full(matrix.shape, np.nan)

    # Assign specific indices for the highlighted values
    # Highlight the path
    for idx, (r, c) in enumerate(path):
        if idx == 0:

            color_matrix[r, c] = 1  # First element in Red

        elif idx == len(path) - 1:

            color_matrix[r, c] = 3  # Last element in Green

        else:

            color_matrix[r, c] = 2  # Path in Blue

    # Set 0 entries to Grey
    color_matrix[matrix == 0] = 4
    # Define custom colormap

    cmap = mcolors.ListedColormap(['red', 'blue', 'green','grey'])

    # Create figure
    fig, ax = plt.subplots()
    ax.imshow(color_matrix, cmap=cmap, interpolation='nearest')

    # Overlay numbers on the image
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            ax.text(j, i, str(matrix[i, j]), ha='center', va='center', color='black', fontsize=12, fontweight='bold')

    # Remove axes
    ax.set_xticks([])
    ax.set_yticks([])

    # Save and show the image
    plt.savefig("highlighted_matrix.png", bbox_inches='tight', pad_inches=0)
    plt.show()
