class DiffieHellman(object):
    
    def __init__(self, public_key1, public_key2, private_key):
        self.public_key1 = public_key1
        self.public_key2 = public_key2
        self.private_key = private_key
        self.full_key = None
        
    def generate_partial_key(self):
        partial_key = self.public_key1**self.private_key
        partial_key = partial_key%self.public_key2
        return partial_key
    
    def generate_full_key(self, partial_key_r):
        full_key = partial_key_r**self.private_key
        full_key = full_key%self.public_key2
        self.full_key = full_key
        return full_key
    
    def encrypt_data(self, data):
        encrypted_data = ""
        key = self.full_key
        for c in data:
            encrypted_data += chr(ord(c)+key)
        return encrypted_data
    
    def decrypt_data(self, encrypted_data):
        decrypted_data = ""
        key = self.full_key
        for c in encrypted_data:
            decrypted_data += chr(ord(c)-key)
        return decrypted_data
