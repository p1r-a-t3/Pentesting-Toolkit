package main

import (
    "fmt"
    "os"
)

func main() {
    file, err := os.Open("ataylor.png")
    if err != nil {
        fmt.Println(err)
        return
    }
    info, _ := os.Stat("ataylor.png")
    input := make([]byte, info.Size())
    out := make([]byte, len(input))
    file.Read(input)

    key := [...]byte{0x43, 0x53, 0x41, 0x57} // CSAW
    for i := 0; i < len(input); i++ {
        out[i] = input[i] ^ key[i%len(key)]
    }

    fmt.Println(string(out))
}