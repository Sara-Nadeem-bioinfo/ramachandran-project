import numpy as np
import matplotlib.pyplot as plt

# ---- DEFINE GRID ----
phi = np.linspace(-180, 180, 100)
psi = np.linspace(-180, 180, 100)

phi_grid, psi_grid = np.meshgrid(phi, psi)

# ---- FAKE BUT REALISTIC ENERGY FUNCTION ----
# (Mimics alanine dipeptide landscape)

energy = (
    np.exp(-((phi_grid + 60)**2 + (psi_grid + 40)**2)/2000) +   # alpha region
    np.exp(-((phi_grid + 120)**2 + (psi_grid - 120)**2)/2000)   # beta region
)

# Convert to energy-like
energy = -np.log(energy + 1e-6)

# ---- PLOT ----
plt.figure(figsize=(6,6))

plt.contourf(phi, psi, energy, levels=30, cmap='viridis')
plt.colorbar(label="Energy (a.u.)")

plt.xlabel("Phi (°)")
plt.ylabel("Psi (°)")
plt.title("Ramachandran Plot (Alanine Dipeptide)")

plt.xlim(-180,180)
plt.ylim(-180,180)

plt.grid()
plt.show()
