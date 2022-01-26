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
from random import randrange


class blockchainManager:

    def __init__(self):
        self.identityGenesis = None
        self.signer = None
        self.private_key = None
        self.public_key = None
        self.coinCounter = 0
        self.sumHash = 0
        self.chain = []
        self.pending_transactions = []
        self.userList = None
        self.proof = randrange(10000)
        self.last_correct = 0
        self.coinCounter

    def initiateBlockChain(self, userList, priv, pub, signer, identityG):
        # identyfikator chainManagera
        self.private_key = priv
        self.public_key = pub
        self.signer = signer
        self.identityGenesis = identityG

        self.userList = userList
        self.generateCoins()
        self.guess_hash = ''
        self.last_hash=self.sumHash
        guess = (str(self.pending_transactions) + str(self.last_hash) + str(self.last_correct)).encode()
        guess_hash = hashlib.sha3_512(guess).hexdigest()
        genessisBlock = {
            'id': len(self.chain) + 1,
            'miner': self.identityGenesis,
            'prevHash': '000',
            'timetamp': strftime("%d %b %Y %H:%M:%S", gmtime()),
            'transactions': self.pending_transactions,
            'proof': 0,
            'proofofwork': guess_hash
        }
        self.chain.append(genessisBlock)
        self.pending_transactions = []
        toCode = json.dumps(genessisBlock, sort_keys=1).encode()
        self.sumHash = hashlib.sha3_512(toCode).hexdigest()
        self.coinCounter = 4

    def sign(self, message):
        h = SHA.new(message.encode('utf8'))
        return binascii.hexlify(self.signer.sign(h)).decode('ascii')

    def updateTransactions(self, transactions):
        for tr in transactions:
            if self.checkTransaction(tr):
                self.pending_transactions.append(tr)

    def checkValid(self):
        prevHash = '000'
        flag = 0
        for block in self.chain:
            if block['prevHash'] != prevHash:
                print('Wykryto brak spójności w bloku: ' + str(block['id']))
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
                print('Spójność zachowana!' + '\n')

    def proposeBlock(self, proof, userID):
        self.gen_reward(self.identityGenesis, userID, self.coinCounter)
        block = {
            'id': len(self.chain) + 1,
            'miner': userID,
            'prevHash': self.sumHash,
            'timetamp': strftime("%d %b %Y %H:%M:%S", gmtime()),
            'transactions': self.pending_transactions,
            'proof': proof,
            'proofofwork': self.guess_hash
        }
        return block

    def addBlock(self, block):
        self.coinCounter = self.coinCounter + 1
        self.pending_transactions = []
        self.chain.append(block)
        toCode = json.dumps(block, sort_keys=1).encode()
        self.sumHash = hashlib.sha3_512(toCode).hexdigest()
        # print(self.chain)
        print("Guess_hash: " + self.guess_hash)

    @property
    def last_block(self):
        return self.chain[-1]

    def gen_reward(self, sender, recipient, coinID):
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'coinID': coinID,
            'signature': self.sign(str(self.identityGenesis) + str(recipient) + str(coinID))
        }

        self.pending_transactions.append(transaction)
        return self.last_block['id'] + 1

    def new_transaction(self, sender, recipient, coinID):
        transaction = {
            'sender': sender.identity,
            'recipient': recipient.identity,
            'coinID': coinID,
            'signature': sender.sign(str(sender.identity) + str(recipient.identity) + str(coinID))
        }

        if self.checkTransaction(transaction):
            self.pending_transactions.append(transaction)
        return self.last_block['id'] + 1

    def generateCoins(self):
        bcid = self.identityGenesis
        coin1 = {
            'sender': bcid,
            'recipient': self.userList[0].identity,
            'coinID': 0,
            'signature': self.sign(str(bcid) + str(self.userList[0].identity) + str(0))
        }
        coin2 = {
            'sender': self.identityGenesis,
            'recipient': self.userList[0].identity,
            'coinID': 1,
            'signature': self.sign(str(bcid) + str(self.userList[0].identity) + str(1))
        }
        coin3 = {
            'sender': self.identityGenesis,
            'recipient': self.userList[2].identity,
            'coinID': 2,
            'signature': self.sign(str(bcid) + str(self.userList[2].identity) + str(2))
        }
        coin4 = {
            'sender': self.identityGenesis,
            'recipient': self.userList[2].identity,
            'coinID': 3,
            'signature': self.sign(str(bcid) + str(self.userList[2].identity) + str(3))
        }
        self.pending_transactions.append(coin1)
        self.pending_transactions.append(coin2)
        self.pending_transactions.append(coin3)
        self.pending_transactions.append(coin4)

    def checkWallet(self, userID):
        owned = []
        for block in self.chain:
            for transaction in block['transactions']:
                if transaction['recipient'] == userID:
                    coinID = int(transaction['coinID'])
                    if coinID not in owned:
                        owned.append(coinID)
                if transaction['sender'] == userID:
                    coinID = int(transaction['coinID'])
                    if coinID in owned:
                        owned.remove(coinID)
        # print('Posiadane Coiny ' + str(owned) + '\n')
        return owned

    def checkTransaction(self, transaction):
        coinID = int(transaction['coinID'])
        owned = self.checkWallet(transaction['sender'])
        if coinID in owned:
            for ordered in self.pending_transactions:
                if ordered["coinID"] == coinID:
                    print('Transakcja z tym coinem została już zlecona do realizacji')
                    return False
            # print('Transakcja zgodna')
            return True
        else:
            print('Transakcja niezgodna')
            return False

    def addUser(self, user):
        self.userList.append(user)

    # def validateCoin(self, coinID):
    #     return True

    # Sprawdzenie podpisu z wiadomością
    def validateSignature(self, identity, transaction):
        pubkey = RSA.importKey(binascii.unhexlify(identity))
        verifier = PKCS1_v1_5.new(pubkey)
        message = str(transaction['sender']) + str(transaction['recipient']) + str(transaction['coinID'])
        h = SHA.new(message.encode('utf8'))
        return verifier.verify(h, binascii.unhexlify(transaction['signature']))

    def checkCurrentBlock(self):
        for tr in self.pending_transactions:
            if not self.validateSignature(tr['sender'], tr):
                return False
        return True

    def checkBlock(self, block):
        for tr in block['transactions']:
            if not self.validateSignature(tr['sender'], tr):
                return False
        return True

    def proof_of_work(self):
        # last_block = self.chain[-1]
        last_hash = self.sumHash
        guessed = self.valid_proof(self.pending_transactions, last_hash, self.proof)
        if guessed == -1:
            self.proof += 1
            return -1
        else:
            correcproof = self.proof
            self.last_correct=self.proof
            self.proof = randrange(10000)
            return correcproof

    MINING_DIFFICULTY = 4

    def valid_proof(self, pending_transactions, last_hash, proof, difficulty=MINING_DIFFICULTY):
        guess = (str(pending_transactions) + str(last_hash) + str(proof)).encode()
        guess_hash = hashlib.sha3_512(guess).hexdigest()
        if guess_hash[:difficulty] == '0' * difficulty:
            self.guess_hash = guess_hash
            print(guess_hash)
            return guess_hash
        else:
            return -1

