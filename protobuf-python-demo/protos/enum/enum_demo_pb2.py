# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: enum_demo.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='enum_demo.proto',
  package='example.enumerations',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0f\x65num_demo.proto\x12\x14\x65xample.enumerations\"V\n\x0b\x45numMessage\x12\n\n\x02id\x18\x01 \x01(\x05\x12;\n\x0f\x64\x61y_of_the_week\x18\x02 \x01(\x0e\x32\".example.enumerations.DayOfTheWeek*w\n\x0c\x44\x61yOfTheWeek\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06MONDAY\x10\x01\x12\x0b\n\x07TUESDAY\x10\x02\x12\r\n\tWEDNESDAY\x10\x03\x12\x0c\n\x08THURSDAY\x10\x04\x12\n\n\x06\x46RIDAY\x10\x05\x12\x0c\n\x08SATURDAY\x10\x06\x12\n\n\x06SUNDAY\x10\x07\x62\x06proto3'
)

_DAYOFTHEWEEK = _descriptor.EnumDescriptor(
  name='DayOfTheWeek',
  full_name='example.enumerations.DayOfTheWeek',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MONDAY', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TUESDAY', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WEDNESDAY', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='THURSDAY', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FRIDAY', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SATURDAY', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SUNDAY', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=129,
  serialized_end=248,
)
_sym_db.RegisterEnumDescriptor(_DAYOFTHEWEEK)

DayOfTheWeek = enum_type_wrapper.EnumTypeWrapper(_DAYOFTHEWEEK)
UNKNOWN = 0
MONDAY = 1
TUESDAY = 2
WEDNESDAY = 3
THURSDAY = 4
FRIDAY = 5
SATURDAY = 6
SUNDAY = 7



_ENUMMESSAGE = _descriptor.Descriptor(
  name='EnumMessage',
  full_name='example.enumerations.EnumMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='example.enumerations.EnumMessage.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='day_of_the_week', full_name='example.enumerations.EnumMessage.day_of_the_week', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=41,
  serialized_end=127,
)

_ENUMMESSAGE.fields_by_name['day_of_the_week'].enum_type = _DAYOFTHEWEEK
DESCRIPTOR.message_types_by_name['EnumMessage'] = _ENUMMESSAGE
DESCRIPTOR.enum_types_by_name['DayOfTheWeek'] = _DAYOFTHEWEEK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EnumMessage = _reflection.GeneratedProtocolMessageType('EnumMessage', (_message.Message,), {
  'DESCRIPTOR' : _ENUMMESSAGE,
  '__module__' : 'enum_demo_pb2'
  # @@protoc_insertion_point(class_scope:example.enumerations.EnumMessage)
  })
_sym_db.RegisterMessage(EnumMessage)


# @@protoc_insertion_point(module_scope)
