package main

import (
	"errors"
	"fmt"
	assert "github.com/stretchr/testify/assert"
	"testing"
	"time"
)

func TestDataStruct(t *testing.T) {
	assert := assert.New(t)

	assert.Nil(NewDataStruct(ModeStack).Head)
}

func TestDataStruct_Add_ModeStack(t *testing.T) {
	assert := assert.New(t)

	ds := NewDataStruct(ModeStack)
	assert.Nil(ds.Head)
	assert.Nil(ds.Tail)

	ds.Add(NewDataElem("1"))

	assert.Equal("1", ds.Head.Data)
	assert.Equal("1", ds.Tail.Data)

	ds.Add(NewDataElem("2"))

	assert.Equal("2", ds.Head.Data)
	assert.Equal("1", ds.Tail.Data)
	assert.Equal("2", ds.Head.Next.Prev.Data)
}

func TestDataStruct_Add_ModeQueue(t *testing.T) {
	assert := assert.New(t)

	ds := NewDataStruct(ModeQueue)
	assert.Nil(ds.Head)
	assert.Nil(ds.Tail)

	ds.Add(NewDataElem("1"))

	assert.Equal("1", ds.Head.Data)
	assert.Equal("1", ds.Tail.Data)

	ds.Add(NewDataElem("2"))

	assert.Equal("2", ds.Head.Data)
	assert.Equal("1", ds.Tail.Data)
	assert.Equal("2", ds.Head.Next.Prev.Data)
}

func TestDataStruct_Retrieve_ModeQueue(t *testing.T) {
	assert := assert.New(t)

	ds := NewDataStruct(ModeQueue)
	ds.Add(NewDataElem("1"))
	ds.Add(NewDataElem("2"))
	assert.Equal("2", ds.Head.Next.Prev.Data)

	dE, err := ds.Retrieve()
	assert.NoError(err)
	assert.Equal("1", dE.Data)
	dE, err = ds.Retrieve()
	assert.NoError(err)
	assert.Equal("2", dE.Data)
	dE, err = ds.Retrieve()
	assert.Error(errors.New("No data found"))
}

func TestDataStruct_Retrieve_ModeStack(t *testing.T) {
	assert := assert.New(t)

	ds := NewDataStruct(ModeStack)
	ds.Add(NewDataElem("1"))
	ds.Add(NewDataElem("2"))
	assert.Equal("2", ds.Head.Next.Prev.Data)

	dE, err := ds.Retrieve()
	assert.NoError(err)
	assert.Equal("2", dE.Data)
	dE, err = ds.Retrieve()
	assert.NoError(err)
	assert.Equal("1", dE.Data)
	dE, err = ds.Retrieve()
	assert.Error(errors.New("No data found"))
}

func TestDataStruct_Retrieve_ModeStack_Mutex(t *testing.T) {
	assert := assert.New(t)

	ds := NewDataStruct(ModeStack)
	ds.Add(NewDataElem("1"))
	ds.Add(NewDataElem("2"))
	assert.Equal("2", ds.Head.Next.Prev.Data)

	c1 := make(chan string)
	c2 := make(chan string)
	c3 := make(chan string)

	var a, b, c *DataElem
	var err error
	go func() {
		a, err = retrieveInTime(ds, time.Duration(4))
		if a != nil {
			c1 <- a.Data
		}
	}()
	// assert.NoError(err)
	// assert.Equal("2", a.Data)
	go func() {
		b, err = retrieveInTime(ds, time.Duration(2))
		if b != nil {
			c2 <- b.Data
		}
	}()
	// assert.Equal("1", b.Data)
	go func() {
		c, err = retrieveInTime(ds, time.Duration(4))
		if c != nil {
			c3 <- c.Data
		}
	}()
	// assert.Error(errors.New("No data found"))

	for i := 0; i < 2; i++ {
		// Await both of these values
		// simultaneously, printing each one as it arrives.
		fmt.Println("retrieved ")
		select {
		case msg1 := <-c1:
			fmt.Println("retrieved ", msg1)
		case msg2 := <-c2:
			fmt.Println("retrieved ", msg2)
		case msg3 := <-c3:
			fmt.Println("retrieved ", msg3)
		}
	}
}

func TestDataStruct_Retrieve_ModeQueue_Mutex(t *testing.T) {
	assert := assert.New(t)

	ds := NewDataStruct(ModeQueue)
	ds.Add(NewDataElem("1"))
	ds.Add(NewDataElem("2"))
	assert.Equal("2", ds.Head.Next.Prev.Data)

	c1 := make(chan string)
	c2 := make(chan string)
	c3 := make(chan string)

	var a, b, c *DataElem
	var err error
	go func() {
		a, err = retrieveInTime(ds, time.Duration(4))
		if a != nil {
			c1 <- a.Data
		}
	}()
	// assert.NoError(err)
	// assert.Equal("2", a.Data)
	go func() {
		b, err = retrieveInTime(ds, time.Duration(2))
		if b != nil {
			c2 <- b.Data
		}
	}()
	// assert.Equal("1", b.Data)
	go func() {
		c, err = retrieveInTime(ds, time.Duration(4))
		if c != nil {
			c3 <- c.Data
		}
	}()
	// assert.Error(errors.New("No data found"))

	for i := 0; i < 2; i++ {
		// Await both of these values
		// simultaneously, printing each one as it arrives.
		fmt.Println("retrieved ")
		select {
		case msg1 := <-c1:
			fmt.Println("retrieved ", msg1)
		case msg2 := <-c2:
			fmt.Println("retrieved ", msg2)
		case msg3 := <-c3:
			fmt.Println("retrieved ", msg3)
		}
	}
}

func retrieveInTime(data *DataStruct, tSec time.Duration) (*DataElem, error) {
	// time.Sleep(tSec)
	return data.Retrieve()
}
