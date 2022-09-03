package main

import (
	"fmt"
	"log"

	// "rsc.io/quote"

	"example.com/greetings"
)

func main() {
	// fmt.Println("hello world")
	// fmt.Println(quote.Go())
	log.SetPrefix("greetings: ")
	log.SetFlags(0)

	message, err := greetings.Hello("aaag")
	if err != nil {
		log.Fatal(err)
	}
	// message := greetings.Hello("ben")
	fmt.Println(message)

	names := []string{"aaaa", "bbbb"}
	meg, e := greetings.Hellos(names)
	if e != nil {
		log.Fatal(err)
	}
	fmt.Println(meg)

}
