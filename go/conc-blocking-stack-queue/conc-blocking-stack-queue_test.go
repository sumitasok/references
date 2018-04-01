package main

import (
	"errors"
	assert "github.com/stretchr/testify/assert"
	"testing"
	// "time"
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
