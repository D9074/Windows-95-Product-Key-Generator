import random

def generate_oem_key():
    # Generate ordinal day (XXX) between 001 and 366
    day = f"{random.randint(1, 366):03}"

    # Generate year (YY) between 1995 and 2003
    year = random.choice([str(y)[-2:] for y in range(1995, 2004)])

    # Set fixed "OEM" and "00"
    oem = "OEM"
    nn = "00"

    # Generate SSSSS where sum of digits is divisible by 7
    while True:
        sssss = f"{random.randint(0, 99999):05}"
        if sum(int(d) for d in sssss) % 7 == 0:
            break

    # Generate random ZZZZZ
    zzzzz = f"{random.randint(0, 99999):05}"

    return f"{day}{year}-{oem}-{nn}{sssss}-{zzzzz}"

# Generate and print a key
print(generate_oem_key())
