def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def gap(g, m, n):
    prev_prime = None
    for num in range(m, n + 1):
        if is_prime(num):
            if prev_prime is not None and num - prev_prime == g:
                return [prev_prime, num]
            prev_prime = num
    return None
