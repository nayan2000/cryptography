# ReverseCipher just reverses the string.

class ReverseCipher(object):

    def __init__(self, data):
        self.data = data

    def encrypt(self):
        encrypted_data = self.data[::-1]
        return encrypted_data
        
    def decrypt(self):
        decrypted_data = self.data[::-1]
        return decrypted_data
