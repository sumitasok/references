package main

import (
	"fmt"
)

func main() {
	messages := make(chan string, 2)

	messages <- "buffered"
	messages <- "ping"

	fmt.Println(<-messages)
	fmt.Println(<-messages)

	messages <- "ping"
	fmt.Println(<-messages)
}
