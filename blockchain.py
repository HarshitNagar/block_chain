from block import Block


class Blockchain:
    def __init__(self):
        self.blocks = []
        self.set_genesis_block()

    def set_genesis_block(self):
        data = "g_e_n_e_s_i_s__b_l_o_c_k"  # no reason. bakchodi
        previous_block_hash = '0'*64  # 32/64/128 ? expose or not ?
        genesis_block = Block(data = data, previous_block_hash = previous_block_hash)

        self.blocks.append(genesis_block)

    def get_hash_of_last_block(self):
        last_block = self.blocks[-1]
        last_block_hash = last_block.hash

        return last_block_hash

    def add_new_block(self, data):
        previous_block_hash = self.get_hash_of_last_block()
        new_block = Block(data = data, previous_block_hash = previous_block_hash)

        self.blocks.append(new_block)

    def get_blocks(self):
        return self.blocks
