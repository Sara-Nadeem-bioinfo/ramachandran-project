"""
Ramachandran Plot using MDTraj + OpenMM
REAL phi-psi calculation
"""

import mdtraj as md
import matplotlib.pyplot as plt
import numpy as np
import urllib.request

# 🔹 Download a valid protein structure
url = "https://files.rcsb.org/download/1CRN.pdb"
urllib.request.urlretrieve(url, "protein.pdb")

# 🔹 Load trajectory
traj = md.load("protein.pdb")

# 🔹 Compute phi and psi
phi = md.compute_phi(traj)
psi = md.compute_psi(traj)

phi_angles = phi[1]
psi_angles = psi[1]

# Convert to degrees
phi_deg = np.degrees(phi_angles)
psi_deg = np.degrees(psi_angles)

# 🔹 Plot Ramachandran
import mdtraj as md
import numpy as np
import matplotlib.pyplot as plt

# Load structure
traj = md.load("ala.pdb")

# Compute angles
import mdtraj as md
import numpy as np
import matplotlib.pyplot as plt

traj = md.load("ala.pdb")

# 👉 Just pick 4 connected atoms (trial working set)
phi = md.compute_dihedrals(traj, [[1, 5, 6, 7]])
psi = md.compute_dihedrals(traj, [[5, 6, 7, 11]])

phi = np.degrees(phi).flatten()
psi = np.degrees(psi).flatten()

print(phi, psi)

# Convert to degrees
phi = np.degrees(phi).flatten()
psi = np.degrees(psi).flatten()

# ---- ENERGY APPROXIMATION (DENSITY) ----
heatmap, xedges, yedges = np.histogram2d(phi, psi, bins=50)

# Convert density to pseudo-energy
energy = -np.log(heatmap + 1)   # +1 avoids log(0)

# ---- PLOT ----
plt.figure(figsize=(6,6))

plt.contourf(
    xedges[:-1],
    yedges[:-1],
    energy.T,
    levels=20,
    cmap='viridis'
)

plt.colorbar(label="Energy (a.u.)")

# Labels
plt.xlabel("Phi (°)")
plt.ylabel("Psi (°)")
plt.title("Energy Contour Ramachandran Plot")
plt.scatter(phi, psi, c='white', s=5, alpha=0.3)
plt.xlim(-180, 180)
plt.ylim(-180, 180)

plt.grid()
plt.show()