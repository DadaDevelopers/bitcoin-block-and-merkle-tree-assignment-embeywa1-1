import hashlib

def bitcoin_double_sha256(hex_a, hex_b):
    """
    Simulates Bitcoin's Merkle leaf/node pairing.
    Handles Little-Endian byte reversal required by Bitcoin protocol.
    """
    # Reverse bytes to Little-Endian
    ba = bytes.fromhex(hex_a)[::-1]
    bb = bytes.fromhex(hex_b)[::-1]
    
    # Concatenate and Double SHA-256
    step1 = hashlib.sha256(ba + bb).digest()
    step2 = hashlib.sha256(step1).digest()
    
    # Return as Big-Endian hex string
    return step2[::-1].hex()

# Transactions from Block 840,000
tx0 = "a0db149ace545beabbd87a8d6b20ffd6aa3b5a50e58add49a3d435f898c272cf"
tx1 = "2bb85f4b004be6da54f766c17c1e855187327112c231ef2ff35ebad0ea67c69e"
tx2 = "152b928e97bb9e874da1bd4abdf766ae0cdc7a2f260dad5542967cb414c58489"
tx3 = "e79134080a83fe3e0e06ed6990c5a9b63b362313341745707a2bff7d788a1375"

# Calculate Level 1
node_a = bitcoin_double_sha256(tx0, tx1)
node_b = bitcoin_double_sha256(tx2, tx3)

# Calculate Root
merkle_root = bitcoin_double_sha256(node_a, node_b)

print(f"Node A (Hash 0+1): {node_a}")
print(f"Node B (Hash 2+3): {node_b}")
print(f"Calculated Merkle Root: {merkle_root}")
