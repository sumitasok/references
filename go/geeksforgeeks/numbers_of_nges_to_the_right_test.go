package main

import (
	"fmt"
	"reflect"
	"testing"
)

func TestNge(t *testing.T) {
	data := []struct {
		input  []int
		output []int
	}{
		{
			input:  []int{3, 4, 2},
			output: []int{3, 4},
		},
		{
			input:  []int{3, 4, 2, 7, 5, 8, 10, 6},
			output: []int{3, 4, 7, 8, 10},
		},
	}

	for i := range data {
		intArray, _ := Nge(data[i].input)
		if len(intArray) == 0 {
			t.Error("count not corect")
		}

		fmt.Println(intArray)

		if !reflect.DeepEqual(intArray, data[i].output) {
			t.Error("output not correct")
		}
	}
}
