from __future__ import print_function

import msgpackrpc #install as admin: pip install msgpack-rpc-python
import numpy as np #pip install numpy

from .types import *

class UE4Poly(object):
    def __init__(self, ip = "", port = 3000, timeout_value = 3600):
        if (ip == ""):
            ip = "127.0.0.1"
        self.client = msgpackrpc.Client(msgpackrpc.Address(ip, port), timeout = timeout_value, pack_encoding = 'utf-8', unpack_encoding = 'utf-8')

    def ping(self):
        return self.client.call('ping', 'ping')

    def draw_polygon(self, cmd):
        return self.client.call('drawPolygon', cmd)