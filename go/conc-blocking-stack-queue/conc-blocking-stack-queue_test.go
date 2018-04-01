package main

import (
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
}
