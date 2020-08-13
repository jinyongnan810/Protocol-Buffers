import enum_demo_pb2
em = enum_demo_pb2.EnumMessage()
em.id = 1
em.day_of_the_week = enum_demo_pb2.TUESDAY
print(em)
