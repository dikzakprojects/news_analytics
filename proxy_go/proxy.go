package main

import (
	"context"
	"flag"
	"fmt"
	"log"
	pb "proxy/protos"
	"time"

	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
)

var (
	addr = flag.String("addr", "localhost:50051", "the address to connect to")
	url = flag.String("url", "BBC", "news site to scrape")
)

func main() {
	flag.Parse()
	// Set up a connection to the server.
	conn, err := grpc.Dial(*addr, grpc.WithTransportCredentials(insecure.NewCredentials()))
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	defer conn.Close()

	client := pb.NewProxyClient(conn)

	// Contact the server and print out its response.
	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()

	r, err := client.GetScraperData(ctx, &pb.ScraperDataRequest{Url: *url})

	if err != nil {
		log.Fatalf("could not greet: %v", err)
	}

	fmt.Println(r.Data[0])
}