import numpy as np
import matplotlib.pyplot as plt
from mpmath import cos, sin, log, nsum, inf


def compute_zeta_parts(sigma, t_values, n_max=1000):
    real_parts = []
    imaginary_parts = []

    for t in t_values:
        sum_real = nsum(lambda n: n ** (-sigma) * cos(t * log(n)), [1, inf], maxterms=n_max)
        sum_imag = nsum(lambda n: -n ** (-sigma) * sin(t * log(n)), [1, inf], maxterms=n_max)

        real_parts.append(sum_real)
        imaginary_parts.append(sum_imag)

    return np.array(real_parts, dtype=float), np.array(imaginary_parts, dtype=float)


def detect_zeros(real_parts, imaginary_parts, t_values):
    zero_indices = []
    for i in range(1, len(t_values)):
        print(f"Zero search at {i} ...",end='\r')
        if (np.sign(real_parts[i - 1]) != np.sign(real_parts[i])) and (
                np.sign(imaginary_parts[i - 1]) != np.sign(imaginary_parts[i])):
            zero_indices.append(i); print(f"\n✅ ZERO at ==> {i}")
    return zero_indices


def plot_zeta_parts(t_values, real_parts, imaginary_parts, sigma, zero_indices):
    plt.figure(figsize=(12, 6))
    plt.plot(t_values, real_parts, label='Real Part')
    plt.plot(t_values, imaginary_parts, label='Imaginary Part')
    plt.scatter(t_values[zero_indices], [0] * len(zero_indices), color='red', label='Zeros')
    plt.xlabel('Theta (t)')
    plt.ylabel('Amplitude')
    plt.title(f'Real and Imaginary Parts of Zeta Function for Sigma = {sigma}')
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    sigma_values = [0.5, 0.6]
    t_values = np.linspace(0, 40, 1000)

    for sigma in sigma_values:
        print(f"Calculating for σ = {sigma}")
        real_parts, imaginary_parts = compute_zeta_parts(sigma, t_values, n_max=1000)
        zero_indices = detect_zeros(real_parts, imaginary_parts, t_values)

        # print(f"Sigma = {sigma}")
        for idx in zero_indices:
            print(f"Zero found at t = {t_values[idx]:.5f}")

        print(f"Drawing plot for σ = {sigma}")
        plot_zeta_parts(t_values, real_parts, imaginary_parts, sigma, zero_indices)


if __name__ == "__main__":
    main()