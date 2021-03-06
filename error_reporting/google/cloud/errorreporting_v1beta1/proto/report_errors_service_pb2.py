# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/devtools/clouderrorreporting_v1beta1/proto/report_errors_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.cloud.errorreporting_v1beta1.proto import common_pb2 as google_dot_devtools_dot_clouderrorreporting__v1beta1_dot_proto_dot_common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/devtools/clouderrorreporting_v1beta1/proto/report_errors_service.proto',
  package='google.devtools.clouderrorreporting.v1beta1',
  syntax='proto3',
  serialized_pb=_b('\nMgoogle/devtools/clouderrorreporting_v1beta1/proto/report_errors_service.proto\x12+google.devtools.clouderrorreporting.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a>google/devtools/clouderrorreporting_v1beta1/proto/common.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x7f\n\x17ReportErrorEventRequest\x12\x14\n\x0cproject_name\x18\x01 \x01(\t\x12N\n\x05\x65vent\x18\x02 \x01(\x0b\x32?.google.devtools.clouderrorreporting.v1beta1.ReportedErrorEvent\"\x1a\n\x18ReportErrorEventResponse\"\xf7\x01\n\x12ReportedErrorEvent\x12.\n\nevent_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12T\n\x0fservice_context\x18\x02 \x01(\x0b\x32;.google.devtools.clouderrorreporting.v1beta1.ServiceContext\x12\x0f\n\x07message\x18\x03 \x01(\t\x12J\n\x07\x63ontext\x18\x04 \x01(\x0b\x32\x39.google.devtools.clouderrorreporting.v1beta1.ErrorContext2\xf8\x01\n\x13ReportErrorsService\x12\xe0\x01\n\x10ReportErrorEvent\x12\x44.google.devtools.clouderrorreporting.v1beta1.ReportErrorEventRequest\x1a\x45.google.devtools.clouderrorreporting.v1beta1.ReportErrorEventResponse\"?\x82\xd3\xe4\x93\x02\x39\"0/v1beta1/{project_name=projects/*}/events:report:\x05\x65ventB\xf9\x01\n/com.google.devtools.clouderrorreporting.v1beta1B\x18ReportErrorsServiceProtoP\x01Z^google.golang.org/genproto/googleapis/devtools/clouderrorreporting/v1beta1;clouderrorreporting\xaa\x02#Google.Cloud.ErrorReporting.V1Beta1\xca\x02#Google\\Cloud\\ErrorReporting\\V1beta1b\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_devtools_dot_clouderrorreporting__v1beta1_dot_proto_dot_common__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_REPORTERROREVENTREQUEST = _descriptor.Descriptor(
  name='ReportErrorEventRequest',
  full_name='google.devtools.clouderrorreporting.v1beta1.ReportErrorEventRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='project_name', full_name='google.devtools.clouderrorreporting.v1beta1.ReportErrorEventRequest.project_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='event', full_name='google.devtools.clouderrorreporting.v1beta1.ReportErrorEventRequest.event', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=253,
  serialized_end=380,
)


_REPORTERROREVENTRESPONSE = _descriptor.Descriptor(
  name='ReportErrorEventResponse',
  full_name='google.devtools.clouderrorreporting.v1beta1.ReportErrorEventResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=382,
  serialized_end=408,
)


_REPORTEDERROREVENT = _descriptor.Descriptor(
  name='ReportedErrorEvent',
  full_name='google.devtools.clouderrorreporting.v1beta1.ReportedErrorEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='event_time', full_name='google.devtools.clouderrorreporting.v1beta1.ReportedErrorEvent.event_time', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='service_context', full_name='google.devtools.clouderrorreporting.v1beta1.ReportedErrorEvent.service_context', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='google.devtools.clouderrorreporting.v1beta1.ReportedErrorEvent.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='context', full_name='google.devtools.clouderrorreporting.v1beta1.ReportedErrorEvent.context', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=411,
  serialized_end=658,
)

_REPORTERROREVENTREQUEST.fields_by_name['event'].message_type = _REPORTEDERROREVENT
_REPORTEDERROREVENT.fields_by_name['event_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_REPORTEDERROREVENT.fields_by_name['service_context'].message_type = google_dot_devtools_dot_clouderrorreporting__v1beta1_dot_proto_dot_common__pb2._SERVICECONTEXT
_REPORTEDERROREVENT.fields_by_name['context'].message_type = google_dot_devtools_dot_clouderrorreporting__v1beta1_dot_proto_dot_common__pb2._ERRORCONTEXT
DESCRIPTOR.message_types_by_name['ReportErrorEventRequest'] = _REPORTERROREVENTREQUEST
DESCRIPTOR.message_types_by_name['ReportErrorEventResponse'] = _REPORTERROREVENTRESPONSE
DESCRIPTOR.message_types_by_name['ReportedErrorEvent'] = _REPORTEDERROREVENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ReportErrorEventRequest = _reflection.GeneratedProtocolMessageType('ReportErrorEventRequest', (_message.Message,), dict(
  DESCRIPTOR = _REPORTERROREVENTREQUEST,
  __module__ = 'google.devtools.clouderrorreporting_v1beta1.proto.report_errors_service_pb2'
  ,
  __doc__ = """A request for reporting an individual error event.
  
  
  Attributes:
      project_name:
          [Required] The resource name of the Google Cloud Platform
          project. Written as ``projects/`` plus the `Google Cloud
          Platform project ID
          <https://support.google.com/cloud/answer/6158840>`__. Example:
          ``projects/my-project-123``.
      event:
          [Required] The error event to be reported.
  """,
  # @@protoc_insertion_point(class_scope:google.devtools.clouderrorreporting.v1beta1.ReportErrorEventRequest)
  ))
_sym_db.RegisterMessage(ReportErrorEventRequest)

ReportErrorEventResponse = _reflection.GeneratedProtocolMessageType('ReportErrorEventResponse', (_message.Message,), dict(
  DESCRIPTOR = _REPORTERROREVENTRESPONSE,
  __module__ = 'google.devtools.clouderrorreporting_v1beta1.proto.report_errors_service_pb2'
  ,
  __doc__ = """Response for reporting an individual error event. Data may be added to
  this message in the future.
  """,
  # @@protoc_insertion_point(class_scope:google.devtools.clouderrorreporting.v1beta1.ReportErrorEventResponse)
  ))
_sym_db.RegisterMessage(ReportErrorEventResponse)

ReportedErrorEvent = _reflection.GeneratedProtocolMessageType('ReportedErrorEvent', (_message.Message,), dict(
  DESCRIPTOR = _REPORTEDERROREVENT,
  __module__ = 'google.devtools.clouderrorreporting_v1beta1.proto.report_errors_service_pb2'
  ,
  __doc__ = """An error event which is reported to the Error Reporting system.
  
  
  Attributes:
      event_time:
          [Optional] Time when the event occurred. If not provided, the
          time when the event was received by the Error Reporting system
          will be used.
      service_context:
          [Required] The service context in which this error has
          occurred.
      message:
          [Required] A message describing the error. The message can
          contain an exception stack in one of the supported programming
          languages and formats. In that case, the message is parsed and
          detailed exception information is returned when retrieving the
          error event again.
      context:
          [Optional] A description of the context in which the error
          occurred.
  """,
  # @@protoc_insertion_point(class_scope:google.devtools.clouderrorreporting.v1beta1.ReportedErrorEvent)
  ))
_sym_db.RegisterMessage(ReportedErrorEvent)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n/com.google.devtools.clouderrorreporting.v1beta1B\030ReportErrorsServiceProtoP\001Z^google.golang.org/genproto/googleapis/devtools/clouderrorreporting/v1beta1;clouderrorreporting\252\002#Google.Cloud.ErrorReporting.V1Beta1\312\002#Google\\Cloud\\ErrorReporting\\V1beta1'))

_REPORTERRORSSERVICE = _descriptor.ServiceDescriptor(
  name='ReportErrorsService',
  full_name='google.devtools.clouderrorreporting.v1beta1.ReportErrorsService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=661,
  serialized_end=909,
  methods=[
  _descriptor.MethodDescriptor(
    name='ReportErrorEvent',
    full_name='google.devtools.clouderrorreporting.v1beta1.ReportErrorsService.ReportErrorEvent',
    index=0,
    containing_service=None,
    input_type=_REPORTERROREVENTREQUEST,
    output_type=_REPORTERROREVENTRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\0029\"0/v1beta1/{project_name=projects/*}/events:report:\005event')),
  ),
])
_sym_db.RegisterServiceDescriptor(_REPORTERRORSSERVICE)

DESCRIPTOR.services_by_name['ReportErrorsService'] = _REPORTERRORSSERVICE

# @@protoc_insertion_point(module_scope)
