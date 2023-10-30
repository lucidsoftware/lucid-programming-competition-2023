package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	var count int

	// Read from stdin
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	_, _ = fmt.Sscanf(scanner.Text(), "%d", &count)
	scanner.Scan()
	numbersStrings := strings.Fields(scanner.Text())

	// Iterate through the strings and convert them to numbers
	var numbers []int
	for _, str := range numbersStrings {
		num, _ := strconv.Atoi(str)
		numbers = append(numbers, num)
	}

	// Calculations
	holes := 0
	for i := 1; i < count; i++ {
		prev := numbers[i-1]
		current := numbers[i]
		if prev-current >= 4 {
			holes++
		}
	}
	fmt.Println(holes)
}
