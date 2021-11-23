import blockchainManager

Blockchain = blockchainManager.blockchainManager()

print(Blockchain)

User1 = blockchainManager.Client('Adrian')
User2 = blockchainManager.Client('Maria')
User3 = blockchainManager.Client('Jan')
User4 = blockchainManager.Client('Karol')

t1 = Blockchain.new_transaction(User1.identity, User2.identity, 1)
t2 = Blockchain.new_transaction(User1.identity, User2.identity, 2)
Blockchain.addBlock(1)

t3 = Blockchain.new_transaction(User3.identity, User4.identity, 3)
t4 = Blockchain.new_transaction(User3.identity, User2.identity, 4)
Blockchain.addBlock(2)
print("Blockchain: ", Blockchain.chain)

userList = []
userList.append(User1)
userList.append(User2)
userList.append(User3)
userList.append(User4)

while True:
    print("1 - Dodaj blok")
    print("2 - Sprawdź spójność")
    print("3 - Lista użytkowników")
    print("4 - Wybierz użytkownika")
    print("0 - Zakończ")
    option = input()
    if option == '1':
        print("Podaj zawartość")
        content = input()
        Blockchain.addBlock(content)
    elif option == '2':
        Blockchain.checkValid()
    elif option == '3':
        for user in userList:
            print(user.name + ', ', end='')
        print()
    elif option == '4':
        userFlag = True
        selectedUser = input()
        user = userList[int(selectedUser)]
        while userFlag:
            print(user.name + """
1 - Sprawdź portfel
2 - Zleć transakcję
0 - Wyjdź
            """)
            userOption = input()
            if userOption == '1':
                Blockchain.checkWallet(user.identity)
            elif userOption == '2':
                print('Podaj odbiorcę')
                selectedRecipient = input()
                recipient = userList[int(selectedRecipient)]
                selectedCoin = input()
                Blockchain.new_transaction(user.identity, recipient, selectedCoin)
            elif userOption == '0':
                userFlag = False
    elif option == '0':
        exit(1)
    else:
        print("Wybierz 1 lub 2")

