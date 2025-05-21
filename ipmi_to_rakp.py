#!/usr/bin/env python3

import sys

if len(sys.argv) != 3:
    print("Usage: python3 ipmi_to_rakp.py <ip_address> <ipmi_hash>")
    print('Example:')
    print('  python3 ipmi_to_rakp.py 10.129.248.23 "admin:22203174...:fc85bc04..."')
    sys.exit(1)

ip = sys.argv[1]
input_hash = sys.argv[2]

try:
    parts = input_hash.strip().split(":")
    if len(parts) != 3:
        raise ValueError("Invalid hash format. Expected 3 colon-separated fields.")

    username = parts[0]
    blob = parts[1]
    hmac_hash = parts[2]

    client_random = blob[:80]
    server_random = blob[80:]

    rakp_format = f"$rakp$0${ip}${username}${client_random}${server_random}${hmac_hash}"
    print(rakp_format)

except Exception as e:
    print(f"[!] Error: {e}")
    sys.exit(1)
