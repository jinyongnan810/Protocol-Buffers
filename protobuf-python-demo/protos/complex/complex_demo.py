import complex_pb2

dm1 = complex_pb2.DummyMessage()
dm1.id = 1
dm1.name = "dm1"
dm2 = complex_pb2.DummyMessage()
dm2.id = 2
dm2.name = "dm2"
dm3 = complex_pb2.DummyMessage()
dm3.id = 3
dm3.name = "dm3"
cm = complex_pb2.ComplexMessage()
# cm.one_dummy = dm1
cm.one_dummy.id = 1
cm.one_dummy.name = "dm1"

# repeated fields
# method 1
cm.multiple_dummy.extend([dm2, dm3])
# method 2
dm4 = cm.multiple_dummy.add()
dm4.id = 4
dm4.name = "dm4"
# method 3
cm.multiple_dummy.add(id=5, name="dm5")
print(cm)
