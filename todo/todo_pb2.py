# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: todo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\ntodo.proto\x12\x04todo\x1a\x1bgoogle/protobuf/empty.proto"G\n\x04Todo\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04task\x18\x02 \x01(\t\x12\x14\n\x0cis_completed\x18\x03 \x01(\x08\x12\x0f\n\x07\x63reated\x18\x04 \x01(\t"\x11\n\x0fTodoListRequest"!\n\x13TodoRetrieveRequest\x12\n\n\x02id\x18\x01 \x01(\x03\x32\xed\x01\n\x0eTodoController\x12-\n\x04List\x12\x15.todo.TodoListRequest\x1a\n.todo.Todo"\x00\x30\x01\x12"\n\x06\x43reate\x12\n.todo.Todo\x1a\n.todo.Todo"\x00\x12\x33\n\x08Retrieve\x12\x19.todo.TodoRetrieveRequest\x1a\n.todo.Todo"\x00\x12"\n\x06Update\x12\n.todo.Todo\x1a\n.todo.Todo"\x00\x12/\n\x07\x44\x65stroy\x12\n.todo.Todo\x1a\x16.google.protobuf.Empty"\x00\x62\x06proto3'
)


_TODO = DESCRIPTOR.message_types_by_name["Todo"]
_TODOLISTREQUEST = DESCRIPTOR.message_types_by_name["TodoListRequest"]
_TODORETRIEVEREQUEST = DESCRIPTOR.message_types_by_name["TodoRetrieveRequest"]
Todo = _reflection.GeneratedProtocolMessageType(
    "Todo",
    (_message.Message,),
    {
        "DESCRIPTOR": _TODO,
        "__module__": "todo_pb2"
        # @@protoc_insertion_point(class_scope:todo.Todo)
    },
)
_sym_db.RegisterMessage(Todo)

TodoListRequest = _reflection.GeneratedProtocolMessageType(
    "TodoListRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _TODOLISTREQUEST,
        "__module__": "todo_pb2"
        # @@protoc_insertion_point(class_scope:todo.TodoListRequest)
    },
)
_sym_db.RegisterMessage(TodoListRequest)

TodoRetrieveRequest = _reflection.GeneratedProtocolMessageType(
    "TodoRetrieveRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _TODORETRIEVEREQUEST,
        "__module__": "todo_pb2"
        # @@protoc_insertion_point(class_scope:todo.TodoRetrieveRequest)
    },
)
_sym_db.RegisterMessage(TodoRetrieveRequest)

_TODOCONTROLLER = DESCRIPTOR.services_by_name["TodoController"]
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _TODO._serialized_start = 49
    _TODO._serialized_end = 120
    _TODOLISTREQUEST._serialized_start = 122
    _TODOLISTREQUEST._serialized_end = 139
    _TODORETRIEVEREQUEST._serialized_start = 141
    _TODORETRIEVEREQUEST._serialized_end = 174
    _TODOCONTROLLER._serialized_start = 177
    _TODOCONTROLLER._serialized_end = 414
# @@protoc_insertion_point(module_scope)
