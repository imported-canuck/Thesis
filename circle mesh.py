import numpy as np
from scipy.spatial import Delaunay

# 1) scatter interior points
r     = np.sqrt(np.random.rand(600)) 
theta = 2*np.pi*np.random.rand(600)
pts   = np.stack((r*np.cos(theta), r*np.sin(theta)), axis=1)

# 2) add boundary points
perim = np.stack((
    np.cos(np.linspace(0, 2*np.pi, 200, endpoint=False)),
    np.sin(np.linspace(0, 2*np.pi, 200, endpoint=False))
), axis=1)
pts   = np.vstack((pts, perim))    # (800,2)

# 3) Delaunay triangulation
tri   = Delaunay(pts)
tris  = tri.simplices              # (M,3), 0-based

# 4) lift to 3D (z=0)
pts3d = np.hstack((pts, np.zeros((pts.shape[0], 1))))  # (800,3)

# 5) save mesh.vert and mesh.triv
np.savetxt("mesh.vert", pts3d, fmt="%.6f")
np.savetxt("mesh.triv", tris + 1, fmt="%d")  # convert to 1-based indexing

# 6) write circle.obj for visualization
with open("circle.obj", "w") as f:
    # write vertices
    for x, y, z in pts3d:
        f.write(f"v {x:.6f} {y:.6f} {z:.6f}\n")
    # write faces (1-based)
    for a, b, c in tris + 1:
        f.write(f"f {a} {b} {c}\n")

print("Done")