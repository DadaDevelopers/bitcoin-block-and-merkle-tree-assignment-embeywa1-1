cat <<EOF > README.md
# Bitcoin Block and Merkle Tree Assignment

## Task 1: Block Inspection
I used the Mempool.space API to inspect **Block 840,000** (The 2024 Halving Block). 

- **Block Height:** 840,000
- **Block Hash:** 0000000000000000000320283a032748cef8227873ff4872689bf23f1cda83a5
- **Merkle Root:** 18e8749a9415446062f6d2f3068e27c62b5364177b9605f8841b590e826e7a2b

## Task 2: Merkle Tree Visualization
Below is the visualization of the Merkle Tree construction using the first 4 transactions from the block.

\`\`\`text
                    [ Merkle Root ]
                 (Hash of Node A + B)
                        /    \
            [ Node A ]          [ Node B ]
          (Hash of 0+1)        (Hash of 2+3)
            /      \              /      \
        [ Tx 0 ]  [ Tx 1 ]    [ Tx 2 ]  [ Tx 3 ]
        a0db...   2bb8...     152b...   e791...
\`\`\`

### Explanation of Process
1. **Data Acquisition:** I used a Python script (\`fetch_block.py\`) to query the Mempool.space API for block 840,000.
2. **Hashing Algorithm:** Bitcoin uses **Double SHA-256** ($SHA256(SHA256(data))$).
3. **Byte Order:** Bitcoin hashes are processed in **Little-Endian** format. When concatenating two hashes, they must be reversed, hashed, and then reversed back for the final hex display.
4. **Tree Construction:**
   - Transactions are paired at the base (Leaf nodes).
   - Each pair is hashed to create a parent node.
   - This process continues upward until a single **Merkle Root** is found. This root provides a cryptographic summary of all transactions in the block.

## How to Run the Code
1. Navigate to the \`code/\` directory.
2. Run \`python3 merkle_tree.py\` to see the manual calculation of the Merkle nodes.
EOF
