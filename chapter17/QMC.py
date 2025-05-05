""" From "COMPUTATIONAL PHYSICS", 3rd Ed, Enlarged Python eTextBook  
    by RH Landau, MJ Paez, and CC Bordeianu
    Copyright Wiley-VCH Verlag GmbH & Co. KGaA, Berlin;  Copyright R Landau,
    Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2015.
    Support by National Science Foundation"""

# List 17.3 QMC.py: Modified version by F.I. based on the previous Fortran code

import numpy as np
import matplotlib.pyplot as plt

def energy(array):
    return np.sum((array[1:] - array[:-1])**2 + array[:-1]**2)

def qmc_simulation(max_iter=250000, path_len=100, 
                   prob_file="qmc_prob.dat", path_file="qmc_path.dat"):
    path = np.zeros(path_len)
    prob = np.zeros(100, dtype=int)
    oldE = energy(path)

    for _ in range(max_iter):
        element = np.random.randint(0, path_len)
        change = (np.random.rand() - 0.5) * 2.0
        path[element] += change
        newE = energy(path)

        if newE > oldE and np.exp(-(newE - oldE)) < np.random.rand():
            path[element] -= change
        else:
            oldE = newE

        for j in range(path_len):
            idx = int(path[j] * 10 + 50)
            if 0 <= idx < 100:
                prob[idx] += 1

    with open(prob_file, "w") as f_prob, open(path_file, "w") as f_path:
        for j in range(100):
            f_prob.write(f"{j - 50} {prob[j] / max_iter:.6f}\n")
            f_path.write(f"{j + 1} {path[j]:.6f}\n")

    print(f"Data saved in {prob_file} & {path_file}")

def plot_results(prob_file="qmc_prob.dat", path_file="qmc_path.dat"):
    # qmc_prob.dat
    data_prob = np.loadtxt(prob_file)
    x_prob, y_prob = data_prob[:, 0], data_prob[:, 1]
    plt.figure()
    plt.plot(x_prob, y_prob, marker='x', linestyle='-', label='Probability')
    plt.title("Probability")
    plt.xlabel("Position")
    plt.ylabel("Probability (unnormalized)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    # qmc_path.dat
    data_path = np.loadtxt(path_file)
    x_path, y_path = data_path[:, 0], data_path[:, 1]
    plt.figure()
    plt.plot(x_path, y_path, marker='x', linestyle='-', label='Path')
    plt.title("Path")
    plt.xlabel("Time")
    plt.ylabel("Position")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    plt.show()

if __name__ == "__main__":
    qmc_simulation()
    plot_results()
