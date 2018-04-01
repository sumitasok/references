package main

import (
	"errors"
)

var (
	// ErrUnknownMode - error when mode is not defined.
	ErrUnknownMode = errors.New("Unknown mode")
)

// DataStruct - hods the data and defined the action that works for stack or queue.
type DataStruct struct {
	Head *DataElem
	Tail *DataElem
	mode mode
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
	return &DataStruct{mode: _mode}
}

// Add add element to the Struct using mode already defined
func (d *DataStruct) Add(dataElem *DataElem) error {
	switch d.mode {
	case ModeStack:
		if d.Head == nil {
			d.Tail = dataElem
		}

		dataElem.Next = d.Head
		d.Head = dataElem
	case ModeQueue:
	default:
		return ErrUnknownMode
	}

	return nil
}

// DataElem - holds each data unit
type DataElem struct {
	Data string
	Next *DataElem
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
