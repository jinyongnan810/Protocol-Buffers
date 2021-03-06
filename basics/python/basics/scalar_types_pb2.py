# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: basics/scalar-types.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from basics import date_pb2 as basics_dot_date__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='basics/scalar-types.proto',
  package='person',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x19\x62\x61sics/scalar-types.proto\x12\x06person\x1a\x11\x62\x61sics/date.proto\"\xa9\x03\n\x06Person\x12\x0b\n\x03\x61ge\x18\x01 \x01(\x05\x12\x12\n\nfirst_name\x18\x02 \x01(\t\x12\x11\n\tlast_name\x18\x03 \x01(\t\x12\x0e\n\x06\x61vatar\x18\x04 \x01(\x0c\x12\x18\n\x10is_profile_valid\x18\x05 \x01(\x08\x12\x0e\n\x06height\x18\x06 \x01(\x02\x12\x15\n\rphone_numbers\x18\x07 \x03(\t\x12*\n\teye_color\x18\x08 \x01(\x0e\x32\x17.person.Person.EyeColor\x12\x1f\n\x08\x62iethday\x18\t \x01(\x0b\x32\r.my.date.Date\x12\'\n\x07\x61\x64\x64ress\x18\n \x01(\x0b\x32\x16.person.Person.Address\x1ak\n\x07\x41\x64\x64ress\x12\x16\n\x0e\x61\x64\x64ress_line_1\x18\x01 \x01(\t\x12\x16\n\x0e\x61\x64\x64ress_line_2\x18\x02 \x01(\t\x12\x10\n\x08zip_code\x18\x03 \x01(\t\x12\r\n\x05state\x18\x04 \x01(\t\x12\x0f\n\x07\x63ountry\x18\x05 \x01(\t\"7\n\x08\x45yeColor\x12\x0b\n\x07UNKNOWN\x10\x00\x12\t\n\x05GREEN\x10\x01\x12\t\n\x05\x42ROWN\x10\x02\x12\x08\n\x04\x42LUE\x10\x03\x62\x06proto3'
  ,
  dependencies=[basics_dot_date__pb2.DESCRIPTOR,])



_PERSON_EYECOLOR = _descriptor.EnumDescriptor(
  name='EyeColor',
  full_name='person.Person.EyeColor',
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
      name='GREEN', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BROWN', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BLUE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=427,
  serialized_end=482,
)
_sym_db.RegisterEnumDescriptor(_PERSON_EYECOLOR)


_PERSON_ADDRESS = _descriptor.Descriptor(
  name='Address',
  full_name='person.Person.Address',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='address_line_1', full_name='person.Person.Address.address_line_1', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address_line_2', full_name='person.Person.Address.address_line_2', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='zip_code', full_name='person.Person.Address.zip_code', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='person.Person.Address.state', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='country', full_name='person.Person.Address.country', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=318,
  serialized_end=425,
)

_PERSON = _descriptor.Descriptor(
  name='Person',
  full_name='person.Person',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='age', full_name='person.Person.age', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='first_name', full_name='person.Person.first_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_name', full_name='person.Person.last_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='avatar', full_name='person.Person.avatar', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_profile_valid', full_name='person.Person.is_profile_valid', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='height', full_name='person.Person.height', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='phone_numbers', full_name='person.Person.phone_numbers', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='eye_color', full_name='person.Person.eye_color', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='biethday', full_name='person.Person.biethday', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='person.Person.address', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_PERSON_ADDRESS, ],
  enum_types=[
    _PERSON_EYECOLOR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=57,
  serialized_end=482,
)

_PERSON_ADDRESS.containing_type = _PERSON
_PERSON.fields_by_name['eye_color'].enum_type = _PERSON_EYECOLOR
_PERSON.fields_by_name['biethday'].message_type = basics_dot_date__pb2._DATE
_PERSON.fields_by_name['address'].message_type = _PERSON_ADDRESS
_PERSON_EYECOLOR.containing_type = _PERSON
DESCRIPTOR.message_types_by_name['Person'] = _PERSON
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Person = _reflection.GeneratedProtocolMessageType('Person', (_message.Message,), {

  'Address' : _reflection.GeneratedProtocolMessageType('Address', (_message.Message,), {
    'DESCRIPTOR' : _PERSON_ADDRESS,
    '__module__' : 'basics.scalar_types_pb2'
    # @@protoc_insertion_point(class_scope:person.Person.Address)
    })
  ,
  'DESCRIPTOR' : _PERSON,
  '__module__' : 'basics.scalar_types_pb2'
  # @@protoc_insertion_point(class_scope:person.Person)
  })
_sym_db.RegisterMessage(Person)
_sym_db.RegisterMessage(Person.Address)


# @@protoc_insertion_point(module_scope)
