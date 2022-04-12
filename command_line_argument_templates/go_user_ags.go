package main

import (
    "flag"
    "fmt"
)
func main() {
    ip := flag.String("i", "127.0.0.1", "IP of Listening Host")
    port := flag.Int("p", 8443, "Listening Port Number")
    opt := flag.String("o", "/bin/sh", "Desired shell option")
    method := flag.String("m", "rev", "Shell Method: bind or rev")

    flag.Parse()

    fmt.Println("IP:", *ip)
    fmt.Println("Port:", *port)
    fmt.Println("Option:", *opt)
    fmt.Println("Method:", *method)
}
