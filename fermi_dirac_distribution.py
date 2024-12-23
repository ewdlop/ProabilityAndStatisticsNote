import numpy as np
import matplotlib.pyplot as plt

# Constants
k_B = 8.617333262145e-5  # Boltzmann constant in eV/K

def fermi_dirac(E, T, E_F):
    """Calculate the Fermi-Dirac distribution.
    E : array-like
        Energy levels (eV)
    T : float
        Temperature (K)
    E_F : float
        Fermi energy (eV)
    """
    return 1 / (np.exp((E - E_F) / (k_B * T)) + 1)

# Energy levels (eV)
E = np.linspace(0, 1, 1000)

# Temperature (K)
T = 300

# Fermi energy (eV)
E_F = 0.5

# Calculate the Fermi-Dirac distribution
f_D = fermi_dirac(E, T, E_F)

# Plot the distribution
plt.plot(E, f_D, label=f'T={T}K, E_F={E_F}eV')
plt.xlabel('Energy (eV)')
plt.ylabel('Fermi-Dirac Distribution')
plt.title('Fermi-Dirac Distribution')
plt.legend()
plt.grid(True)
plt.show()
