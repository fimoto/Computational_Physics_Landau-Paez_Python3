""" From "COMPUTATIONAL PHYSICS", 3rd Ed, Enlarged Python eTextBook  
    by RH Landau, MJ Paez, and CC Bordeianu
    Copyright Wiley-VCH Verlag GmbH & Co. KGaA, Berlin;  Copyright R Landau,
    Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2015.
    Support by National Science Foundation"""

# List 17.4 QMCbouncer.py: Modified version by F.I. based on the previous Fortran code

import numpy as np
import matplotlib.pyplot as plt
import random

def energy(array, dt, g):
    return np.sum(0.5 * ((array[1:] - array[:-1]) / dt)**2 + g * (array[1:] + array[:-1]) / 2)

def qmc_bouncer_simulation(max_iter=1_000_000, path_len=100, dt=0.05, g=2.0, output_file="qmcbouncer.dat"):
    path = np.zeros(path_len+1)
    prob = np.zeros(2*path_len+1, dtype=int)
    oldE = energy(path, dt, g)
    maxel = 1

    for _ in range(max_iter):
        element = int(path_len*random.random())

        if element != 0 and element != path_len:
            change = (np.random.rand() - 0.5) * 2.0
            if path[element] + change > 0:
                path[element] += change
                newE = energy(path, dt, g)

                if newE > oldE and np.exp(-(newE - oldE)) < np.random.rand():
                    path[element] -= change

                ele = int(path[element] * 1250 / 100)
                if ele >= maxel:
                    maxel = ele
                if element != 0:
                    prob[ele] += 1
                oldE = newE

    with open(output_file, "w") as f:
        for j in range(100):
            f.write(f"{j+1} {prob[j]/max_iter:.6f}\n")

    print(f"Data saved in {output_file}")

def plot_qmcbouncer(file="qmcbouncer.dat"):
    data = np.loadtxt(file)
    x, y = data[:, 0], data[:, 1]

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, marker='o', linestyle='-', label='Probability')
    plt.title("QMC Bouncer Distribution")
    plt.xlabel("Index (position)")
    plt.ylabel("Unnormalized Probability")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    qmc_bouncer_simulation()
    plot_qmcbouncer()
