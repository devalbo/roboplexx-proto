# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tasktypes.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import common_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tasktypes.proto',
  package='',
  serialized_pb='\n\x0ftasktypes.proto\x1a\x0c\x63ommon.proto\"\\\n\x17SetDevicePropertiesTask\x12\x0e\n\x06hostId\x18\x01 \x02(\t\x12\x12\n\ndevicePath\x18\x02 \x03(\t\x12\x1d\n\nproperties\x18\x03 \x03(\x0b\x32\t.Property\"r\n\x14\x44oDeviceCommandsTask\x12\x0e\n\x06hostId\x18\x01 \x02(\t\x12\x12\n\ndevicePath\x18\x02 \x03(\t\x12\x11\n\tcommandId\x18\x03 \x02(\t\x12#\n\x10\x63ommandArguments\x18\x04 \x03(\x0b\x32\t.Property\"F\n\x15SetHostPropertiesTask\x12\x0e\n\x06hostId\x18\x01 \x02(\t\x12\x1d\n\nproperties\x18\x02 \x03(\x0b\x32\t.Property\"\\\n\x12\x44oHostCommandsTask\x12\x0e\n\x06hostId\x18\x01 \x02(\t\x12\x11\n\tcommandId\x18\x02 \x02(\t\x12#\n\x10\x63ommandArguments\x18\x03 \x03(\x0b\x32\t.Property')




_SETDEVICEPROPERTIESTASK = _descriptor.Descriptor(
  name='SetDevicePropertiesTask',
  full_name='SetDevicePropertiesTask',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hostId', full_name='SetDevicePropertiesTask.hostId', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='devicePath', full_name='SetDevicePropertiesTask.devicePath', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='properties', full_name='SetDevicePropertiesTask.properties', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=33,
  serialized_end=125,
)


_DODEVICECOMMANDSTASK = _descriptor.Descriptor(
  name='DoDeviceCommandsTask',
  full_name='DoDeviceCommandsTask',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hostId', full_name='DoDeviceCommandsTask.hostId', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='devicePath', full_name='DoDeviceCommandsTask.devicePath', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='commandId', full_name='DoDeviceCommandsTask.commandId', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='commandArguments', full_name='DoDeviceCommandsTask.commandArguments', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=127,
  serialized_end=241,
)


_SETHOSTPROPERTIESTASK = _descriptor.Descriptor(
  name='SetHostPropertiesTask',
  full_name='SetHostPropertiesTask',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hostId', full_name='SetHostPropertiesTask.hostId', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='properties', full_name='SetHostPropertiesTask.properties', index=1,
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
  serialized_start=243,
  serialized_end=313,
)


_DOHOSTCOMMANDSTASK = _descriptor.Descriptor(
  name='DoHostCommandsTask',
  full_name='DoHostCommandsTask',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hostId', full_name='DoHostCommandsTask.hostId', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='commandId', full_name='DoHostCommandsTask.commandId', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='commandArguments', full_name='DoHostCommandsTask.commandArguments', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=315,
  serialized_end=407,
)

_SETDEVICEPROPERTIESTASK.fields_by_name['properties'].message_type = common_pb2._PROPERTY
_DODEVICECOMMANDSTASK.fields_by_name['commandArguments'].message_type = common_pb2._PROPERTY
_SETHOSTPROPERTIESTASK.fields_by_name['properties'].message_type = common_pb2._PROPERTY
_DOHOSTCOMMANDSTASK.fields_by_name['commandArguments'].message_type = common_pb2._PROPERTY
DESCRIPTOR.message_types_by_name['SetDevicePropertiesTask'] = _SETDEVICEPROPERTIESTASK
DESCRIPTOR.message_types_by_name['DoDeviceCommandsTask'] = _DODEVICECOMMANDSTASK
DESCRIPTOR.message_types_by_name['SetHostPropertiesTask'] = _SETHOSTPROPERTIESTASK
DESCRIPTOR.message_types_by_name['DoHostCommandsTask'] = _DOHOSTCOMMANDSTASK

class SetDevicePropertiesTask(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SETDEVICEPROPERTIESTASK

  # @@protoc_insertion_point(class_scope:SetDevicePropertiesTask)

class DoDeviceCommandsTask(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DODEVICECOMMANDSTASK

  # @@protoc_insertion_point(class_scope:DoDeviceCommandsTask)

class SetHostPropertiesTask(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SETHOSTPROPERTIESTASK

  # @@protoc_insertion_point(class_scope:SetHostPropertiesTask)

class DoHostCommandsTask(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DOHOSTCOMMANDSTASK

  # @@protoc_insertion_point(class_scope:DoHostCommandsTask)


# @@protoc_insertion_point(module_scope)
