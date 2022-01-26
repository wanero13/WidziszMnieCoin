import blockchainManager
import binascii
import Crypto.Random
from Crypto.PublicKey import RSA
from client import Client

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

# while True:
#     print("""
# 1 - Dodaj blok
# 2 - Sprawdź spójność
# 3 - Lista użytkowników
# 4 - Wybierz użytkownika
# 0 - Zakończ
# """)
#     option = input()
#     if option == '1':
#         print("Podaj zawartość")
#         content = input()
#         Blockchain.addBlock(content)
#     elif option == '2':
#         print(Blockchain.chain)
#         Blockchain.checkValid()
#     elif option == '3':
#         print('Lista użytkoniwków: ')
#         for user in Blockchain.userList:
#             print(user.name + ', ', end='')
#         print()
#     elif option == '4':
#         print('Podaj ID użytkownika (0-3): ')
# # Menu użytkownika

#         userFlag = True
#         selectedUser = input()
#         user = Blockchain.userList[int(selectedUser)]
#         while userFlag:
#             print(user.name + """
# 1 - Sprawdź portfel
# 2 - Zleć transakcję
# 0 - Wyjdź
#             """)
#             userOption = input()
#             if userOption == '1':
#                 Blockchain.checkWallet(user.identity)
#             elif userOption == '2':
#                 print('Podaj ID odbiorcy')
#                 selectedRecipient = input()
#                 recipient = Blockchain.userList[int(selectedRecipient)]
#                 print('Podaj CoinID')
#                 selectedCoin = input()
#                 Blockchain.new_transaction(user.identity, recipient.identity, int(selectedCoin))
#             elif userOption == '0':
#                 userFlag = False
#             else:
#                 print("Wybierz poprawną opcję")
#     elif option == '0':
#         exit(1)
#     else:
#         print("Wybierz poprawną opcję")

# Dodanie bloku z 2 transakcjami
# Blockchain.new_transaction(User1, User2, 0)
# Blockchain.new_transaction(User3, User4, 2)
# Blockchain.addBlock('proof')
#
# # Wypisanie zawartosci portfeli po dodaniu bloku
# Blockchain.checkWallet(User1.identity)
# Blockchain.checkWallet(User2.identity)
# Blockchain.checkWallet(User3.identity)
# Blockchain.checkWallet(User4.identity)
#
# #Kolejny blok z tranzakcjami
# Blockchain.new_transaction(User4, User1, 2)
# Blockchain.new_transaction(User3, User2, 3)
# Blockchain.new_transaction(User1, User2, 1)
# Blockchain.addBlock('blok2')
#
# # Wypisanie zawartosci portfeli po dodaniu bloku
# Blockchain.checkWallet(User1.identity)
# Blockchain.checkWallet(User2.identity)
# Blockchain.checkWallet(User3.identity)
# Blockchain.checkWallet(User4.identity)
#
# # Sprawdzenie spójności
# Blockchain.checkValid()
#
# # Wygenerownie pary kluczy do testowania
# random = Crypto.Random.new().read
# fakepair = RSA.generate(1024, random)
# fakepub = binascii.hexlify(fakepair.publickey().exportKey(format='DER')).decode('ascii')
#
# #Dodanie tranzakcji i sprawdzenie podpisu
# Blockchain.new_transaction(User2, User3, 1)
#
# tr1 = Blockchain.pending_transactions[0]
# if Blockchain.validateSignature(User2.identity, tr1):
#     print('Tranakcja podpisana poprawnie')
# else:
#     print('Tranzakcja podpisana niepoprawnie')
#
# Blockchain.new_transaction(User2, User4, 0)
# tr2 = Blockchain.pending_transactions[1]
# tr2['sender'] = fakepub
#
# tr1 = Blockchain.pending_transactions[0]
# if Blockchain.validateSignature(User2.identity, tr2):
#     print('Tranakcja podpisana poprawnie')
# else:
#     print('Tranzakcja podpisana niepoprawnie')
#
#
#
# # Weryfikacja genesis
# genesis = Blockchain.chain[0]
# if Blockchain.checkBlock(genesis):
#     print('Blok genesis zawiera poprawnie podpisy')
# else:
#     print('Blok genesis zawiera niepoprawne podpisy')
#
# genesis['transactions'][0]['sender'] = str(fakepub)
#
# genesis = Blockchain.chain[0]
# if Blockchain.checkBlock(genesis):
#     print('Blok genesis zawiera poprawnie podpisy')
# else:
#     print('Blok genesis zawiera niepoprawne podpisy')
#
# # Ponowana walidacja spójności
# Blockchain.checkValid()



