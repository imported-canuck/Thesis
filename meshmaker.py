import numpy as np
from scipy.spatial import ConvexHull

def get_top_face_boundary(pts3d, triangles, cos_thresh=0.9):
    """
    Return an ordered boundary loop from only the top face triangles,
    by selecting triangles whose normals point mostly up (z > 0).
    Falls back to convex hull of all top‐face vertices if no manifold boundary.
    """
    # 1) Compute triangle normals
    v0 = pts3d[triangles[:,0]]
    v1 = pts3d[triangles[:,1]]
    v2 = pts3d[triangles[:,2]]
    normals = np.cross(v1 - v0, v2 - v0)
    norms = np.linalg.norm(normals, axis=1)
    # avoid division by zero
    valid = norms > 1e-8
    nz = np.zeros_like(norms)
    nz[valid] = normals[valid,2] / norms[valid]

    # 2) Keep only triangles whose normal.z is > cos_thresh (i.e. < acos threshold)
    top_tris = triangles[(nz > cos_thresh)]

    # 3) Attempt manifold boundary on that subset
    def extract_loop(tris):
        edge_count = {}
        for tri in tris:
            for i,j in ((0,1),(1,2),(2,0)):
                e = tuple(sorted((int(tri[i]), int(tri[j]))))
                edge_count[e] = edge_count.get(e,0) + 1
        boundary = [e for e,c in edge_count.items() if c == 1]
        if not boundary:
            raise ValueError
        adj = {}
        for u,v in boundary:
            adj.setdefault(u,[]).append(v)
            adj.setdefault(v,[]).append(u)
        start = boundary[0][0]
        loop, prev, curr = [start], None, start
        while True:
            nbr = adj[curr]
            nxt = nbr[0] if nbr[0] != prev else nbr[1]
            if nxt == start: break
            loop.append(nxt)
            prev, curr = curr, nxt
        return loop

    try:
        return extract_loop(top_tris)
    except ValueError:
        # fallback to convex hull of all top‐face verts
        verts2d = pts3d[:,:2]  # projection
        idxs = np.unique(top_tris.ravel())
        hull = ConvexHull(verts2d[idxs])
        return idxs[hull.vertices].tolist()
