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
import blockchainManager


class Client:
    def __init__(self, name):
        random = Crypto.Random.new().read
        self._private_key = RSA.generate(1024, random)
        self._public_key = self._private_key.publickey()
        self._signer = PKCS1_v1_5.new(self._private_key)
        self.name = name
        self.bcm = blockchainManager.blockchainManager()

    @property
    def identity(self):
        return binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii')

    def sign(self, message):
        h = SHA.new(message.encode('utf8'))
        return binascii.hexlify(self._signer.sign(h)).decode('ascii')

    def initiateBlockchain(self, userList):
        return self.bcm.initiateBlockChain(userList)

    def proofofwork(self):
        return self.bcm.proof_of_work()

    def proposeBlock(self, proof):
        return self.bcm.proposeBlock(proof)

    def addBlock(self, block):
        return self.bcm.addBlock(block=block)

    def updateTransactions(self, transactions):
        return self.bcm.updateTransactions(transactions)

    def addTransaction(self, sender, recipient, coinID):
        return self.bcm.new_transaction(sender=sender, recipient=recipient, coinID=coinID)
