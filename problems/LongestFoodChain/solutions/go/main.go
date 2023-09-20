package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

var graph map[string][]string
var longestChain map[string]int

func dfs(dinosaur string) int {
	// If we've already computed the longest chain for this dinosaur, return it.
	if val, ok := longestChain[dinosaur]; ok {
		return val
	}

	// Initialize the longest chain length for this dinosaur to 1.
	longest := 1

	// Check each prey of the current dinosaur.
	for _, prey := range graph[dinosaur] {
		// Recursively find the longest chain starting from the prey.
		chainLength := 1 + dfs(prey)

		// Update the longest chain length if the current prey leads to a longer chain.
		if chainLength > longest {
			longest = chainLength
		}
	}

	// Store the computed longest chain length for this dinosaur in the map.
	longestChain[dinosaur] = longest

	return longest
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()

	var n int
	fmt.Sscanf(scanner.Text(), "%d", &n)
	graph = make(map[string][]string)
	longestChain = make(map[string]int)

	// Read the input lines and build the graph.
	for i := 0; i < n; i++ {
		scanner.Scan()
		line := scanner.Text()
		parts := strings.Split(line, " <- ")
		predator := parts[0]
		preyList := strings.Split(parts[1], ", ")

		// Add predator and prey relationships to the graph.
		graph[predator] = preyList
	}

	fmt.Println(graph)
	// Initialize a variable to keep track of the longest chain found.
	maxChain := 0

	// Iterate through each dinosaur and find the longest chain starting from it.
	for dinosaur := range graph {
		chainLength := dfs(dinosaur)
		if chainLength > maxChain {
			maxChain = chainLength
		}
	}
	fmt.Println(maxChain)
}
