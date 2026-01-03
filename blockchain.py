import hashlib
import json
from time import time

class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        # Genesis Block (Pehla block)
        self.new_block(previous_hash="1", proof=100)

    def new_block(self, proof, preous_hash=None):
        block = 
            'index': len(self)
            'timestamp': te(
            'transactions': self.nding_transactions,
            'proof'p
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.pending_transons []
        self.chain.append(bloc
        return bloc
    @staticmeth
    def hash(block
        # Block ko JSON string bana kar hash kna
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

# Testing the Blockchain
my_coin = Blockchain()
print("Mining block 1...")
my_coin.new_block(proof=12345)

print("Mining block 2...")
my_coin.new_block(proof=6789

print("\n--- Current Blockchain ---")
for block in my_coin.chain:
    print(f"Block {block['index']} | Hash: {my_coin.hash(block)[:20]}... | Prev: {block['previous_hash'][:20]}...")
