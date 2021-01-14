from Extra_File import get_primes_up_to

current_smallest_n = 0
current_smallest_n_phi = 100000000
primes = sorted(list(get_primes_up_to(5000000)))
for i, p_1 in enumerate(primes):
    idx = 0
    while True:
        if idx >= len(primes):
            break
        n = p_1 * primes[idx]
        if n >= 10000000:
            break
        phi = (p_1 - 1) * (primes[idx] - 1)
        n_phi = n / phi
        if ''.join(sorted(str(n))) == ''.join(sorted(str(int(phi)))) and n_phi < current_smallest_n_phi:
            current_smallest_n_phi = n_phi
            current_smallest_n = n
        idx += 1
print(f"N: {current_smallest_n}\tPhi: {current_smallest_n_phi}")
