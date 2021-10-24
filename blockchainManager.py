import json
import hashlib

class blockchainManager:

    def __init__(self):
        self.chain = []

        genessisBlock = {
            'id': len(self.chain)+1,
            'prevHash': 0,
            'content': 'content',
        }
        self.chain.append(genessisBlock)
        toCode = json.dumps(genessisBlock, sort_keys=1).encode()
        self.sumHash = hashlib.sha3_512(toCode).hexdigest()

    def checkValid(self):
        prevHash = 0
        flag = 0
        for block in self.chain:
            if block['prevHash'] != prevHash:
                print('Wykryto brak spójności w bloku: ' + block)
                flag = 1
                break
            prevBytes = json.dumps(block, sort_keys=1).encode()
            prevHash = hashlib.sha3_512(prevBytes).hexdigest()
        lastBlock = self.chain[-1]
        lastBlockBytes = json.dumps(lastBlock, sort_keys=1).encode()
        lastBlockHash = hashlib.sha3_512(lastBlockBytes).hexdigest()
        if flag == 0:
            if lastBlockHash != self.sumHash:
                print('Wykryto brak spójności w bloku: ' + lastBlock)
            else:
                print('Spójność zachowana!')


    def addBlock(self, content):
        block = {
            'id': len(self.chain)+1,
            'prevHash': self.sumHash,
            'content': content,
        }
        self.chain.append(block)
        toCode = json.dumps(block,sort_keys=1).encode()
        self.sumHash = hashlib.sha3_512(toCode).hexdigest()
        print(self.chain)