from hashlib import sha256
from datetime import datetime


class Block:
    def __init__(self, data, previous_block_hash):
        self.timestamp = datetime.utcnow()
        self.data = data
        self.previous_block_hash = previous_block_hash
        self.hash = None
        self.calculate_valid_hash()

    def is_hash_valid(self, temp_hash):
        return temp_hash.startswith('0' * 4)  # expose this

    def to_string(self):
        return f"{self.data}\t{self.timestamp}\t{self.previous_block_hash}"

    def calculate_valid_hash(self):
        temp_hash = ''  # should this be configurable ?
        nonce = 0  # should this be configurable ? Read on how to choose nonce

        while not self.is_hash_valid(temp_hash):
            temp = self.to_string() + str(nonce)  # needs to be broken into functions
            temp_hash = sha256(temp.encode()).hexdigest()  # need of a diff hash algo in future ?
            nonce += 1  # might change based on nonce strategy

        self.hash = temp_hash
# hash usage might not be proper. have to check
