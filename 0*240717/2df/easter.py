%High - precision
Riemann
zeta
function
evaluation
using
Euler - Maclaurin

%Step
1: Define
constants
pi_val = pi;

%Step
2: Define
the
quasi - zero
formula
for t_n
    t_n =


    @(n)(pi_val / 4 + n * pi_val) / log(2 * pi_val)

    ;

    %Step
    3: Compute
    quasi - zeroes(t_n
    values)
    num_zeroes = 10; %You
    can
    increase
    this
    for more zeroes
        quasi_zeroes = zeros(num_zeroes, 1);

    for n = 0:(num_zeroes - 1)
    quasi_zeroes(n + 1) = t_n(n);
    end

    disp('Quasi-zeroes (t_n values):');
    disp(quasi_zeroes);

    %Step
    4: Define
    the
    function
    for manually computing the zeta function using the functional equation
    function
    zeta_val = zeta_manual(s)
    %Functional
    equation: ζ(s) = 2 ^ s * π ^ (s - 1) * sin(πs / 2) * Γ(1 - s) * ζ(1 - s)
    two_pow_s = 2 ^ s;
    pi_pow_s_minus_1 = pi ^ (s - 1);
    sin_pi_s_over_2 = sin(pi * s / 2);
    gamma_1_minus_s = gamma(1 - s);

    %Use
    the
    Euler - Maclaurin
    formula
    to
    compute
    ζ(1 - s)
    zeta_1_minus_s = zeta_euler_maclaurin(1 - s, 10000); %More
    precise
    approximation

    %Combine
    the
    terms
    to
    get
    zeta(s)
    zeta_val = two_pow_s * pi_pow_s_minus_1 * sin_pi_s_over_2 * gamma_1_minus_s * zeta_1_minus_s;
    end

    %Step
    5: Implement
    the
    Euler - Maclaurin
    summation
    for zeta(s)
        function
        z = zeta_euler_maclaurin(s, N)
    %High - precision
    approximation
    using
    Euler - Maclaurin
    summation
    B = [1 / 6, -1 / 30, 1 / 42, -1 / 30, 5 / 66]; %Bernoulli
    numbers
    B_2, B_4, B_6, B_8, B_10
    z = 0;

    %Summation
    part
    for n = 1:N - 1
    z = z + 1 / n ^ s;
    end

    %Euler - Maclaurin
    corrections
    z = z + (N ^ (1 - s) / (s - 1)) + (N ^ (-s) / 2);

    %Add
    the
    Bernoulli
    term
    corrections
    for k = 1:length(B)
    z = z + (B(k) / factorial(2 * k)) * prod(s:(s + 2 * k - 1)) *N ^ (-s - 2 * k + 1);
    end
    end

    %Step
    6: Evaluate
    the
    zeta
    function
    at
    the
    quasi - zeroes(s=-0.5 + it_n)
    s_values = -0.5 + 1
    i * quasi_zeroes; %Complex
    values
    of
    s = -1 / 2 + i * t_n
    zeta_values = zeros(num_zeroes, 1); %To
    store
    zeta(s)
    values

    for k = 1:num_zeroes
    zeta_values(k) = zeta_manual(s_values(k)); %Compute
    zeta
    using
    the
    manual
    approach
    end

    %Step
    7: Display
    the
    results
    disp('Zeta values at the quasi-zeroes:');
    for k = 1:num_zeroes
    fprintf('ζ(%f + i * %f) = %f + i * %f\n', real(s_values(k)), imag(s_values(k)), ...
    real(zeta_values(k)), imag(zeta_values(k)));
    end

    % Optional: Plot
    the
    real and imaginary
    parts
    of
    ζ(s)
    at
    these
    quasi - zeroes
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
