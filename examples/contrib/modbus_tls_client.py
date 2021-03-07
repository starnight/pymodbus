#!/usr/bin/env python
"""
Simple Modbus TCP over TLS client
---------------------------------------------------------------------------

This is a simple example of writing a modbus TCP over TLS client that uses
Python builtin module ssl - TLS/SSL wrapper for socket objects for the TLS
feature.
"""
# -------------------------------------------------------------------------- #
# import neccessary libraries
# -------------------------------------------------------------------------- #
import ssl
from pymodbus.client.sync import ModbusTlsClient

# -------------------------------------------------------------------------- #
# the TLS detail security can be set in SSLContext which is the context here
# -------------------------------------------------------------------------- #
sslctx = ssl.SSLContext(ssl.PROTOCOL_TLS)
sslctx.options |= ssl.OP_NO_SSLv2
sslctx.options |= ssl.OP_NO_SSLv3
sslctx.options |= ssl.OP_NO_TLSv1
sslctx.options |= ssl.OP_NO_TLSv1_1
sslctx.verify_mode = ssl.CERT_REQUIRED
sslctx.check_hostname = True

# Prepare client's certificate which the server requires for TLS full handshake
# sslctx.load_cert_chain(certfile="client.crt", keyfile="client.key",
#                        password="pwd")

# -------------------------------------------------------------------------- #
# pass SSLContext which is the context here to ModbusTcpClient()
# -------------------------------------------------------------------------- #
client = ModbusTlsClient('test.host.com', 8020, sslctx=sslctx)
client.connect()

result = client.read_coils(1, 8)
print(result.bits)

client.close()
