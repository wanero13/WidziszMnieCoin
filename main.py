import blockchainManager
import binascii
import Crypto.Random
from Crypto.PublicKey import RSA
from client import Client
from queue import Queue
from threading import Thread, Event
import time
import json
import hashlib
import binascii
from matplotlib import pylab
import pylab as pl
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA

random = Crypto.Random.new().read
priv = RSA.generate(1024, random)
pub = priv.publickey()
sign = PKCS1_v1_5.new(priv)
identityGenesis = binascii.hexlify(pub.exportKey(format='DER')).decode('ascii')

# Utworzenie użytkowników początkowych
User1 = Client('Adrian')
User2 = Client('Maria')
User3 = Client('Jan')
User4 = Client('Karol')

userList = []
userList.append(User1)
userList.append(User2)
userList.append(User3)
userList.append(User4)

# Stworzenie blockchainu

User1.initiateBlockchain(userList, priv, pub, sign, identityGenesis)
User2.initiateBlockchain(userList, priv, pub, sign, identityGenesis)
User3.initiateBlockchain(userList, priv, pub, sign, identityGenesis)
User4.initiateBlockchain(userList, priv, pub, sign, identityGenesis)

flag = True
proposed_block = None
transaction_list = []
proof = 0

tr1 = {
            'sender': User1.identity,
            'recipient': User2.identity,
            'coinID': 0,
            'signature': User1.sign(str(User1.identity) + str(User2.identity) + str(0))
        }
tr2 = {
            'sender': User1.identity,
            'recipient': User2.identity,
            'coinID': 1,
            'signature': User1.sign(str(User1.identity) + str(User2.identity) + str(1))
        }




def vlidate_block(user: Client):
    if user.validateBlock(proposed_block) and User1.valid_proof(transaction_list, User1.bcm.sumHash, proof):
        user.addBlock(proposed_block)
        return print("user1 potwierdza")
    else:
        return print("bład user 1")

def threadLoop1():
    global flag
    global proposed_block
    b = -1
    while flag:
        b = User1.proofofwork()
        if b != -1:
            print('proof: ' + str(b))
            print("wykopał User 1")
            flag = False
    if b == -1:
        return
    proposed_block = User1.proposeBlock(b)



def threadLoop2():

    global flag
    global proposed_block
    b = -1
    while flag:
        b = User2.proofofwork()
        if b != -1:
            print('proof: ' + str(b))
            print("wykopał User 2")
            flag = False
    if b == -1:
        return
    proposed_block = User2.proposeBlock(b)


def threadLoop3():
    global flag
    global proposed_block
    b = -1
    while flag:
        b = User3.proofofwork()
        if b != -1:
            print('proof: ' + str(b))
            print("wykopał User 3")
            flag = False
    if b == -1:
        return
    proposed_block = User3.proposeBlock(b)


def threadLoop4():
    global flag
    global proposed_block
    b = -1
    while flag:
        b = User4.proofofwork()
        if b != -1:
            print('proof: ' + str(b))
            print("wykopał User 4")
            flag = False
    if b == -1:
        return
    proposed_block = User4.proposeBlock(b)


thread1 = Thread(target=threadLoop1)
thread2 = Thread(target=threadLoop2)
thread3 = Thread(target=threadLoop3)
thread4 = Thread(target=threadLoop4)

def maketurn():
    #propose transactions
    transaction_list.append(tr1)
    transaction_list.append(tr2)
    #update transactions
    User1.updateTransactions(transaction_list)
    User2.updateTransactions(transaction_list)
    User3.updateTransactions(transaction_list)
    User4.updateTransactions(transaction_list)
    #start mining
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    #finish mining
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    #check block validity

    #add block if valid
    print(proposed_block)

maketurn()

