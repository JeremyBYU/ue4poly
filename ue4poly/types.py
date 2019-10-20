from __future__ import print_function
import msgpackrpc #install as admin: pip install msgpack-rpc-python
import numpy as np #pip install numpy

class MsgpackMixin:
    def __repr__(self):
        from pprint import pformat
        return "<" + type(self).__name__ + "> " + pformat(vars(self), indent=4, width=1)

    def to_msgpack(self, *args, **kwargs):
        return self.__dict__

    @classmethod
    def from_msgpack(cls, encoded):
        obj = cls()
        #obj.__dict__ = {k.decode('utf-8'): (from_msgpack(v.__class__, v) if hasattr(v, "__dict__") else v) for k, v in encoded.items()}
        obj.__dict__ = { k : (v if not isinstance(v, dict) else getattr(getattr(obj, k).__class__, "from_msgpack")(v)) for k, v in encoded.items()}
        #return cls(**msgpack.unpack(encoded))
        return obj



class DPCommand(MsgpackMixin): 
    lifetime = -1.0
    shell = []
    holes = [[]]
    shell_color = [1, 50, 32]
    hole_color = [255, 153, 0]
    thickness = 1.0

    def __init__(self, lifetime=-1.0, shell=[], holes=[[]], shell_color=[0, 128, 0], hole_color=[255, 153, 0], thickness=1.0):
        self.lifetime = lifetime
        self.shell = shell
        self.holes = holes
        self.shell_color = shell_color
        self.hole_color = hole_color
        self.thickness = thickness
