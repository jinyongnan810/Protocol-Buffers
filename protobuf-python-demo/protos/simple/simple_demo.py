import simple_pb2
import json
from protobuf_to_dict import protobuf_to_dict, dict_to_protobuf
sm = simple_pb2.SimpleMessage()
sm.id = 7
sm.name = "test name"
sm.is_simple = True
sm.sample_list.extend([1, 3, 5])
print(sm)

# write to a file
print("-----write to file-----")
with open("protobuf-python-demo/protos/simple/simple.bin", "wb") as f:
    bytesOfString = sm.SerializeToString()
    f.write(bytesOfString)
# read from the file
print("-----read from file-----")
with open("protobuf-python-demo/protos/simple/simple.bin", "rb") as f:
    sm2 = simple_pb2.SimpleMessage().FromString(f.read())
print(sm2)
# parse to dict & json
print("-----parse to dict & json-----")
proto_dict = protobuf_to_dict(sm)
print(proto_dict)
print(json.dumps(proto_dict))
# parse from dict & json
print("-----parse from dict & json-----")
json_str = json.dumps(proto_dict)
dict_from_json = json.loads(json_str)
sm3 = dict_to_protobuf(simple_pb2.SimpleMessage, values=dict_from_json)
print(sm3)
