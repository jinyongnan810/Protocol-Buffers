protoc -I protos/simple/ --python_out=protos/simple/ protos/simple/simple.proto
protoc -I protos/enum/ --python_out=protos/enum/ protos/enum/enum_demo.proto
protoc -I protos/complex/ --python_out=protos/complex/ protos/complex/complex.proto