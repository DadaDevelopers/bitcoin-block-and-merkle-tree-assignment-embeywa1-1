import urllib.request
import json

# Fetching by Height (Block 840,000)
height = 840000
# First, get the hash for this height
hash_url = f"https://mempool.space/api/block-height/{height}"

try:
    print(f"Fetching Hash for Height {height}...")
    with urllib.request.urlopen(hash_url) as response:
        block_hash = response.read().decode().strip()
    
    print(f"Block Hash found: {block_hash}")
    
    # Now get the full block data
    data_url = f"https://mempool.space/api/block/{block_hash}"
    with urllib.request.urlopen(data_url) as response:
        data = json.loads(response.read().decode())
        
        # Save to your assignment file
        with open("block-inspection.md", "w") as f:
            f.write("Block Inspection Results\n")
            f.write("------------------------\n")
            f.write(f"Block Height: {data['height']}\n")
            f.write(f"Block Hash: {data['id']}\n")
            f.write(f"Previous Block Hash: {data['previousblockhash']}\n")
            f.write(f"Merkle Root: {data['merkle_root']}\n")
            f.write(f"Number of Transactions: {data['tx_count']}\n")
            f.write(f"Timestamp: {data['timestamp']}\n")
        
        print("Successfully wrote to block-inspection.md!")

    # Also grab 4 TXIDs for Task 2
    txid_url = f"https://mempool.space/api/block/{block_hash}/txids"
    with urllib.request.urlopen(txid_url) as response:
        txids = json.loads(response.read().decode())
        print("\n--- 4 TXIDs for Task 2 ---")
        for i in range(4):
            print(f"Tx{i}: {txids[i]}")

except Exception as e:
    print(f"Error: {e}")
