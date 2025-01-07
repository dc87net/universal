% MATLAB/Octave script to compute quasi-zeroes and analyze the Riemann zeta function


% pkg install -forge symbolic
pkg load symbolic


% Step 1: Define constants
pi_val = pi;
log_2pi = log(2 * pi);

% Step 2: Define the function to compute the quasi-zeroes
t_n = @(n) ((pi_val / 4) + n * pi_val) / log_2pi;

% Step 3: Define the number of quasi-zeroes to compute
num_zeroes = 20;  % You can increase this to compute more quasi-zeroes
quasi_zeroes = zeros(num_zeroes, 1);

% Step 4: Generate the quasi-zeroes (t_n values)
for n = 0:(num_zeroes - 1)
    quasi_zeroes(n + 1) = t_n(n);
end

% Display the generated quasi-zeroes
disp('Quasi-zeroes (t_n values):');
disp(quasi_zeroes);

% Step 5: Define the Riemann zeta function in Octave/Matlab
% We will use the built-in zeta function in MATLAB/Octave
% Note: In Octave, zeta is implemented for real values of s.
% For complex s, we will use a numerical approach.
% Define a function for zeta for complex s

function z = zeta_complex(s)
    % Numerical approximation of the Riemann zeta function for complex s
    % Use the Euler-Maclaurin formula or built-in zeta for real part separately
    z = zeta(real(s)) + 1i * imag(zeta(real(s)));
end

% Step 6: Analyze the Riemann zeta function at the quasi-zeroes
s_values = -0.5 + 1i * quasi_zeroes;  % Complex values of s = pi + i * t_n
zeta_values = zeros(num_zeroes, 1);  % To store the zeta(s) values

for k = 1:num_zeroes
    zeta_values(k) = zeta_complex(s_values(k));  % Compute zeta at each s
end

% Step 7: Display the results
disp('Zeta values at the quasi-zeroes:');
for k = 1:num_zeroes
    fprintf('ζ(%f + i * %f) = %f + i * %f\n', real(s_values(k)), imag(s_values(k)), ...
            real(zeta_values(k)), imag(zeta_values(k)));
end

% Optional: Plot the real and imaginary parts of zeta(s) for these quasi-zeroes
figure;
subplot(2, 1, 1);
plot(quasi_zeroes, real(zeta_values), '-o');
xlabel('t_n');
ylabel('Re(ζ(s))');
title('Real part of ζ(s) at quasi-zeroes');

subplot(2, 1, 2);
plot(quasi_zeroes, imag(zeta_values), '-o');
xlabel('t_n');
ylabel('Im(ζ(s))');
title('Imaginary part of ζ(s) at quasi-zeroes');
