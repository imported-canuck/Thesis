import numpy as np
import matplotlib.pyplot as plt
import os

# Build absolute UNC paths
base = r"\\campus\emf\Mech2\carsla\My Documents\Downloads\TestingMesh"
vert_fp = os.path.join(base, "mesh.vert")
triv_fp = os.path.join(base, "mesh.triv")

verts = np.loadtxt(vert_fp)
tris  = np.loadtxt(triv_fp, dtype=int) - 1

# Plot the triangulation
fig, ax = plt.subplots()
ax.triplot(verts[:, 0], verts[:, 1], tris, linewidth=0.5)
ax.scatter(verts[:, 0], verts[:, 1], s=5)
ax.set_aspect('equal')
ax.set_title('Mesh Preview: Triangles and Vertices')
plt.show()