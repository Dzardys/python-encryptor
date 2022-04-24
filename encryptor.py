from cryptography.fernet import Fernet
import os
import os.path
def start():
    print("Vítej v jednoduchém šifrovacím programu. Pomocí tohoto programu můžeš šifrovat i dešifrovat soubory, avšak pamatuj, že jej užíváš na vlastní riziko!")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Nyní si vyber, jakou úlohu chceš, aby program vykonal. Před šifrováním si však budeš muset vytvořit šifrovací klíč, před dešifrováním zase bude potřeba, aby takový klíč existoval.")
    print("[1] - Vytvořit klíč [2] - Zašifrovat soubor [3] - Dešifrovat soubor")
    choice = input()
    match choice:
        case "1":
            generatekey()
        case "2":
            encrypt()
        case "3":
            decrypt()
        case _:
            print("Špatná volba, ukončuji program...")
            quit()
          
def generatekey():
    key = Fernet.generate_key()
    print("Zadej název souboru: ")
    keypath = input()
    with open(keypath + ".key", 'wb') as unlock:
        unlock.write(key)
    with open(keypath + ".key", 'rb') as unlock:
        key = unlock.read()
    print("Soubor s klíčem byl vytvořen, nezapomeňte si jej zálohovat, abyste mohli získat přístup k souboru. Klíč: ")
    print(key)
    print("Přeješ si dále pokračovat? Vyber možnost.")
    print("[1] - Šifrovat soubor s užitím klíče [2] - Dešifrovat soubor [3] - Vytvořit nový klíč [4] - Ukončit aplikaci ")
    choice = input()
    match choice:
        case "1":
            encrypt()
        case "2":
            decrypt()
        case "3":
            generatekey()
        case "4":
            quit()
        case _:
            print("Špatná volba, ukončuji program...")
            quit()

def encrypt():
    print("Zadej cestu ke klíči (stačí [název].key nebo úplná cesta): ")
    path = input();
    isFile = os.path.isfile(path)
    
    if isFile == True:
        if(path.endswith(".key")):
            with open(path, 'rb') as filekey:
                key = filekey.read()
            fernet = Fernet(key)
            print("Zadej cestu k souboru: ")
            file = input();
            isFile2 = os.path.isfile(file)
            
            if isFile2 == True:
                with open(file, 'rb') as ori:
                    original = ori.read()
                encrypted = fernet.encrypt(original)
                with open(file, 'wb') as encrypted_file:
                    encrypted_file.write(encrypted);
                print("Soubor úspěšně zašifrován.")
                print("Přeješ si pokračovat?")
                print("[1] - Vytvořit nový klíč [2] - Šifrovat jiný soubor [3] - Dešifrovat soubor [4] - Ukončit aplikaci")
                choice = input()
                match choice:
                    case "1":
                        generatekey()
                    case "2":
                        encrypt()
                    case "3":
                        decrypt()
                    case "4":
                        quit()
                    case _:
                        print("Neplatná volba. Ukončuji aplikaci...")
                        quit()
            else:
                print("Neplatný soubor k zašifrování.")
                quit()
        else:
            print("Vyybrán neplatný soubor s klíčem. Ukončuji program...")
            quit()
    else:
        print("Zadaná cesta neodkazuje na klíč. Ukončuji program...")
        quit()

def decrypt():
    print("Zadej cestu ke klíči (stačí [název].key nebo úplná cesta): ")
    path = input()
    isFile = os.path.isfile(path)
    
    if isFile == True:
        if(path.endswith(".key")):
            with open(path, 'rb') as filekey:
                key = filekey.read()
            fernet = Fernet(key)
            print("Zadej cestu k souboru: ")
            file = input()
            isFile2 = os.path.isfile(file)

            if isFile2 == True:
                with open(file, 'rb') as enc_file:
                    encrypted = enc_file.read()
                decrypted = fernet.decrypt(encrypted)
                with open(file, 'wb') as dec_file:
                    dec_file.write(decrypted)
                print("Soubor úspěšně dešifrován. Přejete si pokračovat?")
                print("[1] - Vytvořit nový klíč [2] - Šifrovat nový soubor [3] - Dešifrovat jiný soubor [4] - Ukončit aplikaci")
                choice = input()
                match choice:
                    case "1":
                        generatekey()
                    case "2":
                        encrypt()
                    case "3":
                        decrypt()
                    case "4":
                        quit()
                    case _:
                        print("Neplatná volba. Ukončuji program...")
            else:
                print("Neplatná cesta k souboru, ukončuji program...")
                quit()
        else:
            print("Neplatný soubor s klíčem, ukončuji program...")
            quit()
    else:
        print("Zadaná cesta neodkazuje na klíč. Ukončuji aplikaci...")
        quit()
start()
