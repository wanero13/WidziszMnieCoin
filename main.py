import blockchainManager

Blockchain = blockchainManager.blockchainManager()

User1 = blockchainManager.Client('Adrian')
User2 = blockchainManager.Client('Maria')
User3 = blockchainManager.Client('Jan')
User4 = blockchainManager.Client('Karol')
Blockchain.addUser(User1)
Blockchain.addUser(User2)
Blockchain.addUser(User3)
Blockchain.addUser(User4)
print(Blockchain.userList)

Blockchain.generateCoins()
Blockchain.addBlock('proof')
print(Blockchain.chain)



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
        for user in Blockchain.userList:
            print(user.name + ', ', end='')
        print()
    elif option == '4':
        userFlag = True
        selectedUser = input()
        user = Blockchain.userList[int(selectedUser)]
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
                recipient = Blockchain.userList[int(selectedRecipient)]
                selectedCoin = input()
                Blockchain.new_transaction(user.identity, recipient, selectedCoin)
            elif userOption == '0':
                userFlag = False
    elif option == '0':
        exit(1)
    else:
        print("Wybierz 1 lub 2")

