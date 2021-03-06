# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hello_world.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='hello_world.proto',
  package='test',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11hello_world.proto\x12\x04test\")\n\x0cHelloGrpcReq\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03\x61ge\x18\x02 \x01(\x05\" \n\x0eHelloGrpcReply\x12\x0e\n\x06result\x18\x01 \x01(\t\"\xa9\x01\n\x0cHelloTestReq\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03\x61ge\x18\x02 \x01(\x03\x12\x0c\n\x04\x64\x61ta\x18\x03 \x03(\t\x12.\n\x06\x64\x65tail\x18\x04 \x03(\x0b\x32\x1e.test.HelloTestReq.DetailEntry\x1a@\n\x0b\x44\x65tailEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12 \n\x05value\x18\x02 \x01(\x0b\x32\x11.test.DetailValue:\x02\x38\x01\"K\n\x0b\x44\x65tailValue\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03\x61ge\x18\x02 \x01(\x03\x12\x0e\n\x06gender\x18\x03 \x01(\t\x12\x11\n\tis_active\x18\x04 \x01(\x08\"\x10\n\x0eHelloTestReply\"\x1d\n\rSendStreamReq\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\"!\n\x0fSendStreamReply\x12\x0e\n\x06result\x18\x01 \x01(\t\"\x1d\n\rRecvStreamReq\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\"!\n\x0fRecvStreamReply\x12\x0e\n\x06result\x18\x01 \x01(\t\"\x1f\n\x0f\x44oubleStreamReq\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\"#\n\x11\x44oubleStreamReply\x12\x0e\n\x06result\x18\x01 \x01(\t2\xcc\x02\n\nHelloWorld\x12\x36\n\x08show_msg\x12\x12.test.HelloGrpcReq\x1a\x14.test.HelloGrpcReply\"\x00\x12\x41\n\x0fshow_detail_msg\x12\x12.test.HelloTestReq\x1a\x14.test.HelloTestReply\"\x00(\x01\x30\x01\x12=\n\x0bsend_stream\x12\x13.test.SendStreamReq\x1a\x15.test.SendStreamReply\"\x00\x30\x01\x12=\n\x0brecv_stream\x12\x13.test.RecvStreamReq\x1a\x15.test.RecvStreamReply\"\x00(\x01\x12\x45\n\rdouble_stream\x12\x15.test.DoubleStreamReq\x1a\x17.test.DoubleStreamReply\"\x00(\x01\x30\x01\x62\x06proto3'
)




_HELLOGRPCREQ = _descriptor.Descriptor(
  name='HelloGrpcReq',
  full_name='test.HelloGrpcReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='test.HelloGrpcReq.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='age', full_name='test.HelloGrpcReq.age', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=27,
  serialized_end=68,
)


_HELLOGRPCREPLY = _descriptor.Descriptor(
  name='HelloGrpcReply',
  full_name='test.HelloGrpcReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='test.HelloGrpcReply.result', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=70,
  serialized_end=102,
)


_HELLOTESTREQ_DETAILENTRY = _descriptor.Descriptor(
  name='DetailEntry',
  full_name='test.HelloTestReq.DetailEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='test.HelloTestReq.DetailEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='test.HelloTestReq.DetailEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=210,
  serialized_end=274,
)

_HELLOTESTREQ = _descriptor.Descriptor(
  name='HelloTestReq',
  full_name='test.HelloTestReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='test.HelloTestReq.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='age', full_name='test.HelloTestReq.age', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='test.HelloTestReq.data', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='detail', full_name='test.HelloTestReq.detail', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_HELLOTESTREQ_DETAILENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=105,
  serialized_end=274,
)


_DETAILVALUE = _descriptor.Descriptor(
  name='DetailValue',
  full_name='test.DetailValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='test.DetailValue.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='age', full_name='test.DetailValue.age', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gender', full_name='test.DetailValue.gender', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_active', full_name='test.DetailValue.is_active', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=276,
  serialized_end=351,
)


_HELLOTESTREPLY = _descriptor.Descriptor(
  name='HelloTestReply',
  full_name='test.HelloTestReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=353,
  serialized_end=369,
)


_SENDSTREAMREQ = _descriptor.Descriptor(
  name='SendStreamReq',
  full_name='test.SendStreamReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='test.SendStreamReq.data', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=371,
  serialized_end=400,
)


_SENDSTREAMREPLY = _descriptor.Descriptor(
  name='SendStreamReply',
  full_name='test.SendStreamReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='test.SendStreamReply.result', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=402,
  serialized_end=435,
)


_RECVSTREAMREQ = _descriptor.Descriptor(
  name='RecvStreamReq',
  full_name='test.RecvStreamReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='test.RecvStreamReq.data', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=437,
  serialized_end=466,
)


_RECVSTREAMREPLY = _descriptor.Descriptor(
  name='RecvStreamReply',
  full_name='test.RecvStreamReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='test.RecvStreamReply.result', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=468,
  serialized_end=501,
)


_DOUBLESTREAMREQ = _descriptor.Descriptor(
  name='DoubleStreamReq',
  full_name='test.DoubleStreamReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='test.DoubleStreamReq.data', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=503,
  serialized_end=534,
)


_DOUBLESTREAMREPLY = _descriptor.Descriptor(
  name='DoubleStreamReply',
  full_name='test.DoubleStreamReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='test.DoubleStreamReply.result', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=536,
  serialized_end=571,
)

_HELLOTESTREQ_DETAILENTRY.fields_by_name['value'].message_type = _DETAILVALUE
_HELLOTESTREQ_DETAILENTRY.containing_type = _HELLOTESTREQ
_HELLOTESTREQ.fields_by_name['detail'].message_type = _HELLOTESTREQ_DETAILENTRY
DESCRIPTOR.message_types_by_name['HelloGrpcReq'] = _HELLOGRPCREQ
DESCRIPTOR.message_types_by_name['HelloGrpcReply'] = _HELLOGRPCREPLY
DESCRIPTOR.message_types_by_name['HelloTestReq'] = _HELLOTESTREQ
DESCRIPTOR.message_types_by_name['DetailValue'] = _DETAILVALUE
DESCRIPTOR.message_types_by_name['HelloTestReply'] = _HELLOTESTREPLY
DESCRIPTOR.message_types_by_name['SendStreamReq'] = _SENDSTREAMREQ
DESCRIPTOR.message_types_by_name['SendStreamReply'] = _SENDSTREAMREPLY
DESCRIPTOR.message_types_by_name['RecvStreamReq'] = _RECVSTREAMREQ
DESCRIPTOR.message_types_by_name['RecvStreamReply'] = _RECVSTREAMREPLY
DESCRIPTOR.message_types_by_name['DoubleStreamReq'] = _DOUBLESTREAMREQ
DESCRIPTOR.message_types_by_name['DoubleStreamReply'] = _DOUBLESTREAMREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HelloGrpcReq = _reflection.GeneratedProtocolMessageType('HelloGrpcReq', (_message.Message,), {
  'DESCRIPTOR' : _HELLOGRPCREQ,
  '__module__' : 'hello_world_pb2'
  # @@protoc_insertion_point(class_scope:test.HelloGrpcReq)
  })
_sym_db.RegisterMessage(HelloGrpcReq)

HelloGrpcReply = _reflection.GeneratedProtocolMessageType('HelloGrpcReply', (_message.Message,), {
  'DESCRIPTOR' : _HELLOGRPCREPLY,
  '__module__' : 'hello_world_pb2'
  # @@protoc_insertion_point(class_scope:test.HelloGrpcReply)
  })
_sym_db.RegisterMessage(HelloGrpcReply)

HelloTestReq = _reflection.GeneratedProtocolMessageType('HelloTestReq', (_message.Message,), {

  'DetailEntry' : _reflection.GeneratedProtocolMessageType('DetailEntry', (_message.Message,), {
    'DESCRIPTOR' : _HELLOTESTREQ_DETAILENTRY,
    '__module__' : 'hello_world_pb2'
    # @@protoc_insertion_point(class_scope:test.HelloTestReq.DetailEntry)
    })
  ,
  'DESCRIPTOR' : _HELLOTESTREQ,
  '__module__' : 'hello_world_pb2'
  # @@protoc_insertion_point(class_scope:test.HelloTestReq)
  })
_sym_db.RegisterMessage(HelloTestReq)
_sym_db.RegisterMessage(HelloTestReq.DetailEntry)

DetailValue = _reflection.GeneratedProtocolMessageType('DetailValue', (_message.Message,), {
  'DESCRIPTOR' : _DETAILVALUE,
  '__module__' : 'hello_world_pb2'
  # @@protoc_insertion_point(class_scope:test.DetailValue)
  })
_sym_db.RegisterMessage(DetailValue)

HelloTestReply = _reflection.GeneratedProtocolMessageType('HelloTestReply', (_message.Message,), {
  'DESCRIPTOR' : _HELLOTESTREPLY,
  '__module__' : 'hello_world_pb2'
  # @@protoc_insertion_point(class_scope:test.HelloTestReply)
  })
_sym_db.RegisterMessage(HelloTestReply)

SendStreamReq = _reflection.GeneratedProtocolMessageType('SendStreamReq', (_message.Message,), {
  'DESCRIPTOR' : _SENDSTREAMREQ,
  '__module__' : 'hello_world_pb2'
  # @@protoc_insertion_point(class_scope:test.SendStreamReq)
  })
_sym_db.RegisterMessage(SendStreamReq)

SendStreamReply = _reflection.GeneratedProtocolMessageType('SendStreamReply', (_message.Message,), {
  'DESCRIPTOR' : _SENDSTREAMREPLY,
  '__module__' : 'hello_world_pb2'
  # @@protoc_insertion_point(class_scope:test.SendStreamReply)
  })
_sym_db.RegisterMessage(SendStreamReply)

RecvStreamReq = _reflection.GeneratedProtocolMessageType('RecvStreamReq', (_message.Message,), {
  'DESCRIPTOR' : _RECVSTREAMREQ,
  '__module__' : 'hello_world_pb2'
  # @@protoc_insertion_point(class_scope:test.RecvStreamReq)
  })
_sym_db.RegisterMessage(RecvStreamReq)

RecvStreamReply = _reflection.GeneratedProtocolMessageType('RecvStreamReply', (_message.Message,), {
  'DESCRIPTOR' : _RECVSTREAMREPLY,
  '__module__' : 'hello_world_pb2'
  # @@protoc_insertion_point(class_scope:test.RecvStreamReply)
  })
_sym_db.RegisterMessage(RecvStreamReply)

DoubleStreamReq = _reflection.GeneratedProtocolMessageType('DoubleStreamReq', (_message.Message,), {
  'DESCRIPTOR' : _DOUBLESTREAMREQ,
  '__module__' : 'hello_world_pb2'
  # @@protoc_insertion_point(class_scope:test.DoubleStreamReq)
  })
_sym_db.RegisterMessage(DoubleStreamReq)

DoubleStreamReply = _reflection.GeneratedProtocolMessageType('DoubleStreamReply', (_message.Message,), {
  'DESCRIPTOR' : _DOUBLESTREAMREPLY,
  '__module__' : 'hello_world_pb2'
  # @@protoc_insertion_point(class_scope:test.DoubleStreamReply)
  })
_sym_db.RegisterMessage(DoubleStreamReply)


_HELLOTESTREQ_DETAILENTRY._options = None

_HELLOWORLD = _descriptor.ServiceDescriptor(
  name='HelloWorld',
  full_name='test.HelloWorld',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=574,
  serialized_end=906,
  methods=[
  _descriptor.MethodDescriptor(
    name='show_msg',
    full_name='test.HelloWorld.show_msg',
    index=0,
    containing_service=None,
    input_type=_HELLOGRPCREQ,
    output_type=_HELLOGRPCREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='show_detail_msg',
    full_name='test.HelloWorld.show_detail_msg',
    index=1,
    containing_service=None,
    input_type=_HELLOTESTREQ,
    output_type=_HELLOTESTREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='send_stream',
    full_name='test.HelloWorld.send_stream',
    index=2,
    containing_service=None,
    input_type=_SENDSTREAMREQ,
    output_type=_SENDSTREAMREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='recv_stream',
    full_name='test.HelloWorld.recv_stream',
    index=3,
    containing_service=None,
    input_type=_RECVSTREAMREQ,
    output_type=_RECVSTREAMREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='double_stream',
    full_name='test.HelloWorld.double_stream',
    index=4,
    containing_service=None,
    input_type=_DOUBLESTREAMREQ,
    output_type=_DOUBLESTREAMREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_HELLOWORLD)

DESCRIPTOR.services_by_name['HelloWorld'] = _HELLOWORLD

# @@protoc_insertion_point(module_scope)
