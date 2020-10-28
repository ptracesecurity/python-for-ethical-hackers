#!/usr/bin/env python3
#
# Gianni Gnesa (gnix)
# www.ptrace-security.com
#
#
# Example of output:
# ==================
# ➜ python3 shellcode_basic_usage.py
# b'ABCDEFGH'
# b'4142434445464748'
# b'\x41\x42\x43\x44\x45\x46\x47\x48'
# b'QUJDREVGR0g='
# b'\x41\x42\x43\x44\x45\x46\x47\x48'
#

import sys
import base64
import binascii


def main():

    ##### Store your payload #####

    payload = b"\x41\x42\x43\x44\x45\x46\x47\x48"

    payload2 = (
        b"\x41\x42\x43\x44\x45\x46\x47\x48\x41\x42\x43\x44\x45\x46\x47\x48"
        b"\x41\x42\x43\x44\x45\x46\x47\x48\x41\x42\x43\x44\x45\x46\x47\x48"
        b"\x41\x42\x43\x44\x45\x46\x47\x48\x41\x42\x43\x44\x45\x46\x47\x48"
        b"\x41\x42\x43\x44\x45\x46\x47\x48\x41\x42\x43\x44\x45\x46\x47\x48"
    )

    payload3 =  b"\x41\x42\x43\x44\x45\x46\x47\x48\x41\x42\x43\x44\x45\x46\x47\x48"
    payload3 += b"\x41\x42\x43\x44\x45\x46\x47\x48\x41\x42\x43\x44\x45\x46\x47\x48"
    payload3 += b"\x41\x42\x43\x44\x45\x46\x47\x48\x41\x42\x43\x44\x45\x46\x47\x48"
    payload3 += b"\x41\x42\x43\x44\x45\x46\x47\x48\x41\x42\x43\x44\x45\x46\x47\x48"
    payload3 += b"\x41\x42\x43\x44\x45\x46\x47\x48\x41\x42\x43\x44\x45\x46\x47\x48"
    payload3 += b"\x41\x42\x43\x44\x45\x46\x47\x48\x41\x42\x43\x44\x45\x46\x47\x48"
    payload3 += b"\x41\x42\x43\x44\x45\x46\x47\x48\x41\x42\x43\x44\x45\x46\x47\x48"



    ##### Display the content of your payload variable #####

    # Default print (Good for alphanumeric payloads)
    print(payload)

    # Get a hex representation
    print(binascii.hexlify(payload))

    # Get an hex representation with the \x prefix
    print("b'{}'".format(''.join('\\x{:02x}'.format(b) for b in payload)))



    ##### Base64 Encode/decode your payload #####

    # Base64 encode the payload
    encoded_payload = base64.b64encode(payload)
    print(encoded_payload)

    # Base64 decode the payload
    decoded_payload = base64.b64decode(encoded_payload)
    print("b'{}'".format(''.join('\\x{:02x}'.format(b) for b in decoded_payload)))


    sys.exit(0)


if __name__ == "__main__":
    main()
