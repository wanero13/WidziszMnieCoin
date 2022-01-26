import blockchainManager
import binascii
import Crypto.Random
from Crypto.PublicKey import RSA
from client import Client
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

User1.initiateBlockchain(userList)
User2.initiateBlockchain(userList)
User3.initiateBlockchain(userList)
User4.initiateBlockchain(userList)


