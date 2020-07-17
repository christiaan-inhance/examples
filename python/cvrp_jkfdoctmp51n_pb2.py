# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cvrp-jkfdoctmp51n.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='cvrp-jkfdoctmp51n.proto',
  package='CVRP',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x17\x63vrp-jkfdoctmp51n.proto\x12\x04\x43VRP\"@\n\x07Geocode\x12\n\n\x02id\x18\x01 \x02(\t\x12\t\n\x01x\x18\x02 \x02(\x02\x12\t\n\x01y\x18\x03 \x02(\x02\x12\x13\n\x08quantity\x18\x04 \x02(\x02:\x01\x30\"\xf3\x01\n\x04\x43VRP\x12\x1d\n\x06points\x18\x01 \x03(\x0b\x32\r.CVRP.Geocode\x12\x1c\n\x05\x64\x65pot\x18\x02 \x02(\x0b\x32\r.CVRP.Geocode\x12\x18\n\x10NumberOfVehicles\x18\x03 \x02(\x05\x12\x17\n\x0fVehicleCapacity\x18\x04 \x02(\x02\x12;\n\x0c\x64istancetype\x18\x05 \x01(\x0e\x32\x18.CVRP.CVRP.eDistanceType:\x0bRoadNetwork\">\n\reDistanceType\x12\x0f\n\x0bRoadNetwork\x10\x01\x12\r\n\tEuclidean\x10\x02\x12\r\n\tHaversine\x10\x03\"\xc5\x01\n\x0cSolveRequest\x12\x19\n\x05model\x18\x01 \x01(\x0b\x32\n.CVRP.CVRP\x12\x0f\n\x07modelID\x18\x02 \x01(\t\x12\x15\n\rvisitSequence\x18\x03 \x03(\t\x12\x39\n\tsolveType\x18\x04 \x01(\x0e\x32\x1c.CVRP.SolveRequest.SolveType:\x08Optimise\"7\n\tSolveType\x12\x0c\n\x08Optimise\x10\x00\x12\x0c\n\x08\x45valuate\x10\x01\x12\x0e\n\nReOptimise\x10\x02\"{\n\x04\x45\x64ge\x12\x0c\n\x04\x66rom\x18\x01 \x02(\t\x12\n\n\x02to\x18\x02 \x02(\t\x12\x10\n\x08\x64istance\x18\x03 \x01(\x02\x12%\n\x08geometry\x18\x04 \x03(\x0b\x32\x13.CVRP.Edge.Geometry\x1a \n\x08Geometry\x12\t\n\x01x\x18\x01 \x02(\x02\x12\t\n\x01y\x18\x02 \x02(\x02\"\xa2\x01\n\x10SolutionResponse\x12,\n\x06routes\x18\x01 \x03(\x0b\x32\x1c.CVRP.SolutionResponse.Route\x12\x11\n\tobjective\x18\x02 \x02(\x02\x1aM\n\x05Route\x12\x10\n\x08sequence\x18\x01 \x03(\t\x12\x19\n\x05\x65\x64ges\x18\x02 \x03(\x0b\x32\n.CVRP.Edge\x12\x17\n\x0fvisitCapacities\x18\x03 \x03(\x02')
)



_CVRP_EDISTANCETYPE = _descriptor.EnumDescriptor(
  name='eDistanceType',
  full_name='CVRP.CVRP.eDistanceType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RoadNetwork', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Euclidean', index=1, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Haversine', index=2, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=281,
  serialized_end=343,
)
_sym_db.RegisterEnumDescriptor(_CVRP_EDISTANCETYPE)

_SOLVEREQUEST_SOLVETYPE = _descriptor.EnumDescriptor(
  name='SolveType',
  full_name='CVRP.SolveRequest.SolveType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Optimise', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Evaluate', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ReOptimise', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=488,
  serialized_end=543,
)
_sym_db.RegisterEnumDescriptor(_SOLVEREQUEST_SOLVETYPE)


_GEOCODE = _descriptor.Descriptor(
  name='Geocode',
  full_name='CVRP.Geocode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='CVRP.Geocode.id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='x', full_name='CVRP.Geocode.x', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='CVRP.Geocode.y', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quantity', full_name='CVRP.Geocode.quantity', index=3,
      number=4, type=2, cpp_type=6, label=2,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=97,
)


_CVRP = _descriptor.Descriptor(
  name='CVRP',
  full_name='CVRP.CVRP',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='points', full_name='CVRP.CVRP.points', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='depot', full_name='CVRP.CVRP.depot', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='NumberOfVehicles', full_name='CVRP.CVRP.NumberOfVehicles', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='VehicleCapacity', full_name='CVRP.CVRP.VehicleCapacity', index=3,
      number=4, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='distancetype', full_name='CVRP.CVRP.distancetype', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CVRP_EDISTANCETYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=100,
  serialized_end=343,
)


_SOLVEREQUEST = _descriptor.Descriptor(
  name='SolveRequest',
  full_name='CVRP.SolveRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='model', full_name='CVRP.SolveRequest.model', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='modelID', full_name='CVRP.SolveRequest.modelID', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='visitSequence', full_name='CVRP.SolveRequest.visitSequence', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='solveType', full_name='CVRP.SolveRequest.solveType', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SOLVEREQUEST_SOLVETYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=346,
  serialized_end=543,
)


_EDGE_GEOMETRY = _descriptor.Descriptor(
  name='Geometry',
  full_name='CVRP.Edge.Geometry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='CVRP.Edge.Geometry.x', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='CVRP.Edge.Geometry.y', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=636,
  serialized_end=668,
)

_EDGE = _descriptor.Descriptor(
  name='Edge',
  full_name='CVRP.Edge',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='from', full_name='CVRP.Edge.from', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='to', full_name='CVRP.Edge.to', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='distance', full_name='CVRP.Edge.distance', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='geometry', full_name='CVRP.Edge.geometry', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_EDGE_GEOMETRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=545,
  serialized_end=668,
)


_SOLUTIONRESPONSE_ROUTE = _descriptor.Descriptor(
  name='Route',
  full_name='CVRP.SolutionResponse.Route',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sequence', full_name='CVRP.SolutionResponse.Route.sequence', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='edges', full_name='CVRP.SolutionResponse.Route.edges', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='visitCapacities', full_name='CVRP.SolutionResponse.Route.visitCapacities', index=2,
      number=3, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=756,
  serialized_end=833,
)

_SOLUTIONRESPONSE = _descriptor.Descriptor(
  name='SolutionResponse',
  full_name='CVRP.SolutionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='routes', full_name='CVRP.SolutionResponse.routes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='objective', full_name='CVRP.SolutionResponse.objective', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SOLUTIONRESPONSE_ROUTE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=671,
  serialized_end=833,
)

_CVRP.fields_by_name['points'].message_type = _GEOCODE
_CVRP.fields_by_name['depot'].message_type = _GEOCODE
_CVRP.fields_by_name['distancetype'].enum_type = _CVRP_EDISTANCETYPE
_CVRP_EDISTANCETYPE.containing_type = _CVRP
_SOLVEREQUEST.fields_by_name['model'].message_type = _CVRP
_SOLVEREQUEST.fields_by_name['solveType'].enum_type = _SOLVEREQUEST_SOLVETYPE
_SOLVEREQUEST_SOLVETYPE.containing_type = _SOLVEREQUEST
_EDGE_GEOMETRY.containing_type = _EDGE
_EDGE.fields_by_name['geometry'].message_type = _EDGE_GEOMETRY
_SOLUTIONRESPONSE_ROUTE.fields_by_name['edges'].message_type = _EDGE
_SOLUTIONRESPONSE_ROUTE.containing_type = _SOLUTIONRESPONSE
_SOLUTIONRESPONSE.fields_by_name['routes'].message_type = _SOLUTIONRESPONSE_ROUTE
DESCRIPTOR.message_types_by_name['Geocode'] = _GEOCODE
DESCRIPTOR.message_types_by_name['CVRP'] = _CVRP
DESCRIPTOR.message_types_by_name['SolveRequest'] = _SOLVEREQUEST
DESCRIPTOR.message_types_by_name['Edge'] = _EDGE
DESCRIPTOR.message_types_by_name['SolutionResponse'] = _SOLUTIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Geocode = _reflection.GeneratedProtocolMessageType('Geocode', (_message.Message,), dict(
  DESCRIPTOR = _GEOCODE,
  __module__ = 'cvrp_jkfdoctmp51n_pb2'
  # @@protoc_insertion_point(class_scope:CVRP.Geocode)
  ))
_sym_db.RegisterMessage(Geocode)

CVRP = _reflection.GeneratedProtocolMessageType('CVRP', (_message.Message,), dict(
  DESCRIPTOR = _CVRP,
  __module__ = 'cvrp_jkfdoctmp51n_pb2'
  # @@protoc_insertion_point(class_scope:CVRP.CVRP)
  ))
_sym_db.RegisterMessage(CVRP)

SolveRequest = _reflection.GeneratedProtocolMessageType('SolveRequest', (_message.Message,), dict(
  DESCRIPTOR = _SOLVEREQUEST,
  __module__ = 'cvrp_jkfdoctmp51n_pb2'
  # @@protoc_insertion_point(class_scope:CVRP.SolveRequest)
  ))
_sym_db.RegisterMessage(SolveRequest)

Edge = _reflection.GeneratedProtocolMessageType('Edge', (_message.Message,), dict(

  Geometry = _reflection.GeneratedProtocolMessageType('Geometry', (_message.Message,), dict(
    DESCRIPTOR = _EDGE_GEOMETRY,
    __module__ = 'cvrp_jkfdoctmp51n_pb2'
    # @@protoc_insertion_point(class_scope:CVRP.Edge.Geometry)
    ))
  ,
  DESCRIPTOR = _EDGE,
  __module__ = 'cvrp_jkfdoctmp51n_pb2'
  # @@protoc_insertion_point(class_scope:CVRP.Edge)
  ))
_sym_db.RegisterMessage(Edge)
_sym_db.RegisterMessage(Edge.Geometry)

SolutionResponse = _reflection.GeneratedProtocolMessageType('SolutionResponse', (_message.Message,), dict(

  Route = _reflection.GeneratedProtocolMessageType('Route', (_message.Message,), dict(
    DESCRIPTOR = _SOLUTIONRESPONSE_ROUTE,
    __module__ = 'cvrp_jkfdoctmp51n_pb2'
    # @@protoc_insertion_point(class_scope:CVRP.SolutionResponse.Route)
    ))
  ,
  DESCRIPTOR = _SOLUTIONRESPONSE,
  __module__ = 'cvrp_jkfdoctmp51n_pb2'
  # @@protoc_insertion_point(class_scope:CVRP.SolutionResponse)
  ))
_sym_db.RegisterMessage(SolutionResponse)
_sym_db.RegisterMessage(SolutionResponse.Route)


# @@protoc_insertion_point(module_scope)
