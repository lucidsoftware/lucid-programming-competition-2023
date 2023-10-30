#!/usr/bin/env python3
import argparse
import secrets
import random
import string
from typing import List

def main():
    args = argparse.ArgumentParser()
    args.add_argument("--species", type=int, required=True)
    args.add_argument("--fossils", type=int, required=True)
    args.add_argument("--attrs-low", type=int, default=2)
    args.add_argument("--attrs-high", type=int, default=10)
    args.add_argument("--attrs-pool-size", type=int, default=20)
    args = args.parse_args()
    generate(
        args.species,
        args.fossils,
        args.attrs_low,
        args.attrs_high,
        args.attrs_pool_size,
    )


def generate_nonce():
    return "".join(secrets.choice(string.ascii_letters + string.digits) for _ in range(32))

def generate_species_name():
    return f"Sp{generate_nonce()}"

def generate_attribute_name():
    return f"At{generate_nonce()}"

def print_attributes(attrs_low, attrs_high, pool: List[str]):
    attrs = random.sample(pool, random.randint(attrs_low, attrs_high))
    print(len(attrs))
    for a in attrs:
        print(a)

def generate(species: int, fossils: int, attrs_low: int, attrs_high: int, attrs_pool_size: int):
    pool = [generate_attribute_name() for _ in range(attrs_pool_size)]
    print(species)
    for _ in range(species):
        print(generate_species_name())
        print_attributes(attrs_low, attrs_high, pool)
    print(fossils)
    for _ in range(fossils):
        print_attributes(attrs_low, attrs_high, pool)





if __name__ == "__main__":
    main()