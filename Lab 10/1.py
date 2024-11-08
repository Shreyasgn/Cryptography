1. Write a Python script to list all the prime numbers from 1 to 100 using Sieve of Eratosthenes.

def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    
    for p in range(2, int(limit**0.5) + 1):
        if primes[p]:
            for multiple in range(p * p, limit + 1, p):
                primes[multiple] = False

    prime_numbers = [p for p, is_prime in enumerate(primes) if is_prime]
    return prime_numbers

# List all prime numbers from 1 to 100
prime_numbers = sieve_of_eratosthenes(100)
print("Prime numbers from 1 to 100:", prime_numbers)
