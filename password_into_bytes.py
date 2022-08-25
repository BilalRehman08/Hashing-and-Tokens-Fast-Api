from cryptography.fernet import Fernet
# Put this somewhere safe!
key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b"ok.")
token2 = f.encrypt(b"ok.")
print("token : ", token)
print("token2 : ", token2)
