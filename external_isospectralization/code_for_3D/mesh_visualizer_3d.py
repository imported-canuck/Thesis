import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import but required for 3D projection

# Load mesh files
V = np.loadtxt("mesh.vert")                # expects lines: X Y Z
T = np.loadtxt("mesh.triv", dtype=int) - 1 # expects 1-based indices

# Separate coordinates
X, Y, Z = V.T

# Create figure and 3D axes
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot the triangular surface
ax.plot_trisurf(X, Y, Z, triangles=T, linewidth=0.2, antialiased=True, color='lightgray', edgecolor='k', alpha=0.8)

# Overlay the mesh vertices
ax.scatter(X, Y, Z, s=8, color='red')

# Function to set equal aspect ratio on 3D axes
def set_axes_equal(ax):
    x_limits = ax.get_xlim3d()
    y_limits = ax.get_ylim3d()
    z_limits = ax.get_zlim3d()
    x_range = abs(x_limits[1] - x_limits[0])
    x_middle = np.mean(x_limits)
    y_range = abs(y_limits[1] - y_limits[0])
    y_middle = np.mean(y_limits)
    z_range = abs(z_limits[1] - z_limits[0])
    z_middle = np.mean(z_limits)
    plot_radius = 0.5 * max(x_range, y_range, z_range)
    ax.set_xlim3d(x_middle - plot_radius, x_middle + plot_radius)
    ax.set_ylim3d(y_middle - plot_radius, y_middle + plot_radius)
    ax.set_zlim3d(z_middle - plot_radius, z_middle + plot_radius)

set_axes_equal(ax)

# Labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title("3D Mesh Visualization")
plt.tight_layout()
plt.show()
