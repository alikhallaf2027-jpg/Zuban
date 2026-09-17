# ZUBAN - N = n! + 10^k + m
# Creator: Tariq Al-Habib - Law: RG-311226
# If you hold the number, you hold the world

import math

def zuban_number(n, k, m):
    """Calculate Zuban Number: N = n! + 10^k + m"""
    return math.factorial(n) + (10**k) + m

def decode_world(n, k, m):
    N = zuban_number(n, k, m)
    print(f"Stone: {n}! = {math.factorial(n)}")
    print(f"Papyrus: 10^{k} = {10**k}")
    print(f"Cartouche: {m}")
    print(f"Full Database N = {N}")
    return N

if __name__ == "__main__":
    decode_world(5, 3, 7)
