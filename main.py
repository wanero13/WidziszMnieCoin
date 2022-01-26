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


def threadLoop1(b):
    global flag
    global proposed_block
    while flag:
        b = User1.proofofwork()
        if b != -1:
            flag = False
    if b == -1:
        return
    proposed_block = User1.proposeBlock(b)


def threadLoop2(b):
    global flag
    global proposed_block
    while flag:
        b = User2.proofofwork()
        if b != -1:
            flag = False
    if b == -1:
        return
    proposed_block = User2.proposeBlock(b)


def threadLoop3(b):
    global flag
    global proposed_block
    while flag:
        b = User3.proofofwork()
        if b != -1:
            flag = False
    if b == -1:
        return
    proposed_block = User3.proposeBlock(b)


def threadLoop4(b):
    global flag
    global proposed_block
    while flag:
        b = User4.proofofwork()
        if b != -1:
            flag = False
    if b == -1:
        return
    proposed_block = User4.proposeBlock(b)


thread1 = Thread(target=threadLoop1, args=(-1,))
thread2 = Thread(target=threadLoop2, args=(-1,))
thread3 = Thread(target=threadLoop3, args=(-1,))
thread4 = Thread(target=threadLoop4, args=(-1,))

def maketurn():
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()

    print(proposed_block)

maketurn()

