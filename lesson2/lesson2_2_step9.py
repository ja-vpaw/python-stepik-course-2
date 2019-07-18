import simplecrypt

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()
    with open("passwords.txt", "r") as p:
        passwords = p.readlines()
        for i in passwords:
            i = i.strip()
            try:
                print(simplecrypt.decrypt(i,encrypted).decode('utf-8'))
                break
            except simplecrypt.DecryptionException:
                pass
