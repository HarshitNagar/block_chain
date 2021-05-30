from blockchain import Blockchain


def test_run():
    test_blockchain = Blockchain()

    test_blockchain.add_new_block(data = "block 1")
    test_blockchain.add_new_block(data = "block 2")
    test_blockchain.add_new_block(data = "block 3")

    for block in test_blockchain.get_blocks():
        print(f"{block.data}\n{block.hash}\n{block.previous_block_hash}\n{block.timestamp}\n\n")


if __name__ == "__main__":
    test_run()
