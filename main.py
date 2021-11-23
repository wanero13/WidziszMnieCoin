import blockchainManager



#Utworzenie użytkowników początkowych
User1 = blockchainManager.Client('Adrian')
User2 = blockchainManager.Client('Maria')
User3 = blockchainManager.Client('Jan')
User4 = blockchainManager.Client('Karol')
userList=[]
userList.append(User1)
userList.append(User2)
userList.append(User3)
userList.append(User4)

#Stworzenie blockchainu
Blockchain = blockchainManager.blockchainManager(userList)

while True:
    print("""
1 - Dodaj blok
2 - Sprawdź spójność
3 - Lista użytkowników
4 - Wybierz użytkownika
0 - Zakończ
""")
    option = input()
    if option == '1':
        print("Podaj zawartość")
        content = input()
        Blockchain.addBlock(content)
    elif option == '2':
        print(Blockchain.chain)
        Blockchain.checkValid()
    elif option == '3':
        for user in Blockchain.userList:
            print(user.name + ', ', end='')
        print()
    elif option == '4':
# Menu użytkownika
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
                print(Blockchain.pending_transactions)
            elif userOption == '2':
                print('Podaj odbiorcę')
                selectedRecipient = input()
                recipient = Blockchain.userList[int(selectedRecipient)]
                print('Podaj CoinID')
                selectedCoin = input()
                Blockchain.new_transaction(user.identity, recipient.identity, int(selectedCoin))
            elif userOption == '0':
                userFlag = False
            else:
                print("Wybierz poprawną opcję")
    elif option == '0':
        exit(1)
    else:
        print("Wybierz poprawną opcję")
