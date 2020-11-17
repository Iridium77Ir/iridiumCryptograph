import lib.iridiumCrypt
class Crypter():

    def __init__(self, password):
        self.password = password

    def read_file(fileName):
        with open(fileName, 'rb') as file:
            msg = file.read()
        return msg
    
    def write_file(fileName, msg):
        with open(fileName, 'wb') as file:
            file.write(msg)

    def encrypt_file(self, encfileName):
        encrypted = lib.iridiumCrypt.Cryptographer.crypt(self.password, Crypter.read_file(encfileName))
        Crypter.write_file(encfileName + '.icr', encrypted)

    def decrypt_file(self, decfileName):
        decrypted = lib.iridiumCrypt.Cryptographer.crypt(self.password, Crypter.read_file(decfileName))
        Crypter.write_file('dec_' + decfileName[:-4], decrypted)