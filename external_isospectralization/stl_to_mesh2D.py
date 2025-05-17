import numpy as np
import meshio

# 1) Read STL
m = meshio.read(r"\\campus\emf\Mech2\carsla\My Documents\Downloads\circle.stl")
pts3d = m.points                 # shape (N,3)
tris   = m.cells_dict["triangle"]  # shape (M,3), 0-based

# 2) Prepare mesh.vert with three columns (x, y, z)
#    If STL happens to have some non-zero z (because of extrusion),
#    flatten it by overriding z to zero:
verts3d = np.zeros_like(pts3d)
verts3d[:, 0:2] = pts3d[:, 0:2]
# verts3d[:, 2] is already zero

# 3) Save mesh.vert and mesh.triv
np.savetxt("mesh.vert", verts3d, fmt="%.6f")    # now has 3 columns
np.savetxt("mesh.triv", tris + 1,    fmt="%d")  # 1-based indexing

# 4) Write mesh.obj for visualization
with open("circle.obj","w") as f:
    for x,y,z in verts3d:
        f.write(f"v {x} {y} {z}\n")
    for a,b,c in tris+1:
        f.write(f"f {a} {b} {c}\n")

print(f"Exported mesh.vert ({len(verts3d)} verts), mesh.triv ({len(tris)} tris), and circle.obj")
