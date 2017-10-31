package main

import (
	"bufio"
	"errors"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func readIntArrayFromInput() ([]int, error) {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter the int array space separated: \n")
	text, _ := reader.ReadString('\n')
	strArray := strings.Fields(text)

	intArray := []int{}
	for _, intStr := range strArray {
		intValue, err := strconv.Atoi(intStr)
		if err == nil {
			intArray = append(intArray, intValue)
		}
	}

	return intArray, nil

}

func readInt() (int, error) {
	var i int
	fmt.Scan(&i)
	return i, nil
}

func Nge(intArray []int) ([]int, error) {
	if len(intArray) < 2 {
		return []int{}, errors.New("no more elements to parse")
	}
	if intArray[0] > intArray[1] {
		if len(intArray) > 2 {
			return Gt(append([]int{intArray[0]}, intArray[2:len(intArray)]...))
		} else {
			return []int{intArray[0]}, nil
		}
	} else {
		if len(intArray) > 2 {
			elements, err := Gt(intArray[1:len(intArray)])
			return append([]int{intArray[0]}, elements...), err
		} else {
			return intArray, nil
		}
	}
}

func main() {
	intArray, err := readIntArrayFromInput()
	if err != nil {
		panic(err)
		return
	}

	intArrayLen := len(intArray)
	fmt.Printf(" read : %v, len %v , errs: %v\n", intArray, intArrayLen, err)

	intQ, err := readInt()
	fmt.Printf("q : %v\n", intQ)

	intIndex, err := readInt()
	fmt.Printf("q : %v\n", intIndex)

	if intIndex >= intArrayLen {
		panic("index out bound")
		return
	}

}
