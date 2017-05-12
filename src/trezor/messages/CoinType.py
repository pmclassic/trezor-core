# Automatically generated by pb2py
import protobuf as p

class CoinType(p.MessageType):
    FIELDS = {
        1: ('coin_name', p.UnicodeType, 0),
        2: ('coin_shortcut', p.UnicodeType, 0),
        3: ('address_type', p.UVarintType, 0), # default=0
        4: ('maxfee_kb', p.UVarintType, 0),
        5: ('address_type_p2sh', p.UVarintType, 0), # default=5
        8: ('signed_message_header', p.UnicodeType, 0),
        9: ('xpub_magic', p.UVarintType, 0), # default=76067358
        10: ('xprv_magic', p.UVarintType, 0), # default=76066276
        11: ('segwit', p.BoolType, 0),
    }
