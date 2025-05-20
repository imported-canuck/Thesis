import os
import numpy as np
import trimesh
import pymeshlab
import tkinter as tk
from tkinter import filedialog, simpledialog

"""
meshmaker3d_pymeshlab.py

Reads a 3D STL/OBJ surface mesh, decimates it to a target
vertex count using PyMeshLab (no Open3D needed), and writes:
  - mesh.vert   (X Y Z per line)
  - mesh.triv   (i j k per line, 1-based)
  - <name>.obj  (re-exported)
"""

def pick_file():
    root = tk.Tk(); root.withdraw()
    path = filedialog.askopenfilename(
        title="Select a 3D STL/OBJ mesh",
        filetypes=[("Mesh files","*.stl *.obj")])
    if not path:
        raise SystemExit("No file selected.")
    return path

def write_outputs(base, verts, faces):
    # mesh.vert
    with open("mesh.vert","w") as fv:
        for x, y, z in verts:
            fv.write(f"{x:.6f} {y:.6f} {z:.6f}\n")
    # mesh.triv (1-based)
    with open("mesh.triv","w") as ft:
        for tri in faces:
            a, b, c = tri + 1
            ft.write(f"{a} {b} {c}\n")
    # write OBJ
    with open(f"{base}.obj","w") as fo:
        for x, y, z in verts:
            fo.write(f"v {x:.6f} {y:.6f} {z:.6f}\n")
        for tri in faces:
            a, b, c = tri + 1
            fo.write(f"f {a} {b} {c}\n")

def main():
    path = pick_file()
    base = os.path.splitext(os.path.basename(path))[0]

    print(f"Loading mesh from {path}…")
    mesh = trimesh.load(path, process=False)
    orig_v = mesh.vertices.shape[0]
    orig_f = mesh.faces.shape[0]
    print(f"  original: {orig_v} vertices, {orig_f} faces")

    # Prompt for target vertices
    root = tk.Tk(); root.withdraw()
    nverts = simpledialog.askinteger(
        "Vertices",
        "Target # of vertices:",
        initialvalue=1000,
        minvalue=4,
        maxvalue=orig_v
    )
    if nverts is None:
        raise SystemExit("No vertex count provided.")

    # Compute decimation percentage
    perc = float(nverts) / orig_v
    print(f"Decimating to ~{nverts} vertices (~{perc*100:.1f}% of original)...")

    ms = pymeshlab.MeshSet()
    ms.load_new_mesh(path)
    # Use targetperc to specify desired fraction of vertices
    ms.simplification_quadric_edge_collapse_decimation(targetperc=perc)
    m_out = ms.current_mesh()
    verts = m_out.vertex_matrix()
    faces = m_out.face_matrix()
    print(f"  result: {verts.shape[0]} vertices, {faces.shape[0]} faces")

    print("Writing mesh.vert, mesh.triv, and", f"{base}.obj")
    write_outputs(base, verts, faces)
    print("Done.")

if __name__ == "__main__":
    main()
