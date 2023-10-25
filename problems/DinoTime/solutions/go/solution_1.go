package main

import (
	"bufio"
	"fmt"
	"os"
)

var MOVES = [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func main() {

	// Read input
	scanner := bufio.NewScanner(os.Stdin)
	var rows, cols int
	scanner.Scan()
	fmt.Sscanf(scanner.Text(), "%d,%d", &rows, &cols)

	mapData := make([][]byte, rows)
	for i := 0; i < rows; i++ {
		scanner.Scan()
		mapData[i] = []byte(scanner.Text())
	}

	// Find the starting point
	startX, startY := -1, -1

	for i, row := range mapData {
		for j, tile := range row {
			if tile == '@' {
				startX, startY = i, j
				break
			}
		}
	}
	if startX == -1 || startY == -1 {
		fmt.Printf("Cannot find dino")
		return
	}

	// Make the initial visited array
	visited := make([][]bool, rows)
	for i := 0; i < rows; i++ {
		visited[i] = make([]bool, cols)
	}

	// Recurse to find entry point
	maxSize := calculateMaxSize(Map{
		MapData: mapData,
		Visited: visited,
		Rows:    rows,
		Cols:    cols,
	}, startX, startY, 1, 0, 1)
	fmt.Println(maxSize)
}

type Map struct {
	MapData [][]byte
	Visited [][]bool
	Rows    int
	Cols    int
}

func calculateMaxSize(world Map, x, y, currentSize, tummy, energy int) int {
	if energy <= 0 {
		return currentSize
	}

	maxSize := currentSize
	world.Visited[x][y] = true

	// Duplicate to be passed for "most" cases
	newWorld := Map{
		Visited: Clone(world.Visited),
		MapData: world.MapData,
		Rows:    world.Rows,
		Cols:    world.Cols,
	}

	for _, move := range MOVES {
		newX, newY := x+move[0], y+move[1]

		if validMove(newX, newY, world.Rows, world.Cols, world.Visited) {
			switch tile := world.MapData[newX][newY]; {
			case tile == '.' || tile == '@':
				maxSize = max(maxSize, calculateMaxSize(newWorld, newX, newY, currentSize, tummy, energy-1))
			case tile == '~' || tile == '"' && energy > 1:
				maxSize = max(maxSize, calculateMaxSize(newWorld, newX, newY, currentSize, tummy, energy-2))
			case tile == '*' && energy > 2:
				maxSize = max(maxSize, calculateMaxSize(newWorld, newX, newY, currentSize, tummy, energy-3))
			case tile >= 'A' && tile <= 'Z' && int(tile)-64 <= currentSize:

				// Eat the dino
				var newSize = currentSize
				var newTummy = tummy

				foodSize := int(tile) - 64
				if foodSize <= currentSize {

					newTummy += foodSize

					if newTummy >= newSize {
						newTummy = newTummy - newSize
						newSize = newSize + 1
					}
				}

				// Update the map
				duplicate := Clone(world.MapData)
				duplicate[newX][newY] = '.'

				// Clear visited
				// Make the initial visited array
				visited := make([][]bool, world.Rows)
				for i := 0; i < world.Rows; i++ {
					visited[i] = make([]bool, world.Cols)
				}

				// Try simulation on new map
				maxSize = max(maxSize, calculateMaxSize(Map{
					Visited: visited,
					MapData: duplicate,
					Rows:    world.Rows,
					Cols:    world.Cols,
				}, newX, newY, newSize, newTummy, newSize))
			}
		}
	}
	return maxSize
}

func Clone[T any](input [][]T) [][]T {
	rows := len(input)
	cols := len(input[0])

	duplicate := make([][]T, rows)
	for i := range input {
		duplicate[i] = make([]T, cols)
		copy(duplicate[i], input[i])
	}

	return duplicate
}

func validMove(x, y, rows, cols int, visited [][]bool) bool {
	return x >= 0 && x < rows && y >= 0 && y < cols && !visited[x][y]
}
