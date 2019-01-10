message = 322

# Choose two random prime numbers
p = 17
q = 19

N = p*q

# Calculation of phi(N)
phi_n = (p-1)*(q-1)

# e is chosen such that 1<e<phi(N) and e and phi(N) don't have common factors
e = 5

# Public keys are (e, N)

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

# Calculation of private key: d
d = modinv(e, phi_n)

# Encryption part
cipher_text = (message**e) % N

print("Cipher text:", int(str(cipher_text)))

# Decryption part
decrypted_text = (cipher_text**d) % N

print("Decrypted text:", int(str(decrypted_text)))