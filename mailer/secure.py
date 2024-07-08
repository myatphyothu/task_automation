from cryptography.fernet import Fernet

text = 'harrick123'


def generate_newkey():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as keyfile:
        keyfile.write(key)

#generate_newkey()

def load_key():
    return open('key.key', 'r').read()

def decrypt(data):
    key = load_key()
    f = Fernet(key)
    return f.decrypt(data)

def test():
    message = text.encode()
    key = load_key()
    f = Fernet(key)
    encrypted = f.encrypt(message)

    print(encrypted)

    decrypted = f.decrypt(encrypted)
    print(decrypted)


