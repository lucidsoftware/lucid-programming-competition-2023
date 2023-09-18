#!/usr/bin/env python3
from typing import List, Set

class Species:

    def __init__(
        self,
        name: str,
        known_attrs: List[str]
    ) -> None:
        self.known_attrs = set(known_attrs)
        self.name = name

    def compute_likelihood_score(self, fossil_attrs: Set[str]):
        score = 0
        for attr in fossil_attrs:
            if attr in self.known_attrs:
                score += 1
            else:
                score -= 1
        score *= 100
        score /= len(self.known_attrs)
        return score


def compute_most_likely_species(species: List[Species], fossil_attrs: List[str]):
    best_species_score = float('-inf')
    best_species_name = ""

    for spec in species:
        score = spec.compute_likelihood_score(fossil_attrs)
        if score > best_species_score:
            best_species_score = score
            best_species_name = spec.name

    if best_species_score >= 50:
        __debug_sanity_check_no_ties_in_highest_score(species, fossil_attrs, best_species_score)
        return best_species_name
    else:
        return "Possible New Discovery"


def __debug_sanity_check_no_ties_in_highest_score(species: List[Species], fossil_attrs: List[str], highest_score: float):
    matches = []
    for spec in species:
        score = spec.compute_likelihood_score(fossil_attrs)
        if score == highest_score:
            matches.append(spec.name)
    if len(matches) >= 2:
        print(f"WARNING: Illegal tied score of {highest_score} for the following: {matches}")


def main():
    species: List[Species] = []

    total_species = int(input())
    for _ in range(total_species):
        name = input()
        num_attrs = int(input())
        attrs = []
        for _ in range(num_attrs):
            attrs.append(input())
        species.append(Species(name, attrs))

    total_fossils = int(input())
    for _ in range(total_fossils):
        num_attrs = int(input())
        attrs = []
        for _ in range(num_attrs):
            attrs.append(input())
        print(compute_most_likely_species(species, attrs))


if __name__ == "__main__":
    main()