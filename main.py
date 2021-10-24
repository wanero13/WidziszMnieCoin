import blockchainManager


Blockchain = blockchainManager.blockchainManager()

while True:
    print("1 - Dodaj blok")
    print("2 - Sprawdź spójność")
    print("3 - Zakończ")
    option = input()
    if option == '1':
        print("Podaj zawartość")
        content = input()
        Blockchain.addBlock(content)
    elif option == '2':
        Blockchain.checkValid()
    elif option == '3':
        exit(1)
    else:
        print("Wybierz 1 lub 2")