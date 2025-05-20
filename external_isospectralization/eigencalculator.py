#!/usr/bin/env python3
"""
compute_evals_tf.py

Loads mesh.vert / mesh.triv, uses the original TF-based
calc_evals(...) to compute the first K eigenvalues, and
saves them to evals.txt.
"""

import numpy as np
from shape_library import load_mesh
from spectrum_alignment import calc_evals as calc_eigs  # collision prevention
import os

# --------------------- settings ---------------------
VERT_FILE = "mesh.vert"
TRIV_FILE = "mesh.triv"
K         = 1000
OUT_FILE  = "evals.txt"
# ----------------------------------------------------

def compute_first_k(V, T, k):
    # The original calc_evals returns all eigenvalues; just slice first k
    ev = calc_eigs(V, T)
    return ev[:min(k, len(ev))]

def main():
    # Load data
    V = np.loadtxt(VERT_FILE)
    T = np.loadtxt(TRIV_FILE, dtype=int) - 1

    print(f"Computing first {K} eigenvalues via TF routine…")
    evals = compute_first_k(V, T, K)

    np.savetxt(OUT_FILE, evals, fmt="%.10g")
    print(f"Saved {len(evals)} eigenvalues to {OUT_FILE}")

if __name__ == "__main__":
    main()
