# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/news.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10proto/news.proto\"!\n\x12ScraperDataRequest\x12\x0b\n\x03url\x18\x01 \x01(\t\"+\n\x0fScraperResponse\x12\x18\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\n.Analytics\"\x94\x01\n\tAnalytics\x12\x0c\n\x04word\x18\x01 \x01(\t\x12\x17\n\x0fscrape_datetime\x18\x02 \x01(\t\x12\x0e\n\x06source\x18\x03 \x01(\t\x12\x1d\n\x10\x61rticle_datetime\x18\x04 \x01(\tH\x00\x88\x01\x01\x12\x12\n\x05\x63ount\x18\x05 \x01(\x05H\x01\x88\x01\x01\x42\x13\n\x11_article_datetimeB\x08\n\x06_count2B\n\x05Proxy\x12\x39\n\x0egetScraperData\x12\x13.ScraperDataRequest\x1a\x10.ScraperResponse\"\x00\x42\x14Z\x12../proxy_go/protosb\x06proto3')



_SCRAPERDATAREQUEST = DESCRIPTOR.message_types_by_name['ScraperDataRequest']
_SCRAPERRESPONSE = DESCRIPTOR.message_types_by_name['ScraperResponse']
_ANALYTICS = DESCRIPTOR.message_types_by_name['Analytics']
ScraperDataRequest = _reflection.GeneratedProtocolMessageType('ScraperDataRequest', (_message.Message,), {
  'DESCRIPTOR' : _SCRAPERDATAREQUEST,
  '__module__' : 'proto.news_pb2'
  # @@protoc_insertion_point(class_scope:ScraperDataRequest)
  })
_sym_db.RegisterMessage(ScraperDataRequest)

ScraperResponse = _reflection.GeneratedProtocolMessageType('ScraperResponse', (_message.Message,), {
  'DESCRIPTOR' : _SCRAPERRESPONSE,
  '__module__' : 'proto.news_pb2'
  # @@protoc_insertion_point(class_scope:ScraperResponse)
  })
_sym_db.RegisterMessage(ScraperResponse)

Analytics = _reflection.GeneratedProtocolMessageType('Analytics', (_message.Message,), {
  'DESCRIPTOR' : _ANALYTICS,
  '__module__' : 'proto.news_pb2'
  # @@protoc_insertion_point(class_scope:Analytics)
  })
_sym_db.RegisterMessage(Analytics)

_PROXY = DESCRIPTOR.services_by_name['Proxy']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\022../proxy_go/protos'
  _SCRAPERDATAREQUEST._serialized_start=20
  _SCRAPERDATAREQUEST._serialized_end=53
  _SCRAPERRESPONSE._serialized_start=55
  _SCRAPERRESPONSE._serialized_end=98
  _ANALYTICS._serialized_start=101
  _ANALYTICS._serialized_end=249
  _PROXY._serialized_start=251
  _PROXY._serialized_end=317
# @@protoc_insertion_point(module_scope)
