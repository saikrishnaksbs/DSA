package main

import (
	"fmt"
)

func main() {

	// create a 2d array of size 3x3
	fmt.Print("Enter number of queens: ")

	var arr [3][3]string
	for i := 0; i < 3; i++ {
		for j:= 0; j < 3; j++ {
			arr[i][j] = "_"
		}
	}
	nqueens(arr, 0, 0)
}

func nqueens(arr [3][3]string, i int, j int) {

	solve_nqueens(arr, i, j)
	
}

func solve_nqueens(arr[3][3]string, i int, j int) [][]string, int, int {

	if i > 3 {
		return arr
	}
	
}

