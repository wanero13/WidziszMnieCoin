import json
import hashlib
from time import *

import binascii
from matplotlib import pylab
import pylab as pl

import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5


class Client:
   def __init__(self):
      random = Crypto.Random.new().read
      self._private_key = RSA.generate(1024, random)
      self._public_key = self._private_key.publickey()
      self._signer = PKCS1_v1_5.new(self._private_key)

   @property
   def identity(self):
    return binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii')


class blockchainManager:

    def __init__(self):
        self.chain = []
        self.pending_transactions = []

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


    def addBlock(self, proof):
        block = {
            'id': len(self.chain)+1,
            'prevHash': self.sumHash,
            'timetamp': strftime("%d %b %Y %H:%M:%S", gmtime()),
            'transactions': self.pending_transactions,
            'proof' : proof,
        }
        self.pending_transactions = []
        self.chain.append(block)
        toCode = json.dumps(block,sort_keys=1).encode()
        self.sumHash = hashlib.sha3_512(toCode).hexdigest()
        print(self.chain)

    @property
    def last_block(self):
        return self.chain[-1]

    def new_transaction(self, sender, recipient, amount):
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        }
        self.pending_transactions.append(transaction)
        return self.last_block['id'] + 1

