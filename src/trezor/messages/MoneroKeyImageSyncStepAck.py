# Automatically generated by pb2py
# fmt: off
import protobuf as p

from .MoneroExportedKeyImage import MoneroExportedKeyImage

if __debug__:
    try:
        from typing import List
    except ImportError:
        List = None  # type: ignore


class MoneroKeyImageSyncStepAck(p.MessageType):
    MESSAGE_WIRE_TYPE = 533

    def __init__(
        self,
        kis: List[MoneroExportedKeyImage] = None,
    ) -> None:
        self.kis = kis if kis is not None else []

    @classmethod
    def get_fields(cls):
        return {
            1: ('kis', MoneroExportedKeyImage, p.FLAG_REPEATED),
        }
