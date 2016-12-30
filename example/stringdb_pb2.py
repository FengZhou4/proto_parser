# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stringdb.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='stringdb.proto',
  package='stringdb',
  syntax='proto3',
  serialized_pb=_b('\n\x0estringdb.proto\x12\x08stringdb\"\x1e\n\x0fGetValueRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\"\x1e\n\rGetValueReply\x12\r\n\x05value\x18\x01 \x01(\t\"-\n\x0fSetValueRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\x1e\n\rSetValueReply\x12\r\n\x05value\x18\x01 \x01(\t\" \n\x11\x43ountValueRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\" \n\x0f\x43ountValueReply\x12\r\n\x05\x63ount\x18\x01 \x01(\x03\x32\xd6\x01\n\x08StringDb\x12@\n\x08GetValue\x12\x19.stringdb.GetValueRequest\x1a\x17.stringdb.GetValueReply\"\x00\x12@\n\x08SetValue\x12\x19.stringdb.SetValueRequest\x1a\x17.stringdb.SetValueReply\"\x00\x12\x46\n\nCountValue\x12\x1b.stringdb.CountValueRequest\x1a\x19.stringdb.CountValueReply\"\x00\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_GETVALUEREQUEST = _descriptor.Descriptor(
  name='GetValueRequest',
  full_name='stringdb.GetValueRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='stringdb.GetValueRequest.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=58,
)


_GETVALUEREPLY = _descriptor.Descriptor(
  name='GetValueReply',
  full_name='stringdb.GetValueReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='stringdb.GetValueReply.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=60,
  serialized_end=90,
)


_SETVALUEREQUEST = _descriptor.Descriptor(
  name='SetValueRequest',
  full_name='stringdb.SetValueRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='stringdb.SetValueRequest.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='stringdb.SetValueRequest.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=92,
  serialized_end=137,
)


_SETVALUEREPLY = _descriptor.Descriptor(
  name='SetValueReply',
  full_name='stringdb.SetValueReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='stringdb.SetValueReply.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=139,
  serialized_end=169,
)


_COUNTVALUEREQUEST = _descriptor.Descriptor(
  name='CountValueRequest',
  full_name='stringdb.CountValueRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='stringdb.CountValueRequest.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=171,
  serialized_end=203,
)


_COUNTVALUEREPLY = _descriptor.Descriptor(
  name='CountValueReply',
  full_name='stringdb.CountValueReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='count', full_name='stringdb.CountValueReply.count', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=205,
  serialized_end=237,
)

DESCRIPTOR.message_types_by_name['GetValueRequest'] = _GETVALUEREQUEST
DESCRIPTOR.message_types_by_name['GetValueReply'] = _GETVALUEREPLY
DESCRIPTOR.message_types_by_name['SetValueRequest'] = _SETVALUEREQUEST
DESCRIPTOR.message_types_by_name['SetValueReply'] = _SETVALUEREPLY
DESCRIPTOR.message_types_by_name['CountValueRequest'] = _COUNTVALUEREQUEST
DESCRIPTOR.message_types_by_name['CountValueReply'] = _COUNTVALUEREPLY

GetValueRequest = _reflection.GeneratedProtocolMessageType('GetValueRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETVALUEREQUEST,
  __module__ = 'stringdb_pb2'
  # @@protoc_insertion_point(class_scope:stringdb.GetValueRequest)
  ))
_sym_db.RegisterMessage(GetValueRequest)

GetValueReply = _reflection.GeneratedProtocolMessageType('GetValueReply', (_message.Message,), dict(
  DESCRIPTOR = _GETVALUEREPLY,
  __module__ = 'stringdb_pb2'
  # @@protoc_insertion_point(class_scope:stringdb.GetValueReply)
  ))
_sym_db.RegisterMessage(GetValueReply)

SetValueRequest = _reflection.GeneratedProtocolMessageType('SetValueRequest', (_message.Message,), dict(
  DESCRIPTOR = _SETVALUEREQUEST,
  __module__ = 'stringdb_pb2'
  # @@protoc_insertion_point(class_scope:stringdb.SetValueRequest)
  ))
_sym_db.RegisterMessage(SetValueRequest)

SetValueReply = _reflection.GeneratedProtocolMessageType('SetValueReply', (_message.Message,), dict(
  DESCRIPTOR = _SETVALUEREPLY,
  __module__ = 'stringdb_pb2'
  # @@protoc_insertion_point(class_scope:stringdb.SetValueReply)
  ))
_sym_db.RegisterMessage(SetValueReply)

CountValueRequest = _reflection.GeneratedProtocolMessageType('CountValueRequest', (_message.Message,), dict(
  DESCRIPTOR = _COUNTVALUEREQUEST,
  __module__ = 'stringdb_pb2'
  # @@protoc_insertion_point(class_scope:stringdb.CountValueRequest)
  ))
_sym_db.RegisterMessage(CountValueRequest)

CountValueReply = _reflection.GeneratedProtocolMessageType('CountValueReply', (_message.Message,), dict(
  DESCRIPTOR = _COUNTVALUEREPLY,
  __module__ = 'stringdb_pb2'
  # @@protoc_insertion_point(class_scope:stringdb.CountValueReply)
  ))
_sym_db.RegisterMessage(CountValueReply)