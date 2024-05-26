def modular_exponentiation(base, exponent, mod):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exponent //= 2
    return result


def geometric_series_sum(a, x, m):
    """Compute (a^0 + a^1 + ... + a^(x-1)) % m"""
    if x == 0:
        return 0
    elif x == 1:
        return 1 % m
    if a % m == 1:  # When A=1, we simply return X % M since 1^i = 1
        return x % m
    a_mod = a % m
    # (1 - a^x) / (1 - a) is the sum of GP
    # We use the modular inverse of (1-a) to calculate it modulo m
    ae_mod_x = modular_exponentiation(a_mod, x, m)
    numerator = (ae_mod_x - 1 + m) % m
    a_minus_1 = (a_mod - 1 + m) % m

    # Compute modular inverse of a_minus_1 modulo m
    inv_a_minus_1 = pow(a_minus_1, m - 2, m)

    result = (numerator * inv_a_minus_1) % m
    return result


import sys

input = sys.stdin.read


def main():
    data = input().strip()
    a, x, m = map(int, data.split())
    result = geometric_series_sum(a, x, m)
    print(result)


if __name__ == "__main__":
    main()
