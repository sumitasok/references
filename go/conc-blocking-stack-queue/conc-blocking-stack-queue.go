package main

import (
	"errors"
	"sync"
)

var (
	// ErrUnknownMode - error when mode is not defined.
	ErrUnknownMode = errors.New("Unknown mode")
	// ErrNoDataFound - error no data found.
	ErrNoDataFound = errors.New("No data found")
)

// DataStruct - hods the data and defined the action that works for stack or queue.
type DataStruct struct {
	Head  *DataElem
	Tail  *DataElem
	mode  mode
	mutex *sync.Mutex
}

type mode string

var (
	// ModeStack - define mode as stack
	ModeStack mode = "stack"
	// ModeQueue - define mode as queue
	ModeQueue mode = "queue"
)

// NewDataStruct - return new Data Struct
func NewDataStruct(_mode mode) *DataStruct {
	var mutex = &sync.Mutex{}
	return &DataStruct{mode: _mode, mutex: mutex}
}

// Add add element to the Struct using mode already defined
func (d *DataStruct) Add(dataElem *DataElem) error {
	d.mutex.Lock()
	defer d.mutex.Unlock()

	switch d.mode {
	case ModeStack:
		if d.Head == nil {
			d.Tail = dataElem
		}

		dataElem.Next = d.Head
		if d.Head != nil {
			d.Head.Prev = dataElem
		}
		d.Head = dataElem
	case ModeQueue:
		if d.Head == nil {
			d.Tail = dataElem
		}

		dataElem.Next = d.Head
		if d.Head != nil {
			d.Head.Prev = dataElem
		}
		d.Head = dataElem
	default:
		return ErrUnknownMode
	}

	return nil
}

// Retrieve retrieve element from the Struct using mode already defined
func (d *DataStruct) Retrieve() (*DataElem, error) {
	d.mutex.Lock()
	defer d.mutex.Unlock()

	if d.Head == nil {
		return nil, ErrNoDataFound
	}

	item := &DataElem{}

	switch d.mode {
	case ModeStack:
		item = d.Head
		d.Head = d.Head.Next
		if d.Head == nil {
			d.Tail = nil
		} else {
			d.Head.Prev = nil
		}
	case ModeQueue:
		item = d.Tail
		d.Tail = d.Tail.Prev
		if d.Tail == nil {
			d.Head = nil
		} else {
			d.Tail.Next = nil
		}
	default:
		return nil, ErrUnknownMode
	}

	return item, nil
}

// DataElem - holds each data unit
type DataElem struct {
	Data string
	Next *DataElem
	Prev *DataElem
}

// NewDataElem - return new Data Element
func NewDataElem(data string) *DataElem {
	return &DataElem{Data: data}
}

func main() {
	dsS := NewDataStruct(ModeStack)
	dsS.Add(NewDataElem("1"))

	dsQ := NewDataStruct(ModeQueue)
	dsQ.Add(NewDataElem("1"))
}
