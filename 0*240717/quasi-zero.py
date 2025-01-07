import mpmath as mp
import matplotlib.pyplot as plt
import numpy as np

# -------------------------------
# 1. Configuration and Parameters
# -------------------------------

# Set high precision (e.g., 100 decimal places)
mp.dps = 100

# Define the range of n for quasi-zeroes
n_min = 1
n_max = 100  # Adjust as needed for more quasi-zeroes


# Formula for t_n: t_n = (pi/4 + n*pi) / ln(2*pi)
def compute_t_n(n):
    return (mp.pi / 4 + n * mp.pi) / mp.log(2 * mp.pi)


# -------------------------------
# 2. Generate Quasi-Zeroes Using Provided Formula
# -------------------------------

def generate_quasi_zeroes(n_min, n_max):
    """
    Generates quasi-zeroes on Re(s) = -0.5 using the formula:
    t_n = (pi/4 + n*pi) / ln(2*pi)

    Parameters:
        n_min (int): Starting value of n
        n_max (int): Ending value of n

    Returns:
        list of mpmath.mpc: List of quasi-zeroes s_n = -0.5 + i t_n
    """
    quasi_zeroes = []
    for n in range(n_min, n_max + 1):
        t_n = compute_t_n(n)
        s_n = mp.mpc(-0.5, t_n)
        quasi_zeroes.append(s_n)
    return quasi_zeroes


# Generate quasi-zeroes
quasi_zeroes_all = generate_quasi_zeroes(n_min, n_max)

# -------------------------------
# 3. Define Actual Non-Trivial Zeros on the Critical Line
# -------------------------------

# For demonstration, we'll use the first few known non-trivial zeros on the critical line.
# In practice, you can extend this list with more zeros as needed.

actual_zero_t_values = [
    14.1347251417346937904572519835624702707842571156992431,
    21.022039638771554992628479593896902777334340524266243,
    25.0108575801456887632137909925628218186595496725571323,
    30.424876125859513210311897530583323900910497583472521,
    32.935061587739189690662368964074063303508982438199559,
    37.586178158825671257217763480705708411764095546094149,
    40.918719012147495187398126914633644208549311694603186,
    43.327073280914999519496122165406982380714833525287849,
    48.005150881167159727942472749427661034217658871681275,
    49.773832477672302181916784678563226050381343220158316
]

# Convert actual zeros to mpmath complex numbers on the critical line
actual_zeros = [mp.mpc(0.5, t) for t in actual_zero_t_values]


# -------------------------------
# 4. Substitute Actual Zeros with Quasi-Zeroes
# -------------------------------

def substitute_zeros(actual_zeros, quasi_zeroes):
    """
    Substitutes actual zeros with quasi-zeroes.

    Parameters:
        actual_zeros (list of mpmath.mpc): List of actual non-trivial zeros
        quasi_zeroes (list of mpmath.mpc): List of quasi-zeroes

    Returns:
        list of mpmath.mpc: Substituted list of zeros
    """
    substituted_zeros = []
    for actual_zero, quasi_zero in zip(actual_zeros, quasi_zeroes):
        substituted_zeros.append(quasi_zero)
    return substituted_zeros


# Ensure there are enough quasi-zeroes to substitute
if len(quasi_zeroes_all) < len(actual_zeros):
    raise ValueError("Not enough quasi-zeroes to substitute for actual zeros.")

# Perform substitution
substituted_zeros = substitute_zeros(actual_zeros, quasi_zeroes_all[:len(actual_zeros)])

print(f"Number of actual zeros: {len(actual_zeros)}")
print(f"Number of quasi-zeroes available for substitution: {len(quasi_zeroes_all)}")
print(f"Number of quasi-zeroes used for substitution: {len(substituted_zeros)}")


# -------------------------------
# 5. Define the Explicit Formula for ψ(x)
# -------------------------------

def psi_explicit(x, zeros):
    """
    Computes the explicit formula for ψ(x) using a list of zeros.

    ψ(x) = x - ∑ (x^rho / rho)

    Parameters:
        x (float): The value at which to evaluate ψ(x).
        zeros (list of mpmath.mpc): List of zeros (actual or substituted quasi-zeroes).

    Returns:
        mpf: The computed value of ψ(x).
    """
    psi = mp.mpf(x)
    for rho in zeros:
        # To prevent overflow, especially with large t, limit x^rho
        # Alternatively, use logarithmic computations if necessary
        try:
            term = mp.power(x, rho) / rho
            psi -= term
        except OverflowError:
            # Handle potential overflow by skipping the term
            pass
    return psi


# -------------------------------
# 6. Compute ψ(x) with Actual Zeros and with Substituted Quasi-Zeroes
# -------------------------------

# Define a range of x values to evaluate ψ(x)
x_min = 10
x_max = 1000
num_points = 500
x_values = np.linspace(x_min, x_max, num_points)

# Initialize lists to store ψ(x) values
psi_actual = []
psi_substituted = []

# Compute ψ(x) using actual zeros
print("Computing ψ(x) using actual zeros...")
for x in x_values:
    psi = psi_explicit(x, actual_zeros)
    psi_actual.append(mp.nstr(psi, 15))  # Convert to string for consistency

# Compute ψ(x) using substituted quasi-zeroes
print("Computing ψ(x) using substituted quasi-zeroes...")
for x in x_values:
    psi = psi_explicit(x, substituted_zeros)
    psi_substituted.append(mp.nstr(psi, 15))

# -------------------------------
# 7. Plotting the Results
# -------------------------------

# Convert ψ(x) lists to floats for plotting
# Since ψ(x) is a real-valued function, we take the real part
psi_actual_real = [float(mp.re(mp.mpf(val))) for val in psi_actual]
psi_substituted_real = [float(mp.re(mp.mpf(val))) for val in psi_substituted]

# Plot ψ(x) with actual zeros vs. substituted quasi-zeroes
plt.figure(figsize=(14, 7))
plt.plot(x_values, psi_actual_real, label='ψ(x) with Actual Zeros', color='blue')
plt.plot(x_values, psi_substituted_real, label='ψ(x) with Substituted Quasi-Zeroes', color='red', alpha=0.7)
plt.xlabel('x')
plt.ylabel('ψ(x)')
plt.title('Impact of Substituting Actual Zeros with Quasi-Zeroes in ψ(x)')
plt.legend()
plt.grid(True)
plt.show()

# -------------------------------
# 8. Plotting the Difference
# -------------------------------

# Compute the absolute difference between the two ψ(x) computations
psi_difference = [abs(a - b) for a, b in zip(psi_actual_real, psi_substituted_real)]

plt.figure(figsize=(14, 7))
plt.plot(x_values, psi_difference, label='|ψ(x) with Actual Zeros - ψ(x) with Quasi-Zeroes|', color='green')
plt.xlabel('x')
plt.ylabel('Difference in ψ(x)')
plt.title('Difference in ψ(x) Due to Substitution of Quasi-Zeroes')
plt.legend()
plt.grid(True)
plt.show()

# -------------------------------
# 9. Analysis and Interpretation
# -------------------------------

print("Analysis Complete. Please review the plots to observe any divergence or lack thereof.")
