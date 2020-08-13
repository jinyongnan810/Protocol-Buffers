#### compilation sample
`protoc -I=. --python_out=basics/python basics/*.proto`
#### run go in vscode
~~~~ bash
go get -v github.com/go-delve/delve/cmd/dlv
go get -u google.golang.org/protobuf/cmd/protoc-gen-go
go install google.golang.org/protobuf/cmd/protoc-gen-go
go mod init example.com/protos # for imports
~~~~
