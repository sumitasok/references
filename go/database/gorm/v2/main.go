package main

import (
	"fmt"
	_ "github.com/sirupsen/logrus"
	"gorm.io/driver/postgres"
	"gorm.io/gorm"
	"log"
)

var config = struct {
	PgHost     string
	PgPort     string
	PgDbname   string
	PgUser     string
	PgPassword string
	PgSslmode  string
}{
	PgHost:     "localhost", // "db", // "localhost",
	PgPort:     "5432",      // "5432",
	PgDbname:   "dbtest",
	PgUser:     "sumitasok",
	PgPassword: "nest-skyward-decision",
	PgSslmode:  "disable", // "require" (default), "verify-full", "verify-ca", and "disable" supported
}

var pgConnStr = fmt.Sprintf("host=%s port=%s user=%s dbname=%s password=%s sslmode=%s",
	config.PgHost, config.PgPort, config.PgUser, config.PgDbname, config.PgPassword, config.PgSslmode)

func main() {
	db, err := gorm.Open(postgres.Open(pgConnStr), &gorm.Config{})
	if err != nil {
		log.Panicln(err.Error())
	}

	db.AutoMigrate(&Data{})

	data := Data{Name: "Sumit"}

	err = db.Create(data).Error
	log.Panicln(err)
}

type Data struct {
	Name string `gorm:"size:50;not null;" json:"name"`
}
