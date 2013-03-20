# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: descriptions.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='descriptions.proto',
  package='',
  serialized_pb='\n\x12\x64\x65scriptions.proto\"Q\n\x0fHostDescription\x12\x0e\n\x06hostId\x18\x01 \x02(\t\x12.\n\x12\x64\x65viceDescriptions\x18\x02 \x03(\x0b\x32\x12.DeviceDescription\"9\n\x11\x44\x65viceDescription\x12\x10\n\x08\x64\x65viceId\x18\x01 \x02(\t\x12\x12\n\ndeviceType\x18\x02 \x02(\t')




_HOSTDESCRIPTION = _descriptor.Descriptor(
  name='HostDescription',
  full_name='HostDescription',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hostId', full_name='HostDescription.hostId', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deviceDescriptions', full_name='HostDescription.deviceDescriptions', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  extension_ranges=[],
  serialized_start=22,
  serialized_end=103,
)


_DEVICEDESCRIPTION = _descriptor.Descriptor(
  name='DeviceDescription',
  full_name='DeviceDescription',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='deviceId', full_name='DeviceDescription.deviceId', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deviceType', full_name='DeviceDescription.deviceType', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  extension_ranges=[],
  serialized_start=105,
  serialized_end=162,
)

_HOSTDESCRIPTION.fields_by_name['deviceDescriptions'].message_type = _DEVICEDESCRIPTION
DESCRIPTOR.message_types_by_name['HostDescription'] = _HOSTDESCRIPTION
DESCRIPTOR.message_types_by_name['DeviceDescription'] = _DEVICEDESCRIPTION

class HostDescription(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HOSTDESCRIPTION

  # @@protoc_insertion_point(class_scope:HostDescription)

class DeviceDescription(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DEVICEDESCRIPTION

  # @@protoc_insertion_point(class_scope:DeviceDescription)


# @@protoc_insertion_point(module_scope)
