package main

import (
	"fmt"
)

func main() {
	type_check(2)
	type_check("two")
	type_check(true)
}

func type_check(v interface{}) {

	switch value := v.(type) {
	case int:
		fmt.Printf("Twice %v is %v\n", value, value*2)
	case string:
		fmt.Printf("%q is %v bytes long\n", value, len(value))
	default:
		fmt.Printf("I dont know about type %T\n", value)
	}

}
