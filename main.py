import blockchainManager

Blockchain = blockchainManager.blockchainManager()

# while True:
#     print("1 - Dodaj blok")
#     print("2 - Sprawdź spójność")
#     print("3 - Zakończ")
#     option = input()
#     if option == '1':
#         print("Podaj zawartość")
#         content = input()
#         Blockchain.addBlock(content)
#     elif option == '2':
#         Blockchain.checkValid()
#     elif option == '3':
#         exit(1)
#     else:
#         print("Wybierz 1 lub 2")

User1 = blockchainManager.Client()
User2 = blockchainManager.Client()

t1 = Blockchain.new_transaction(User1.identity, User2.identity, '5btc')
t2 = Blockchain.new_transaction(User1.identity, User2.identity, '5btc')
Blockchain.addBlock(1)

t3 = Blockchain.new_transaction("user3", "user4", '2btc')
t4 = Blockchain.new_transaction("user2", "user4", '1btc')
Blockchain.addBlock(2)
print("Blockchain: ", Blockchain.chain)