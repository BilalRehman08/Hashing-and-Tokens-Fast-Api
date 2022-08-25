
from passlib.context import CryptContext


def verify_passwords(password):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    hashed_password = pwd_context.hash(password)
    result = pwd_context.verify(password, hashed_password)
    print("Original Password: ", password)
    print("Hashed Password: ", hashed_password)
    print("Verified or Not : ", result)
    return result


verify_passwords("Bilal")
