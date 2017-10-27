package main

import (
	"fmt"
	"time"
)

func main() {
	messages := make(chan string)

	go func() {
		fmt.Println("before channel")
		messages <- "ping"
		fmt.Println("after channel")
	}()

	// fmt.Println("before sleep")
	// time.Sleep(10 * time.Second)
	// fmt.Println("after sleep")
	msg := <-messages
	fmt.Println(msg)

	// go channel(messages)
}

func channel(messages chan string) {
	fmt.Println("before sleep")
	time.Sleep(10 * time.Second)
	fmt.Println("after sleep")
}
