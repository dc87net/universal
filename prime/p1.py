import cmath
import math
import plotly.graph_objects as go


def generate_and_visualize_primes(limit, iterations):
    z = 1 + 0j  # Initial seed value
    primes = set()

    for _ in range(iterations):
        # Apply the first transformation
        z = cmath.exp(cmath.pi * z * 1j)
        real_part = z.real

        if real_part <= limit and real_part > 1:
            candidate = int(real_part)
            if candidate > 1 and all(candidate % i != 0 for i in range(2, int(math.sqrt(candidate)) + 1)):
                primes.add(candidate)

        # Apply the second transformation
        z = cmath.cos(z) + 1j * cmath.sin(z)
        real_part = z.real

        if real_part <= limit and real_part > 1:
            candidate = int(real_part)
            if candidate > 1 and all(candidate % i != 0 for i in range(2, int(math.sqrt(candidate)) + 1)):
                primes.add(candidate)

    primes = sorted(primes)

    # Plotly visualization
    fig = go.Figure(data=go.Scatter(x=primes, y=[0] * len(primes), mode='markers'))
    fig.update_layout(
        title='Prime Distribution in Higher-Dimensional Space',
        xaxis_title='Prime Numbers',
        yaxis_title='Imaginary Part (Not Used)',
        yaxis=dict(showticklabels=False)  # Hide y-axis labels since they are not used
    )
    fig.show()

    return primes


# Example usage
limit = 100
iterations = 1000
primes = generate_and_visualize_primes(limit, iterations)
print(f"Generated primes: {primes}")