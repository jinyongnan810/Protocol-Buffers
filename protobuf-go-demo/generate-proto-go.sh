export PATH=$PATH:$(go env GOPATH)/bin
protoc -I protos --go_out=protos/simple protos/simple/simple.proto
protoc -I protos --go_out=protos protos/enum/enum_demo.proto
protoc -I protos --go_out=protos protos/complex/complex.proto