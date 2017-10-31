package main

import (
	"fmt"
	"reflect"
	"testing"
)

func TestNge(t *testing.T) {
	intArray, _ := Nge([]int{3, 4, 2})
	if len(intArray) == 0 {
		t.Error("count not corect")
	}

	fmt.Println(intArray)

	if !reflect.DeepEqual(intArray, []int{3, 4}) {
		t.Error("output not correct")
	}

	intArray, _ = Nge([]int{3, 4, 2, 7, 5, 8, 10, 6})

	if len(intArray) == 0 {
		t.Error("count not corect")
	}

	fmt.Println(intArray)

	if !reflect.DeepEqual(intArray, []int{3, 4, 7, 8, 10}) {
		t.Error("output not correct")
	}
}
